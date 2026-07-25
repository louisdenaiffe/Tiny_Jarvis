import csv
import random


def get_recipe():
    list = []
    with open("recipes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=("Title", "Ingredients", "Recipe", "Prep & Cooking Time"))
        for row in reader:
            list.append(row)  # each JSON object = un plat. So it's a list with all the plat JSON objects, easily accessible
    if not list:
        raise ValueError("recipes.csv is empty!")
    return random.choice(list)


def format_cooking_sentence(recipe_object):
    return (
        f"{recipe_object['Title']}."
        f"Ingredients needed: {recipe_object['Ingredients']}."
        f"Recipe: {recipe_object['Recipe']}."
        f"Finally, the preparation and cooking time this recipe will take: {recipe_object['Prep & Cooking Time']}."
    )

# For testing
'''
recipe_object = get_recipe()
print(format_cooking_sentence(recipe_object))
print(recipe_object['Ingredients'])
'''