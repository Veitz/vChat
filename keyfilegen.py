from cryptography.fernet import Fernet

def generate_key():
    """generate a key"""
    key = Fernet.generate_key()
    print(key)
    file = open('keyfile.key', 'wb')
    file.write(key) #type byte
    file.close()
generate_key()
