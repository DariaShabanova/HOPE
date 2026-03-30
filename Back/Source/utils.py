def unite(list_of_dict: list[dict], list_of_int: list[int]) -> list[dict]:
    if len(list_of_int) != len(list_of_dict):
        raise ValueError("Размеры не совпали")

    result = []
    for i in range(len(list_of_int)):
        prom = {"order_id": list_of_int[i]}
        result.append(prom | list_of_dict[i])
    return result






