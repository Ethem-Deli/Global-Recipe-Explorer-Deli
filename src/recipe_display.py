import requests
import os

API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_recipe_details(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=true&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nutrition = {}
    for nutrient in data.get("nutrition", {}).get("nutrients", []):
        nutrition[nutrient["name"]] = f"{nutrient['amount']} {nutrient['unit']}"
    data["nutrition"] = nutrition
    return data
