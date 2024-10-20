import hashlib
import sys
import magic

class Hashing:
    def __init__(self, file_path, sha_algorithm):
        self.file_path = file_path
        self.sha_algorithm = sha_algorithm
        self.hash_function = {
            'sha256': hashlib.sha256,
            'sha1': hashlib.sha1,
            'sha224': hashlib.sha224,
            'sha384': hashlib.sha384,
            'sha512': hashlib.sha512
        }
        self.accepted_file_types = {
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

    
    def hashfile(self):
        try:
            with open(self.file_path, 'rb') as file:
                file_data = file.read()

            if self.sha_algorithm not in self.hash_function:
                raise ValueError(f"You entered an unsupported SHA algorithm: {self.sha_algorithm}")

            hash_code = self.hash_function[self.sha_algorithm]()
            hash_code.update(file_data)  # Corrected variable name
            return hash_code.hexdigest() 

        except FileNotFoundError:
            print("This file doesn't exist")
            sys.exit(1)
        except Exception as e:
            print(f"An error has occurred: {e}")
            sys.exit(1)

    
    def compare_hash(self, stored_hash):
        current_hash = self.hashfile()
        if current_hash == stored_hash:
            print("File integrity is successfull!")
        else:
            print(f"Integrity check has failed!!! {current_hash} does not equal to {stored_hash}")

    
    def file_validation(self):
        get_file_type = magic.from_file(self.file_path, mime=True)
        all_accepted_file_types = [file_type for types in self.accepted_file_types.values() for file_type in types]
        if get_file_type not in all_accepted_file_types:  
            print(f"Enter an accepted file type please: {all_accepted_file_types}")
            raise Exception("Did not enter valid file type")
        else:
            return get_file_type

def main():
    if len(sys.argv) < 3:
        print("Please provide a file name and hash algorithm!")
        sys.exit(1)

    file_path = sys.argv[1]
    hash_algorithm = sys.argv[2].lower()
    

    hasher = Hashing(file_path, hash_algorithm)
    file_to_hash = hasher.hashfile()
    print(f"The hashed file: {file_to_hash}")

    # You need to provide the stored hash for comparison
    stored_hash = file_to_hash
    file_to_compare = hasher.compare_hash(stored_hash)


if __name__ == "__main__":
    main()

