import socket
import threading
from cryptography.fernet import Fernet
import datetime
import configparser

# Choosing Nickname
nickname = input("choose your nickname: ")

# Encryption
file = open('keyfile.key', 'rb')
key = file.read()  # type byte
file.close()
f = Fernet(key)

# Netdata Configparser
config = configparser.ConfigParser()
config.read('chatconfig.ini')
host = config['CLIENT']['host']
port = int(config['CLIENT']['port'])

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
    print("connection established...")
except socket.error as exec:
    print("connection failure...exception socket.error : %s" % exec)

# Listening and Sending
def receive():
    while True:
        try:
            msg = f.decrypt(client.recv(1024))
            message = f.decrypt(msg)
            print(datetime.datetime.now(), message.decode('utf-8'))
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        msg = '{}: {}'.format(nickname, input(''))
        message = f.encrypt(msg.encode('utf-8'))
        client.send(message)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
