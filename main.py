from fastapi import FastAPI
from random import randrange

app = FastAPI()

weapons: list[str] = ['rock', 'paper', 'scissors']
game_key: dict[tuple[str, str], str] = {
    (weapons[0], weapons[0]): "It's a tie.",
    (weapons[0], weapons[1]): "You lost.",
    (weapons[0], weapons[2]): "You won!",
    (weapons[1], weapons[0]): "You won!",
    (weapons[1], weapons[1]): "It's a tie.",
    (weapons[1], weapons[2]): "You lost.",
    (weapons[2], weapons[0]): "You lost.",
    (weapons[2], weapons[1]): "You won!",
    (weapons[2], weapons[2]): "It's a tie.",
}


def opp_weapon() -> str:
    """Returns a random weapon for the opponent's weapon

    :return: The opponent's weapon
    :type: str
    """
    return weapons[randrange(0, 3)]


@app.get('/')
async def read_root():
    return {'message': 'Hello World'}


@app.get('/shoot/{weapon}')
async def shoot(weapon: str):
    opponent: str = opp_weapon()
    message = game_key[(weapon, opponent)]
    result = {'user_weapon': weapon, 'opponent_weapon': opponent, 'message': message}

    return result
