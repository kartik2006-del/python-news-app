import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv('NEWS_API_KEY')

print('welcome to news centre '.center(120).title())

query = input("What type of news you want: ")
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={API_KEY}"

r = requests.get(url)

print("Status Code:", r.status_code)   # check HTTP response
print("Raw Response:", r.text)         # check API response

news = json.loads(r.text)

if "articles" in news:
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("-"*40)
else:
    print("Error in response:", news)