from conf import PARSING, DATAJSON
from database.async_db import asyncHandler as db
from database.parsing.parsing_kino import start
from database.NLP.processing import calc_vectors

if __name__ == '__main__':
    db.init_db()

    if PARSING:
        print("parsing start")
        start(DATAJSON)

        print("vectorization start")
        calc_vectors()
