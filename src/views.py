from utils import greeting, get_info_cards, top_transactions
from external_api import get_currency_rates, get_stock_prices
import json
import datetime
import pandas as pd


def opening_file(path_file: str) -> pd.DataFrame:
    """Функция читает файл формата xlsx и возвращает DataFrame"""
    operations_xlsx = pd.read_excel(path_file)
    return operations_xlsx


def views(data: str) -> str:
    """
    принимает строку с датой, возвращает инфо по операциям с начала месяца по текущую дату
    """
    info_file = opening_file("../data/operations.xlsx")  # Открываем файл с операциями
    sort_file = info_file.sort_values(by="Дата платежа", ascending=True)

    date_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
    new_date_obj = date_obj.replace(day=1)

    slice_time_last = date_obj.strftime("%d.%m.%Y")
    slice_time_first = new_date_obj.strftime("%d.%m.%Y")

    slice_file_to_data = sort_file[
        (sort_file["Дата платежа"] >= slice_time_first) & (sort_file["Дата платежа"] <= slice_time_last)
    ]

    with open("../user_settings.json", encoding="utf-8") as f:  # открываем польз. настройки по акциям и валютам
        load_json_info = json.load(f)

    informations_user = dict()

    informations_user["greeting"] = greeting()  # функция приветствия
    informations_user["cards"] = get_info_cards(slice_file_to_data)  # функция получения инфо по параметрам из файла
    informations_user["top_transactions"] = top_transactions(slice_file_to_data)  # вывод топ транзакций по сумме
    informations_user["currency_rates"] = get_currency_rates(load_json_info["user_currencies"])  # функция
    # получения текущего курса валют(валюты из польз. настроек)
    informations_user["stock_prices"] = get_stock_prices(load_json_info["user_stocks"])  # функция получения текущего
    # курса стоимости акций (акции из польз. настроек)

    return json.dumps(informations_user, ensure_ascii=False, indent=4)
