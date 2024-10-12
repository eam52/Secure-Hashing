import hashlib
import os
import magic
from pyfiglet import Figlet
import requests
import sys


## this method calculates the file hash, and return the calculated hash
def hashfile(file_path):
    if len(sys.argv) < 2:
        print("please provide a file name!")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            hash_code = hashlib.sha256(file_data).hexdigest()
            return hash_code
    except FileNotFoundError:
        print("This file doesn\'t exist")
        sys.exit(1) # exits if the file is not found
    except Exception as e:
        print(f"an error has occured: {e}")


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
    print("the hashed file", file_to_hash)
    print(f"the hashed file: {file_to_hash}")
    compared_hash(file, file_to_hash)

if __name__ == "__main__":
    main()
