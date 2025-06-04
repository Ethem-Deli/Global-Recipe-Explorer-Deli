from api import fetch_recipes

def search_recipes(query):
    results = fetch_recipes(query)
    return results.get('results', [])
