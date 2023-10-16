import requests
import sys
import datetime

token = sys.argv[1]
# Define the entity you want to retrieve data from
entity_str_list = sys.argv[2]
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyYmYxMjUzMWJlMDM0ODdlYjA5MzU3MjRhMDAxYzBiOCIsImlhdCI6MTY5NjkxMzMzNCwiZXhwIjoyMDEyMjczMzM0fQ.EmJ1qh1RyjrtSr9cE1o8psdmVCQuT_dUkl4K-A5GIzI"
entity_list = entity_str_list.split("\n")
print(type(entity_list))
print(entity_list)
# Define Home Assistant API URL
api_url = "http://192.168.1.106:8123/api"


# Make an API request to get the entity state
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}
features = []


def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 0  # 'Morning'
    elif 12 <= hour < 17:
        return 1  # 'Afternoon'
    elif 17 <= hour < 21:
        return 2  # 'Evening'
    else:
        return 3  # 'Night'


now = datetime.datetime.now()
month = now.month
day = now.day
minute = now.minute
hour = now.hour
second = now.second
time_in_day = categorize_time_of_day(hour)
day_in_week = datetime.datetime.today().weekday()

for entity in entity_str_list:
    response = requests.get(f"{api_url}/states/{entity}", headers=headers)

    # Check the response and extract the state
    if response.status_code == 200:
        data = response.json()
        entity_state = data["state"]
        features.append(entity_state)
        # print(f"Entity State: {entity_state}")
    else:
        features.append(entity)
        # print(f"Failed to retrieve entity state: {response.status_code}")


features.append(month)
features.append(day)
features.append(minute)
features.append(hour)
features.append(second)
features.append(day_in_week)
features.append(time_in_day)

for f in features:
    print(f"Entity State: {f}")
