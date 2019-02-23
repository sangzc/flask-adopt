import requests
from secrets import PETFINDER_API_KEY


def get_info_random_pet():
    response = requests.get(
        "http://api.petfinder.com/pet.getRandom",
        params={"format": "json",
                "key": PETFINDER_API_KEY,
                "output": "basic"}
    )

    return response.json()
