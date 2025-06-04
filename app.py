from flask import Flask, render_template, request, redirect, url_for, jsonify
from src.search import search_recipes
from src.recipe_display import get_recipe_details
from src.favorites import load_favorites, add_to_favorites
from src.country_info import get_country_facts
from src.weekly_generator import generate_weekly_recipes
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('q')
    recipes = search_recipes(query) if query else []
    return render_template('index.html', query=query, results=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = get_recipe_details(recipe_id)
    country_name = recipe.get('cuisines', [''])[0] or "Unknown"
    country_info = get_country_facts(country_name)
    return render_template('recipe_detail.html', recipe=recipe, country=country_info)

@app.route('/favorites')
def favorites():
    favs = load_favorites()
    return render_template('favorites.html', favorites=favs)

@app.route('/add_favorite/<int:recipe_id>')
def add_favorite(recipe_id):
    recipe = get_recipe_details(recipe_id)
    add_to_favorites(recipe)
    return redirect(url_for('favorites'))

@app.route('/weekly')
def weekly():
    weekly_recipes = generate_weekly_recipes()
    return render_template('weekly.html', recipes=weekly_recipes)

if __name__ == '__main__':
    app.run(debug=True)

# Load your API key from env or config
SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY') or 'your_api_key_here'

@app.route('/api/recipe/<int:recipe_id>')
def get_recipe_details(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {'apiKey': SPOONACULAR_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'id': data['id'],
            'title': data['title'],
            'summary': data.get('summary', ''),
            'image': data['image']
        })
    return jsonify({'error': 'Recipe not found'}), 404
