import requests

# Replace with your Home Assistant URL
api_url = "http://192.168.1.106:8123/api"

# Replace with your access token
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyYmYxMjUzMWJlMDM0ODdlYjA5MzU3MjRhMDAxYzBiOCIsImlhdCI6MTY5NjkxMzMzNCwiZXhwIjoyMDEyMjczMzM0fQ.EmJ1qh1RyjrtSr9cE1o8psdmVCQuT_dUkl4K-A5GIzI"

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
