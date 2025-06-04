import requests

def get_country_facts(name):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
        country = response.json()[0]
        return {
            "name": country.get("name", {}).get("common", "Unknown"),
            "flag": country.get("flags", {}).get("png", ""),
            "population": country.get("population", "Unknown"),
            "region": country.get("region", "Unknown")
        }
    except:
        return {"name": name, "flag": "", "population": "N/A", "region": "N/A"}
