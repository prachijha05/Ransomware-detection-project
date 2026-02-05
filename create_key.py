from cryptography.fernet import Fernet

# Generate a new, random encryption key
key = Fernet.generate_key()

# Save this key to a file named 'thekey.key'
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

print("Successfully created 'thekey.key'. Keep this file safe!")