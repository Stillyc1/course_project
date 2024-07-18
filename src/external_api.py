import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()
API_KEY = os.getenv("API_KEY")
URL_CONVERT = os.getenv("URL_CONVERT")

with open("../user_settings.json", encoding="utf-8")as f:
    load_json_info = json.load(f)


def get_exchange_rate():
    url = URL_CONVERT
    headers = {"apikey": API_KEY}

    currency_rates = dict()

    for currency in load_json_info["user_currencies"]:
        params = {
            "amount": 1,
            "from": f"{currency}",
            "to": "RUB",
        }

        responce = requests.get(url, headers=headers, params=params).json()
        currency_rates[f"{currency}"] = responce["info"]["rate"]

    return currency_rates

# def stock_prices():
#     response = requests.get(
#         "https://api.twelvedata.com/time_series?apikey=6e9063e4e2e54b9081d89aa412b9474a&interval=1min&format=JSON&timezone=Europe/Moscow&type=stock&symbol=AAPL, AMZN, MSFT, TSLA&country=Russian Federation")
#
#     return response.json()
#
# print(stock_prices())
