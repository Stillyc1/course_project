import datetime
import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_CURRENCY = os.getenv("API_KEY_CURRENCY")


with open("../user_settings.json", encoding="utf-8")as f:  # открывает пользовательские настройки по акциям и валютам
    load_json_info = json.load(f)

# time_now = datetime.datetime.now()
# now_begin = time_now + datetime.timedelta(hours=-time_now.hour, minutes=-time_now.minute, seconds=-time_now.second)
# # Получаем дату с начала текущего дня, для корректного получения стоимости акций
# TIME_NOW_BEGIN = now_begin.strftime("%Y-%m-%d %H:%M:%S")


def get_currency_rates(currencies: list) -> list[dict]:
    """
    Функция принимает список валют из пользовательских настроек
    делает запрос и возвращает список со стоимостью каждой валюты по курсу на сегодня
    """
    rates = []
    for currency in currencies:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY_CURRENCY}/latest/{currency}")
        data = response.json()
        rates.append({"currency": currency, "rate": data["conversion_rates"]["RUB"]})

    return rates


def get_stock_prices(stocks: list) -> list[dict]:
    """
    Принимает пользовательские настройки (выбор акций) и возвращает стоимость акций
    в $ на начало текущего дня
    """
    prices = []

    for stock in stocks:
        params = {
            "apikey": f"{API_KEY}",
            "interval": "1day",
            "format": "JSON",
            "type": "stock",
            "symbol": f"{stock}",
            "outputsize": 1,
            "timezone": "Europe/Moscow"

        }

        response = requests.get("https://api.twelvedata.com/time_series", params=params)

        data = response.json()
        prices.append({"stock": stock, "price": data["values"][0]["close"]})

    return prices


# print(get_stock_prices(load_json_info["user_stocks"]))
