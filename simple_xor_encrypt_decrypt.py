def xor_encrypt_decrypt(key, message):
    # Convert the key to bytes
    key = key.encode()

    # XOR encryption: repeat the key if it's shorter than the message
    encrypted_message = ''.join(chr(ord(m) ^ key[i % len(key)]) for i, m in enumerate(message))
    return encrypted_message

def main():
    # Ask for the plaintext message
    plaintext = input("Type a sentence to encrypt: ")

    # Ask for a simple text key
    key = input("Enter a simple text key: ")

    # Encrypt the message
    encrypted_message = xor_encrypt_decrypt(key, plaintext)

    # Display the encrypted message
    print("Encrypted message:", encrypted_message)

    # Decrypting back using the same function
    decrypted_message = xor_encrypt_decrypt(key, encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
