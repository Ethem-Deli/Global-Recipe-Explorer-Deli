import json
import os

FAV_FILE = "data/favorites.json"

def load_favorites():
    if not os.path.exists(FAV_FILE):
        return []
    with open(FAV_FILE, 'r') as f:
        return json.load(f)

def add_to_favorites(recipe):
    favs = load_favorites()
    if not any(r['id'] == recipe['id'] for r in favs):
        favs.append({'id': recipe['id'], 'title': recipe['title'], 'image': recipe['image']})
    with open(FAV_FILE, 'w') as f:
        json.dump(favs, f, indent=2)
