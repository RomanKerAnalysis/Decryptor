# MD5 : d7a7df59b8979b97d547972b307a4740
# Demo version script
# Script by Romanker (twitter:@Roman_ker)

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Key, IV
key = b'\x64\x00\x37\x00\x61\x00\x30\x00\x31\x00\x73\x00\x39\x00\x75\x00'
iv = b'\x64\x00\x37\x00\x61\x00\x30\x00\x31\x00\x73\x00\x39\x00\x75\x00'

# AES Decrypt Func
def decrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            ciphertext = file.read()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f'Decrypted: {file_path}')

        # Check if a file with the same name exists
        decrypted_file_path = os.path.splitext(file_path)[0]
        while os.path.exists(decrypted_file_path):
            decrypted_file_path += '_copy'
        os.rename(file_path, decrypted_file_path)

        print(f'Renamed to: {original_file_path}')

    except Exception as e:
        print(f'Error decrypting {file_path}: {e}')

# Recursive Func
def decrypt_files_in_directory(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.keygroup777tg'):
                file_path = os.path.join(foldername, filename)
                decrypt_file(file_path)

# Set start directory
start_directory = 'C:\\'

# Lets go
decrypt_files_in_directory(start_directory)
