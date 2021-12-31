##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import smtplib
import datetime 
import random

my_gmail_id = "chungchuong163@gmail.com"
my_password = "anhyeuem12"

#today = (datetime.datetime.now().month, datetime.datetime.now().day)
today = (1,3)

data = pandas.read_csv('birthdays.csv')
birthdays = {(row.month, row.day):row for index, row in data.iterrows()}

if today in birthdays:
    birthday_person = birthdays[today]
    print(birthday_person)
    a = ['letter_1.txt','letter_2.txt','letter_3.txt']
    random_letter = random.choice(a)
    with open(file=f'letter_templates/{random_letter}') as template:
        contents = template.read()
        replace_name = contents.replace('[NAME]', birthday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail_id, password=my_password)
        connection.sendmail(
            from_addr=my_gmail_id,
            to_addrs=birthday_person['email'],
            msg=f"Subject: HPBD\n\n {replace_name}"
        )

           
      