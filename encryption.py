from cryptography.fernet import Fernet

"""def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
generate_key()"""

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print(encrypted_message)

def decrypt_message(encrypted_message):
    if isinstance(encrypted_message, str):
        encrypted_message=encrypted_message.encode()
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message.decode())

"""if __name__ == "__main__":
    encrypt_message("5999")
    decrypt_message("gAAAAABgKjn9XyB1y8Tu5QewujANCFatCEz1sjqYka3WSnvaSf5IbRjYq1MnKhYTbb6biRQd3EdIx9YJ-PWdnU66ZiXUHPLnCA==")
"""
