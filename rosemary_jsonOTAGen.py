import json
import os
import secrets

# Configurable variables
maintainer_name = "Ido"
maintainer_github_username = "xyzuniverse"
device_name = "rosemary"
version = "thirteen"

# Get the user input for the filename
filename = input("Enter the filename: ")

# Read the build date from the file
with open('out/build_date.txt', 'r') as file:
    build_date = int(file.read().strip())

# Generate a random ID string
id_length = 32
id = secrets.token_hex(id_length)

# Get the size of the file in bytes
file_path = f"out/target/product/{device_name}/{filename}"
size = os.path.getsize(file_path)

# Generate the URL
url = f"https://sourceforge.net/projects/rthelolchexbuilds/files/rosemary/pixelos-thirteen/{filename}"

# Read the hash from the file
hash_file_path_sha256 = f"{file_path}.sha256sum"
hash_file_path_md5 = f"{file_path}.md5sum"

if os.path.exists(hash_file_path_sha256):
    hash_file_path = hash_file_path_sha256
elif os.path.exists(hash_file_path_md5):
    hash_file_path = hash_file_path_md5
else:
    print("Hash file not found!")
    exit(1)

with open(hash_file_path, 'r') as hash_file:
    file_hash = hash_file.readline().split()[0]

data = {
    "error": False,
    "version": version,
    "filename": filename,
    "datetime": build_date,
    "size": size,
    "url": url,
    "github_releases_url": "PLACEHOLDER",
    "fastboot_package_url": "PLACEHOLDER",
    "filehash": file_hash,
    "id": id,
    "maintainers": [
        {
            "main_maintainer": True,
            "github_username": maintainer_github_username,
            "name": maintainer_name
        }
    ],
    "donate_url": "PLACEHOLDER",
    "website_url": "https://pixelos.net/",
    "news_url": "https://blog.pixelos.net/",
    "forum_url": "PLACEHOLDER"
}

json_data = json.dumps(data, indent=4)
print(json_data)
