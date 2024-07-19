import datetime
import pandas as pd


def opening_file(path_file: str) -> pd.DataFrame:
    """Функция читает файл формата xlsx и возвращает DataFrame"""
    operations_xlsx = pd.read_excel(path_file)
    return operations_xlsx


def greeting() -> str:
    """ возвращает приветствие, в зависимости от времени"""

    time = datetime.datetime.now().hour
    if time in range(0, 7):
        return f"Доброй ночи"
    elif time in range(6, 13):
        return f"Доброе утро"
    if time in range(12, 19):
        return f"Добрый день"
    else:
        return f"Добрый вечер"


def get_info_cards(operations_xlsx: pd.DataFrame) -> list[dict]:
    """принимает DataFrame и сортирует по параметрам"""
    group_card = operations_xlsx.groupby("Номер карты", as_index=False)

    total_sum_cashback = group_card.sum().loc[:, ["Номер карты", "Сумма платежа", "Кэшбэк"]]

    return total_sum_cashback.to_dict(orient="records")


def top_transactions(operations_xlsx: pd.DataFrame) -> list[dict]:
    """принимает DataFrame и выводит топ 5 транзакций"""
    top_5_operation = operations_xlsx.sort_values(by="Сумма платежа").head()
    information = top_5_operation.loc[:, ["Дата платежа", "Сумма платежа", "Категория", "Описание"]]

    return information.to_dict(orient="records")


if __name__ == "__main__":
    file = opening_file("../data/test.xlsx")
    x = opening_file("../data/operations.xlsx")
    # print(get_info_cards(x))
    # print(top_transactions(x))
