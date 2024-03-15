import os
from collections import defaultdict
import hashlib

def hash_file(file_path):
    """Generate a hash for the given file."""
    hash_obj = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read the file in chunks to avoid memory issues with large files
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def find_duplicate_files(directory):
    """Find duplicate files in the given directory."""
    files_dict = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Get the file name without extension
            file_name = os.path.splitext(file)[0]
            files_dict[file_name].append(file_path)
    return {name: paths for name, paths in files_dict.items() if len(paths) > 1}

def delete_duplicate_files(directory):
    """Delete duplicate files in the given directory."""
    duplicates = find_duplicate_files(directory)
    for name, paths in duplicates.items():
        # Keep the first file and delete the rest
        for path in paths[1:]:
            os.remove(path)
            print(path)

# Specify the directory containing files
directory = "Certificate"
delete_duplicate_files(directory)
