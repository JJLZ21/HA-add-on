import requests
import sys

token = sys.argv[1]

# Define Home Assistant API URL
api_url = "http://192.168.1.106:8123/api"

# Define the entity you want to retrieve data from
entity_id = "sun.sun"

# Make an API request to get the entity state
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
}
response = requests.get(f"{api_url}/states/{entity_id}", headers=headers)

# Check the response and extract the state
if response.status_code == 200:
    data = response.json()
    entity_state = data["state"]
    print(f"Entity State: {entity_state}")
else:
    print(f"Failed to retrieve entity state: {response.status_code}")
