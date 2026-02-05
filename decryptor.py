import os
from cryptography.fernet import Fernet

# --- 1. Find all locked files ---
files_to_decrypt = []
root_dir = "Sandbox"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".locked"):
            files_to_decrypt.append(os.path.join(dirpath, filename))

# --- 2. Load the secret key ---
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()
fernet_tool = Fernet(secret_key)

# --- 3. Decrypt each file ---
for file_path in files_to_decrypt:
    with open(file_path, "rb") as encrypted_file:
        encrypted_content = encrypted_file.read()

    decrypted_content = fernet_tool.decrypt(encrypted_content)

    original_path = file_path.removesuffix(".locked")
    with open(original_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_content)

    os.remove(file_path)

# --- 4. Remove ransom note ---
note_path = os.path.join(root_dir, "NOTE_PLEASE_READ.txt")
if os.path.exists(note_path):
    os.remove(note_path)

print("Decryption complete. All files have been restored.")
