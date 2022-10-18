import asyncio
from random import randint

from req_http import JSONObject, MAX_POKEMON, POKEMON_URL, http_get


async def get_pokemon(pokemon_id: int) -> JSONObject:
    pokemon_url = f"{POKEMON_URL}{pokemon_id}"
    return await http_get(pokemon_url)


async def main() -> None:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon = await get_pokemon(pokemon_id + 1)
    print(pokemon["name"])


if __name__ == "__main__":

    asyncio.run(main())
