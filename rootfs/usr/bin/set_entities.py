import requests

# Replace with your Home Assistant URL
api_url = ""

# Replace with your access token
access_token = ""

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# Define the entity data
entity_id = "binary_sensor.model_addon_testing_entity"
entity_state = "testing3"

# Create the entity using the REST API
response = requests.post(
    f"{api_url}/states/{entity_id}", json={"state": entity_state}, headers=headers
)

if response.status_code == 201:
    print(f"Entity created successfully.")
elif response.status_code == 200:
    print("enetiy is being updated")
else:
    print(f"Failed to create entity. Status code: {response.status_code}")
