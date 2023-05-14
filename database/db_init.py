from conf import PARSING, DATAJSON
from database.async_db import asyncHandler as db
from database.parsing.parsing_kino import start
from database.NLP.processing import calc_vectors
from asyncio import run


def db_init():
    run(db.init_db())

    if PARSING:
        print("parsing start")
        start("database/parsing/" + DATAJSON)

        print("vectorization start")
        run(calc_vectors())

    print("db init end")


if __name__ == '__main__':
    db_init()
