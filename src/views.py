from utils import greeting, opening_file, get_info_cards, top_transactions
from external_api import get_exchange_rate
import json


def views(data: str) -> str:
    info_file = opening_file("../data/operations.xlsx")

    informations_user = dict()

    informations_user["greeting"] = greeting()
    informations_user["cards"] = get_info_cards(info_file)
    informations_user["top_transactions"] = top_transactions(info_file)

    exchange_rate = [
        {
            "currency": "",
            "rate": 0
        },
        {
            "currency": "",
            "rate": 0
        }
    ]

    for key, value in get_exchange_rate().items():
        exchange_rate[0]["currency"] = key


    informations_user["currency_rates"] = exchange_rate

    return json.dumps(informations_user, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print(views("22"))
