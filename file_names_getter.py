import os

def get_filenames(folder_path):

  filenames = []
  for filename in os.listdir(folder_path):
    # Check if it's a file (not a directory)
    if os.path.isfile(os.path.join(folder_path, filename)):
      filenames.append(filename)
  return filenames

# Example usage
folder_path = "OCR"  # Replace with your actual folder path
filenames = get_filenames(folder_path)

# Print the list of filenames
# print("Files in", folder_path, ":")
# for filename in filenames:
#   print(filename)
print(filenames)