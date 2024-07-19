import pandas as pd
from views import opening_file


def filtering_by_search(search_string: str) -> pd.DataFrame:
    """Фильтруем транзакции по строке поиска"""
    file_operation = opening_file("../data/operations.xlsx")

    search_operations = file_operation.loc[
        (file_operation["Категория"] == search_string.title()) |
        (file_operation["Описание"] == search_string.title())
    ]

    return search_operations
