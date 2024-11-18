import requests


def fetch_spacex_launches():    
    url = "https://api.spacexdata.com/v4/launches"
    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()
        return launches
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao conectar à API SpaceX: {e}"}
