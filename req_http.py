import asyncio
from typing import Dict, List, Union

import requests

# A few handy JSON types
JSON = Union[int, str, float, bool, None, Dict[str, "JSON"], List["JSON"]]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

# The maximum amount of Pokemon
MAX_POKEMON = 905

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"


def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)
