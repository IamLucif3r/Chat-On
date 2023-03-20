import threading
import socket

# Encoding format for messages
ENCODING = 'ascii'

# `HOST` is the IPv4 address of the Server, over which it is running.
# I've used my local area network IPv4 address.
HOST = "192.168.2.104"
PORT = 5555  # Choose any random port which is not so common (like 80 is very common)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to IP Address
server.bind((HOST, PORT))
# Start Listening Mode
server.listen()
# List to contain the Clients getting connected and nicknames
clients = []
nicknames = []


# 1.Broadcasting Method
def broadcast(message):
    for client in clients:
        client.send(message)


# 2.Receiving Messages from client then broadcasting
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode(ENCODING).startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = message.decode(ENCODING)[5:]
                    kick_user(name_to_kick)
                else:
                    client.send('Command Refused!'.encode(ENCODING))
            elif message.decode(ENCODING).startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_ban = message.decode(ENCODING)[4:]
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}\n')
                    print(f'{name_to_ban} was banned by the Admin!')
                else:
                    client.send('Command Refused!'.encode(ENCODING))
            else:
                broadcast(message)  # As soon as message received, broadcast it.

        except socket.error:
            if client in clients:
                index = clients.index(client)
                # Index is used to remove client from list after getting disconnected
                client.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the Chat!'.encode(ENCODING))
                nicknames.remove(nickname)
                break


# Main Receive method
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        # Ask the clients for Nicknames
        client.send('NICK'.encode(ENCODING))
        nickname = client.recv(1024).decode(ENCODING)
        # If the Client is an Admin prompt for the password.
        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if nickname + '\n' in bans:
            client.send('BAN'.encode(ENCODING))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode(ENCODING))
            password = client.recv(1024).decode(ENCODING)
            # I know it is lame, but my focus is mainly for Chat system and not a Login System
            if password != 'adminpass':
                client.send('REFUSE'.encode(ENCODING))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the Chat'.encode(ENCODING))
        client.send('Connected to the Server!'.encode(ENCODING))

        # Handling Multiple Clients Simultaneously
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You Were Kicked from Chat !'.encode(ENCODING))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked from the server!'.encode(ENCODING))


# Calling the main method
print('Server is Listening ...')
receive()
