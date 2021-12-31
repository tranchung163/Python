import smtplib

my_gmail_id = 'chungchuong163@gmail.com'
my_gmail_pass = 'anhyeuem12'
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_gmail_id, password=my_gmail_pass)
#     connection.sendmail(
#         from_addr=my_gmail_id, 
#         to_addrs='le.ma63@yahoo.com', 
#         msg='Subject: Hello\n\nThis is the body of the mail')

import datetime as dt
import random
# now = dt.datetime.now()
# print(now.year)
# print(now.minute)
# print(now.weekday())

# data_of_birth = dt.datetime(year=1998,month=3,day=16)

now_weekday = dt.datetime.now().weekday()
if now_weekday == 1:
    with open(file='quotes.txt') as quotes_file:
        quotes = quotes_file.readlines()
        random_number = random.randint(0, len(quotes))
        random_quote = quotes[random_number]
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_gmail_id, password=my_gmail_pass)
            connection.sendmail(
            from_addr=my_gmail_id, 
            to_addrs='tranchung163@gmail.com', 
            msg=f'{random_quote}'
            )

