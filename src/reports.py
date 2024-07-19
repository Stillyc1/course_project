import pandas as pd
import datetime


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: str = None) -> pd.DataFrame:
    """
    Функция принимает на вход:
    датафрейм с транзакциями,
    название категории,
    опциональную дату.
    Если дата не передана, то берется текущая дата.

    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).
    """
    sort_transactions = transactions.sort_values(by="Дата платежа", ascending=False)

    if date is None:
        date = datetime.datetime.now().strftime("%d.%m.%Y")

    date_split = date.split(".")
    three_months_ago = int(date_split[1]) - 3

    date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
    date_three_month_ago = date_obj.replace(month=three_months_ago)

    slice_time_first = date_three_month_ago.strftime("%d.%m.%Y")

    file_to_data = sort_transactions[
        (sort_transactions["Дата платежа"] >= slice_time_first) &
        (sort_transactions["Дата платежа"] <= date)
    ]

    sort_by_category = file_to_data[(file_to_data["Категория"] == category)]

    return pd.DataFrame(sort_by_category)
