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

## this method calculates the file hash, and return the calculated hash
def hashfile(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            hash_code = hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        print("This file doesn\'t exist")
    return hash_code

## this method compares the calculated hash with the stored hash to
## verfiy integrity and any changes made into the document on file

def compared_hash(file_path, stored_hash):
    current_hash = hashfile(file_path)
    
    if current_hash == stored_hash:
        print("File integrity is successful!" )
    else:
        print(f"Integrity check has failed!!! {current_hash} does not equal to {stored_hash}")


def main():
    file = "phishing.docx"
    file_to_hash = hashfile(file)
    print(f"the hashed file: {file_to_hash}")
    compared_hash(file, file_to_hash)


if __name__ == "__main__":
    main()