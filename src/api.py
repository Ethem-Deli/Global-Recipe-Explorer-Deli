import requests

# SPOONACULAR
SPOONACULAR_API_KEY = 'your_spoonacular_api_key'
SPOONACULAR_BASE_URL = 'https://api.spoonacular.com/recipes/'

# REST COUNTRIES
COUNTRIES_BASE_URL = 'https://restcountries.com/v3.1/name/'

def fetch_recipes(query):
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'query': query,
        'number': 10
    }
    response = requests.get(SPOONACULAR_BASE_URL + 'complexSearch', params=params)
    return response.json()

def fetch_recipe_details(recipe_id):
    params = {'apiKey': SPOONACULAR_API_KEY}
    response = requests.get(f"{SPOONACULAR_BASE_URL}{recipe_id}/information", params=params)
    return response.json()

def fetch_country_info(country_name):
    response = requests.get(f"{COUNTRIES_BASE_URL}{country_name}")
    return response.json()
