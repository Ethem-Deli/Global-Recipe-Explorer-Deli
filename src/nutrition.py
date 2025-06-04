def display_nutrition_info(recipe):
    nutrients = recipe.get('nutrition', {}).get('nutrients', [])
    for item in nutrients:
        print(f"{item['title']}: {item['amount']} {item['unit']}")
