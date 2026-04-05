from typing import Optional

def unite(list_of_dict: list[dict], list_of_int: list[int]) -> list[dict]:
    if len(list_of_int) != len(list_of_dict):
        raise ValueError("Размеры не совпали")

    result = []
    for i in range(len(list_of_int)):
        prom = {"order_id": list_of_int[i]}
        result.append(prom | list_of_dict[i])
    return result


def date_correct(value: str) -> str:
    if len(value) == 10:
        return value
    year, month, day = value.split("-")
    if len(month) != 2:
        month = "0" + month
    if len(day) != 2:
        day = "0" + day
    return f"{year}-{month}-{day}"


def unite_for_return(list_of_dict: list[Optional[dict]], list_of_int: list[int]) -> list[dict]:
    if len(list_of_int) != len(list_of_dict):
        raise ValueError("Размеры не совпали")
    result = []
    for i in range(len(list_of_int)):
        if list_of_dict[i] is None:
            continue
        prom = {"order_id": list_of_int[i]}
        result.append(prom | list_of_dict[i])
    return result


def find_last_date(month: int, year: int) -> dict[str, int]:
    if month > 1:
        last_m = month - 1
        return {'month': last_m, 'year': year}
    last_m = 12
    last_y = year - 1
    return {'month': last_m, 'year': last_y}









