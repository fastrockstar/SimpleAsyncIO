import asyncio
from random import randint
from time import perf_counter
from typing import AsyncIterable

from req_http import MAX_POKEMON, POKEMON_URL, http_get


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"{POKEMON_URL}{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        yield await get_random_pokemon_name()


async def main():
    # retrieve the next 10 pokemon names
    time_before = perf_counter()
    async for name in next_pokemon(10):
        print(name)
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    # asynchronous list comprehensions
    time_before = perf_counter()
    names = [name async for name in next_pokemon(10)]
    print(names)
    print(f"Total time (synchronous): {perf_counter() - time_before}")


if __name__ == "__main__":
    asyncio.run(main())
