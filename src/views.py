from src.utils import greeting, opening_file, get_info_cards, top_transactions


def views(data: str) -> dict:
    informations_user = dict()

    informations_user["greeting"] = greeting()
    informations_user["cards"] = get_info_cards("../data/operations.xlsx")

    return informations_user


if __name__ == "__main__":
    print(views("22"))
