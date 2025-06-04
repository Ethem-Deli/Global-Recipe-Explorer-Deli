import random
from src.search import search_recipes

def generate_weekly_recipes(preference=None):
    recipes = search_recipes(preference or "dinner")
    return random.sample(recipes, min(7, len(recipes)))

from src.search import search_recipes

def generate_weekly_recipes():
    suggestions = ['chicken', 'pasta', 'salad', 'rice', 'soup', 'fish', 'vegetarian']
    weekly = []
    for keyword in suggestions:
        recipes = search_recipes(keyword)
        if recipes:
            weekly.append(recipes[0])
    return weekly
