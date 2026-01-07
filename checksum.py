import os
import hashlib


def folder_checksum(folder_path):
    sha = hashlib.sha256()


    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)


            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha.update(chunk)


    return sha.hexdigest()


if __name__ == "__main__":
    folder_path = r"D:\CODES\Project"
   
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
    else:
        checksum = folder_checksum(folder_path)
        print("\nChecksum for folder:")
        print(checksum)
