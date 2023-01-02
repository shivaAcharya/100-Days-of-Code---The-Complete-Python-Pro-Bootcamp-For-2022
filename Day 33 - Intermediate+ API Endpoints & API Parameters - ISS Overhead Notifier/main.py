import requests
from datetime import datetime


MY_LAT = 34.697472
MY_LONG = -118.144524

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# print(latitude, longitude)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split('T')[1][:2]
sunset = data["sunset"].split('T')[1][:2]

print(sunrise, sunset)

time_now = datetime.now()

print(time_now.hour)
