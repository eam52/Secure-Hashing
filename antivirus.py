# importing hashlib for getting sha256() hash function
import hashlib
import os
import magic
from pyfiglet import Figlet
import requests
import sys


# the display_ASCII function will use pyfiglet to create an ASCII
# Messager for out antivirus script

def ascii_print():
    fig = Figlet(font= "slant")
    print(fig.renderText("AntiVirus"))

#The file_hash function will calculate the SHA-256 hash of given file
# using the hashlib library

def hashfile(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        hash_code = hashlib.sha256(file_data).hexdigest()
    return hash_code


def main():
    file = "phishing.docx"
    file_to_hash = hashfile(file)
    print(f"the hashed file: {file_to_hash}")

    ascii_print()

if __name__ == "__main__":
    main()