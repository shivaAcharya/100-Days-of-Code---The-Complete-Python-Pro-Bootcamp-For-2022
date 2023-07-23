import requests
from datetime import datetime

USERNAME = "shivacharya"
TOKEN = "fsadjhfadskjfa3839ks"
GRAPH_ID = "graph1"

pixela_endpoint  = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create Username
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?"),
}

# Post a pixel
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/20230709"

updated_pixel_data = {
    "quantity": "5"
}

# Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=updated_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixel_endpoint}/20230709"

# Delete a pixel
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
