# Chat-On 🐍 : A Python-Based Chat Room
![](https://img.shields.io/apm/l/vim-mode?style=plastic)
![](https://img.shields.io/pypi/pyversions/Django?style=plastic)
![](https://img.shields.io/github/last-commit/IamLucif3r/Chat-On)
![](https://img.shields.io/github/commit-activity/w/IamLucif3r/Chat-On?style=plastic)


This is an advanced Python-based Secure Chat room. The project is entirely based on the Socket Progamming; done using Python. A server is set to the listening mode, with a specific IP Address and Port number (that can be edited in the script) and clients are made to connect to the server, after which they are promopted to enter a nickname. The messages are then broadcasted to all the clients present. 

### 👉 Introduction

#### 👉 Sockets
<b> Sockets </b> and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP. <br><br>
<img align="center" height=300px src=https://github.com/IamLucif3r/Chat-On/blob/main/assets/Python-Sockets-Tutorial_Watermarked.webp> <br>
Image Credit:[Real Python](https://realpython.com/python-sockets/)

#### 👉 TCP Socket
In the diagram below, given the sequence of socket API calls and data flow for TCP:
<br><br>
<img align="center" src=https://github.com/IamLucif3r/Chat-On/blob/main/assets/Screenshot%20at%202021-05-21%2010-47-40.png height=500px>

## 👉 Usage

1. We will have to start our Server first.
``` shell
Python Server.py
```
<b>Note: </b> Before running the server, make sure to edit the IP address and Port number. By default it is running on Localhost:5555 <br><br>
2. Run the Client file, to start the conversation. 
``` Shell
Python Client.py
```
<br>
3. Now Enter a nickname and start your chatting. 


## v1.2 Updates
- The version 1.2 supports the Admin Controls. The admin has certain controls over the chat room.
- The enhanced features include
  - <b>Kick Feature</b> : Admin can kick anyone from the Chat Room.
  - <b>Ban Feature</b> : Admin can ban certain members from re-joining the Chat Room. These names are added in a List.
- Minor Bug Fixes.

<hr>

## Demo-Video 📹
<br>
This is a demo video of the Working of this project.
<br><br>

![](https://github.com/IamLucif3r/Chat-On/blob/main/assets/2021-05-22-15-10-08.gif)

<hr>

## Contribution
👉 You're welcome to contribute in this project. Make a new branch, Commit your changes and send me a Pull Request. I'll merge it in the main branch ✌

[EduardoJTR](https://github.com/EduardoJTR) : Added Menu System

## Contact
📬 Contact with me via email: [sanmol016@gmail.com](mailto:sanmol016@gmail.com)
