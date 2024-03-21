import base64
import requests
import json
import pyperclip


def encode_and_send_file(file_path, api_url, headers={}, data={}):
  """
  This function reads a txt file, encodes it in base64, and sends it in the body of a POST request to the specified API.

  Args:
      file_path (str): Path to the txt file.
      api_url (str): URL of the API endpoint.
      headers (dict, optional): Additional headers for the request. Defaults to {}.
      data (dict, optional): Additional data to send in the request body. Defaults to {}.

  Returns:
      requests.Response: The response object from the API call.
  """
  # Read the file content
  with open(file_path, 'rb') as f:
    file_content = f.read()

  # Encode the content in base64
  encoded_content = base64.b64encode(file_content).decode('utf-8')

  # Update data dictionary with encoded content (assuming key is "file")
  data.update({"file": encoded_content})

  # Send POST request with data
  response = requests.post(api_url, headers=headers, json=data)

  # Return the response object
  return response

# Example usage
file_paths = ['15 -  måltid.txt', '15 - måltid 7eleven.txt', '15 - måltid 7eleven2.txt', '15 - måltid arctic.txt', '15 - måltid cirkle k 2.txt', '15 - måltid cirkle k 3.txt', '15 - måltid cirkle k.txt', '15 - måltid graffi.txt', '15 - måltid leksvik.txt', '15 - måltid matologi.txt', '15 - måltid olearys.txt', '15 - måltid partnersamling.txt', '15 - måltid på tog.txt', '15 - måltid på tog2.txt', '15 - måltid rosenborg bakeri.txt', '15 - måltid starbucks.txt', '15 - måltid strawberry.txt', '15 - måltid trondheim thaimat.txt', '15 - måltid xy.txt', '16 - overnatting.txt', '16 - overnatting2.txt', '16 - overnatting3.txt', '16 - overnatting4.txt', '16 - overnatting5.txt', '16 - overnatting6.txt', '17 - parkering apcoa.txt', '17 - parkering easy park.txt', '17 - parkering one park.txt', '17 - parkering one park2.txt', '17 - parkering timepark.txt', '17 - parkering timepark2.txt', '19 - togbillett vy2.txt', '19 - togbillett vy3.txt', '19 - togtillett vy.txt', '7 - rekvisita.txt', '7 - rekvisita2.txt']

api_url = "http://127.0.0.1:5000/ai-models//document/analyze"
headers = {"companyId": "14",
           "userId" : "250",
           "nodeId" : "Dummy",
           "documentType":"receipt"}  # Add any required headers
# # Add any additional data for the request
file_number = 99
index_number = file_number-63
current_file_path = file_paths[index_number]
print(f"FILE_NUMBER:{file_number}")
pyperclip.copy(current_file_path)
print(current_file_path)
formatted_current_file_path = f"OCR/{current_file_path}"
response = encode_and_send_file(formatted_current_file_path , api_url, headers)

# Check the response status code
if response.status_code == 200:
  print("File uploaded successfully!")
  print(json.dumps(response.json(), indent=4))
else:
  print("Error uploading file. Status code:", response.status_code)
  print(response.text)  # Print the error message from the response

