import requests
import sys
import datetime

# Define the input you want to retrieve data from
token = sys.argv[1]

entity_str_list = sys.argv[2]
entity_list = entity_str_list.split("\n")

out_entity_str_list = sys.argv[3]
out_entity_list = out_entity_str_list.split("\n")


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

for entity in entity_list:
    response = requests.get(f"{api_url}/states/{entity}", headers=headers)
    print(response)
    # Check the response and extract the state
    if response.status_code == 200:
        data = response.json()
        entity_state = data["state"]
        features.append(entity_state)
        # print(f"Entity State: {entity_state}")
    else:
        features.append(response.status_code)
        # print(f"Failed to retrieve entity state: {response.status_code}")


features.append(month)
features.append(day)
features.append(minute)
features.append(hour)
features.append(second)
features.append(day_in_week)
features.append(time_in_day)

print(features)
print(out_entity_list)

# prediction_api_url = "http://192.168.1.109:8080"
# prediction_headers = {
#     "Content-Type": "application/json",
# }
# data = features
# array_str = ",".join(map(str, data))
# payload = {"entities": array_str}
# prediction = requests.get(
#     f"{prediction_api_url}/predict", params=payload, headers=prediction_headers
# )

# for p in prediction:
#     print(p)
