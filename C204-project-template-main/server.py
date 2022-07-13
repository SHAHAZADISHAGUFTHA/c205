import socket
from threading import thread
SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = None
CLIENTS = {}


def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        playerName = player_socket.recv(1024).decode().strip()
        if (len(CLIENTS.keys()) ==0):
            CLIENTS[playerName] = {"planet_type": "player1"}
        else: 
            CLIENTS[playerName] = {"player_type" : "player2"}
    CLIENTS[playerName]["player_socket"] = player_socket
    CLIENTS[playerName]["address"] = addr
    CLIENTS[playerName]["playerName"] = playerName
    CLIENTS[playerName]["turn"] = False
    print(f"connection establish with {playerName} : {addr}")
def setup():
    print("\n\t\t\t\t\t*** Welcome to TAMBOLA GAME***\n")
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)
    print("\t\t\t\t SERVER IS FOR INCOMMING CONNECTIONS...")

    acceptConnections()
setup()
