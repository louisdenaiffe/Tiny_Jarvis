import csv
import random


def get_random_recipe(recipes):
    if not recipes:
        raise ValueError("recipes.csv is empty!")
    return random.choice(recipes)


def load_recipes():
    try:
        with open("recipes.csv", newline="", encoding="utf-8") as csvfile:
            return list(csv.DictReader(csvfile))
    except FileNotFoundError:
        print("Couldn't find recipes.csv!")
        return []


def format_cooking_sentence(recipe_object):
    return (
        f"Today's recipe is {recipe_object['Title']}."
        f"Ingredients needed: {recipe_object['Ingredients']}."
        f"Recipe: {recipe_object['Recipe']}."
        f"Total preparation and cooking time: {recipe_object['Prep & Cooking Time']}."
    )


# For testing
'''
recipe_object = get_recipe()
print(format_cooking_sentence(recipe_object))
print(recipe_object['Ingredients'])
'''