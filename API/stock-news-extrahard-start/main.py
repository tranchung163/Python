import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "GS98ON27ESM45KVC"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "380192b6b29e4d4fb2b5de2c106d4024"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'AC4376f796864ec5682d81818f1c47ed90'
auth_token = '07f084166cc29578f76bab1b6563275b'
client = Client(account_sid, auth_token)

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputside": "full",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, stock_parameter)
stock_data = stock_response.json()['Time Series (Daily)']
data_list =[value for (key, value) in stock_data.items()]

yesterday_price = float(data_list[0]['4. close'])
day_before_yesterday = float(data_list[1]['4. close'])

price_change = float(day_before_yesterday - yesterday_price)*100/yesterday_price

news_response = NewsApiClient(api_key=NEWS_API_KEY)
all_articles = news_response.get_everything(q=COMPANY_NAME,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-11-01',
                                      to='2021-11-24',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

first_news_title = all_articles['articles'][-1]['title']
second_news_title = all_articles['articles'][-2]['title']
third_news_title = all_articles['articles'][-3]['title']

price_change = round(price_change, 3)

if price_change > 0:
    message = client.messages \
                .create(
                     body=f"\n\n   TSLA increased: {price_change}% \n\n   {first_news_title}\n\n   {second_news_title}\n\n   {third_news_title}",
                     from_='+14242288723',
                     to='+17144586728'
                 )
else:
    message = client.messages \
                .create(
                     body=f"\n\n   TSLA decreased: {price_change}% \n\n   {first_news_title}\n\n   {second_news_title}\n\n   {third_news_title}",
                     from_='+14242288723',
                     to='+17144586728'
                )


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

