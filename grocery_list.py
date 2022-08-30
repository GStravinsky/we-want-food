from collections import defaultdict
from domain import Recipe


def produce_grocery_list(data, meal_indices: list[str]) -> str:

    grocery_dict = merge_produce_lists(data, meal_indices)
    return parse_grocery_list(grocery_dict)

def merge_produce_lists(data, meal_indices: list[str]) -> dict :

    recipes = [Recipe(i, data[i]["name"], data[i]["groceries"]) for i in meal_indices]

    grocery_list = defaultdict(list)

    for d in recipes:
        groceries = d.groceries
        for g in groceries.keys():
            if g in grocery_list:
                grocery_list[g].append(groceries[g])
            else:
                grocery_list[g] = [groceries[g]]


    return grocery_list

def parse_grocery_list(grocery_dict: dict) -> str:
    parsed_groceries = ""
    for ingredient, quantity in grocery_dict.items():
        parsed_groceries = parsed_groceries + "\n" + "--{}: {}".format(ingredient, quantity)
    return parsed_groceries

