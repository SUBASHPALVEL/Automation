import os

def list_files_without_extension(directory_path):
  entries = os.scandir(directory_path)

  # Extract filenames without extensions
  filenames_no_extension = [os.path.splitext(entry.name)[0] for entry in entries if entry.is_file()]

  return filenames_no_extension


pdf_files_without_extension = list_files_without_extension('Data/PDF')
print(len(set(pdf_files_without_extension)))
print(len(pdf_files_without_extension))
text_files_without_extension = list_files_without_extension('OCR')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(text_files_without_extension)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(len(set(text_files_without_extension)))


def find_unique_elements(list1, list2):
  # Create a set from the first list
  set1 = set(list1)

  # Create a set from the second list
  set2 = set(list2)

  # Find elements that are in set1 but not in set2
  unique_from_list1 = set1 - set2

  # Find elements that are in set2 but not in set1
  unique_from_list2 = set2 - set1

  # Print the unique elements from list1
  print("Elements present in list1 but not in list2:")
  for element in unique_from_list1:
    print(element)

  # Print the unique elements from list2
  print("\nElements present in list2 but not in list1:")
  for element in unique_from_list2:
    print(element)


find_unique_elements(pdf_files_without_extension, text_files_without_extension)


def find_duplicates(my_list):
  """
  This function takes a list as input and returns a list containing the duplicate elements.

  Args:
      my_list (list): The list to check for duplicates.

  Returns:
      list: A list of duplicate elements.
  """
  # Use a set to efficiently identify unique elements
  seen = set()
  duplicates = []
  for item in my_list:
    if item in seen:
      duplicates.append(item)
    else:
      seen.add(item)
  return duplicates

# Find the duplicates
duplicates = find_duplicates(pdf_files_without_extension)

print(duplicates)

