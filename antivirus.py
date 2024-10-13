import hashlib
import os
import magic
from pyfiglet import Figlet
import requests
import sys


## This method calculates the file hash, and return the calculated hash.
## raises an Error if the file is not found or if other Erro occurs.
def hashfile(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            hash_code = hashlib.sha256()
        return hash_code.hexdigest()      
    except FileNotFoundError:
        print("This file doesn\'t exist")
        sys.exit(1)
    except Exception as e:
        print(f"an error has occured: {e}")


## this method compares the calculated hash with the stored hash to
## verfiy integrity and any changes made into the document on file
def compared_hash(file_path, stored_hash):
    current_hash = hashfile(file_path)
    if current_hash == stored_hash:
        print("File integrity is successfull!" )
    else:
        print(f"Integrity check has failed!!! {current_hash} does not equal to {stored_hash}")


## This method check for file types and raises an Error if the file type is not supported.
def file_validation(file_path):
    get_file_type = magic.from_file(file_path, mime=True)
    
    accepted_file_types = {
        "documents": [
            "application/pdf",
            "application/msword",
            "application/vnd.ms-excel",
            "text/plain",
            "text/csv",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ],
        "scripts": [
            "text/x-python",
            "application/javascript",
            "text/html",
            "text/x-shellscript",
        ]
    }
    all_accepted_file_types = [file_type for types in accepted_file_types.values() for file_type in types]

    if get_file_type not in all_accepted_file_types:
        print(f"Enter accepted file type please: {all_accepted_file_types}")
        raise Exception("did not enter valid file type")
    else:
        return get_file_type


def main():
    if len(sys.argv) < 2:
        print("please provide a file name!")
        sys.exit(1)
    file_path = sys.argv[1]
    file_to_hash = hashfile(file_path)
    print("the hashed file", file_to_hash)
    print(f"the hashed file: {file_to_hash}")
    compared_hash(file_path, file_to_hash)

    print(file_validation(file_path))


if __name__ == "__main__":
    main()
