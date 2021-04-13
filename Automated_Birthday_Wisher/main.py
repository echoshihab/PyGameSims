import smtplib
import datetime as dt
import random
import pandas


##################### Automated Birthday Wisher ######################
now = dt.datetime.now()
current_tuple = (now.month, now.day)

# 2. Check birthdays.csv  to see if today matches a birthday
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 3. there are names in birthday list send letter to each
if current_tuple in birthdays_dict:
    birthday_person = birthdays_dict[current_tuple]
    letter_template = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_template) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"].title())

        print(contents)
        print(birthday_person.email)
# 4. Send the letter generated in step 3 to that person's email address.

    my_email = "fake@email.com"
    password = "fakepassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f"{birthday_person.email}",
                            msg=f"Subject:Happy Birthday\n\n{contents}")

