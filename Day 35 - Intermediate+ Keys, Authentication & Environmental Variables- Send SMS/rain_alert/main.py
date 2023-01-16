import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
OWM_API_KEY = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 34.697472,
    "lon": -118.144524,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
hrly_data_slice = data["hourly"][:12]

for hrly_data in hrly_data_slice:
    main_weather_data = hrly_data["weather"][0]
    if main_weather_data["id"] < 700:
        print("Bring Umbrella")
        break
else:
    exit()

client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella ☔",
                     from_='+19047805729',
                     to='+15054928001'
                 )
print(message.status)
