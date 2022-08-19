import json
import random
from domain import Recipe


def give_meals(data_json, n) -> list[Recipe]:
    with open(data_json) as f:
        data = json.load(f)

    meal_indices = random.sample(list(data.keys()), k=n)

    recipes = [Recipe(i, data[i]["name"], data[i]["groceries"]) for i in meal_indices]

    return recipes
