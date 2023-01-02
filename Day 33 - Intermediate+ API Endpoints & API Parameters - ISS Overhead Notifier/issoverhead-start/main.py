import requests
from datetime import datetime
import smtplib
from config import email, password
import time

MY_LAT = 34.697472
MY_LONG = -118.144524
MY_EMAIL = email
MY_PW = password


# Your position is within +5 or -5 degrees of the ISS position.

def is_iss_at_my_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return sunset <= time_now.hour or time_now.hour <= sunrise

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if is_iss_at_my_location() and is_night():
        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PW)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="cva.acharya8@gmail.com",
                                msg="Subject:Look for ISS Overhead\n\n Look in the sky to spot ISS")




