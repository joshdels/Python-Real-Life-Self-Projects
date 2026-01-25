import hashlib


def compute_file_hash(file_path, algorith="sha256"):
    hash_func = hashlib.new(algorith)

    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

        print(hash_func.hexdigest())
        # return hash_func.hexdigest()


compute_file_hash("test-files/file1.txt")
compute_file_hash("test-files/file111.txt")



# advance
def main():
    file_path = input("Enter the path to the file: ")
    algorithm = input("Enter the hash algorithm (e.g., md5, sha1, sha256): ")
    
    try:
        file_hash = compute_file_hash(file_path, algorithm)
        print(f"The {algorithm} hash of the file is: {file_hash}")
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    except ValueError:
        print(f"Invalid hash algorithm: {algorithm}. Please enter a valid algorithm (e.g., md5, sha1, sha256).")

if __name__ == "__main__":
    main()
    
    
# The hasing starts twith a file path then an algorithm
# most of it is compute_file_hash(filepath, algorith)
#chuch file.read()
#hexdigest()  if feel its easier