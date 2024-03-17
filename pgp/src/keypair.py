"""
file: keypair.py

Generate key pair, sign/verify & encrypt/decrypt messages.

author: logan lee
"""
import gnupg
import os

def generate_keypair(name, email, passphrase, key_length):
    """
    """
    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        name_real=name,
        name_email=email,
        passphrase=passphrase,
        key_length=key_length,
        key_type="RSA",
        subkey_type="RSA",
        subkey_length=2048,
        expire_date=0,
        )
    key = gpg.gen_key(input_data)
    
    # extract public and private keys from the key object
    public_key = str(key)
    private_key = gpg.export_keys(key.fingerprint)

    # return public_key, private_key
    return key


def save_key(key_data, key_name, destination_folder):
    """
    key_data:           the generated key
    key_name:           string of the name you want to give this keypair
    destination_folder: the absolute path of where you want to store your keypair 
    """
    # first create the folder for the new keypair
    destination = f"{destination_folder}/{key_name}"
    try:
        os.mkdir(destination)
        print(f"Successfully created: {destination}")
    except OSError as e:
        print("Failed to create directory {} due to: {}".format(destination, e))
    with open(destination, "w") as file:
        file.write(key_data)

def load_key():
    pass

def sign_message():
    pass

def verify_message():
    pass 

def encrypt_message(message, private_key):
    gpg = gnupg.GPG()
    signed_data = gpg.sign(message, keyid=private_key.fingerprint, detach=True)
    return str(signed_data)

def decrypt_message(encrypted_message, public_key):
    gpg = gnupg.GPG()
    verified = gpg.verify(encrypted_message, key_data=public_key)




    