from src.keypair import generate_keypair, encrypt_message

key_1 = generate_keypair("Logan Lee", "ldl6147@gmail.com", "testpass", 2048)

public_key_1 = str(key_1)

encrypted_message = encrypt_message("I endorse this message.", key_1)

print(encrypted_message)

descrypted_message = decrypt_message()