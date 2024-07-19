from utils import greeting, opening_file, get_info_cards, top_transactions
from external_api import get_currency_rates, get_stock_prices
import json
import datetime
import pandas as pd


def views(data: str) -> str:
    info_file = opening_file("../data/operations.xlsx")  # Открываем файл с операциями
    # info_file.sort_values(by="Дата платежа")

    # date_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
    # new_date_obj = date_obj.replace(day=1)
    # slice_time_last = date_obj.strftime("%d.%m.%Y")
    # slice_time_first = new_date_obj.strftime("%d.%m.%Y")
    #
    # slice_file_to_data = info_file[info_file["Дата платежа"]]

    with open("../user_settings.json", encoding="utf-8") as f:  # открываем польз. настройки по акциям и валютам
        load_json_info = json.load(f)

    informations_user = dict()

    informations_user["greeting"] = greeting()  # функция приветствия
    informations_user["cards"] = get_info_cards(info_file)  # функция получения инфо по параметрам из файла
    informations_user["top_transactions"] = top_transactions(info_file)  # функция вывода топ транзакций по сумме
    informations_user["currency_rates"] = get_currency_rates(load_json_info["user_currencies"])  # функция
    # получения текущего курса валют(валюты из польз. настроек)
    informations_user["stock_prices"] = get_stock_prices(load_json_info["user_stocks"])  # функция получения текущего
    # курса стоимости акций (акции из польз. настроек)

    return json.dumps(informations_user, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print(views("22.12.2021"))

# date_obj = datetime.datetime.strptime("10.12.2021", "%d.%m.%Y")
# new_date_obj = date_obj.replace(day=1)
# slice_time_last = date_obj.strftime("%d.%m.%Y %H:%M:%S")
#
# slice_time_first = new_date_obj.strftime("%d.%m.%Y %H:%M:%S")
#
#
# info_file = opening_file("../data/operations.xlsx")
# i = info_file.set_index("Дата операции")
# x = i.loc[f"{slice_time_first}":f"{slice_time_last}"]

# print(i.head(15))
# print(slice_time_first)
# print(slice_time_last)
