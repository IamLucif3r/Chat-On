import threading
import socket
# Now this Host is the IP address of the Server, over which it is running.
# I've user my localhost.
host = "127.0.0.1"
port = 55555 # Choose any random port which is not so common (like 80)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the server to IP Address
server.bind((host, port))
#Start Listening Mode
server.listen()
#List to contain the Clients getting connected and nicknames
clients = []
nicknames = []

# 1.Broadcasting Method
def broadcast(message):
    for client in clients:
        client.send(message)

# 2.Recieving Messages from client then broadcasting
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # As soon as message recieved, broadcast it.
            broadcast(message)
        except:
            index = clients.index(client)
            #Index is used to remove client from list after getting diconnected
            client.remove(client)
            client.close
            nickname = nicknames[index]
            broadcast(f'{nickname} left the Chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break
# Main Recieve method
def recieve():
    while True:
        client, address = server.accept()
        print("Connected with {str(address)}")
        # Ask the clients for Nicknames
        client.send('NICK'.encode('ascii'))
        nickname - client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joine dthe Chat'.encode('ascii'))
        client.send('Connected to the Server!'.encode('ascii'))

        # Handling Multiple Clients Simultaneously
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

#Calling the main method
print('Server is Listening ...')
recieve()