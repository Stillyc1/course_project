from src.services import filtering_by_search

import pandas as pd


def test_filtering_by_search():
    file_operation = pd.read_excel("../data/test.xlsx")
    assert type(filtering_by_search("Фастфуд")) == type(file_operation)
