import socket
import threading
import datetime
import configparser
from cryptography.fernet import Fernet

# Connection data / configparser
config = configparser.ConfigParser()
config.read('chatconfig.ini')
host = config['SERVER']['ip']
port = int(config['SERVER']['port'])

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print("server is running at", host, ":", port, "-> listen...")
server.listen()

# Lists For Clients and Their Nicknames
clients = []

# encryption / decryption
file = open('keyfile.key', 'rb')
keyed = file.read()  # key is type byte
file.close()
fed = Fernet(keyed)

# Sending Messages To All Connected Clients
def broadcast(message):
    msg = fed.encrypt(message)
    for client in clients:
        client.send(msg)

# Handling Msg From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            print(datetime.datetime.now(), "-", "connected from {}".format(str(client)), message)
            empty = b''
            if message != empty:
                broadcast(message)
            else:
                sysmsg = "a client has disconnected..."
                message = fed.encrypt(sysmsg.encode('utf-8'))
                broadcast(message)

        except:
            # Removing And Closing Clients
            clients.index(client)
            clients.remove(client)
            client.close()
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("a client is connected from {}".format(str(address)))
        clients.append(client)

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
