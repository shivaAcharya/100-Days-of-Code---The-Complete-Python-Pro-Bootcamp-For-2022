import datetime as dt
import random
from collections import defaultdict
import pandas as pd
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
today = dt.datetime.now().day
month = dt.datetime.now().month

bd_dict = {(data_row["month"], data_row["day"]) : data_row for _, data_row in df.iterrows()}

# print(bd_dict)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
if (month, today) in bd_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        msg = letter.read().replace('[NAME]', bd_dict[(month, today)]["name"])  # Assuming only one person born on a day

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "your_email@gmail.com"
my_pw = "Your_password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pw)
    connection.sendmail(from_addr=my_email,
                        to_addrs=bd_dict[(month, today)]["email"],
                        msg=f"Subject:Birthday Wish\n\n{msg}")

