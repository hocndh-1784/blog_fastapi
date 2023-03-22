import requests
from fastapi import HTTPException


def get_dummy_user(user_id: int):
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
