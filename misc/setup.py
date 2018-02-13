import asyncio

import asyncpg

from configs import postgres as pg
from misc.core import retry

from .singleton import Singleton


class Loop(metaclass=Singleton):

    __loop_instance = None

    def get_loop(self):
        if self.__loop_instance is None:
            self.__loop_instance = asyncio.get_event_loop()

        return self.__loop_instance


@retry(times=3)
async def setup_postgres(
    host=pg.HOST,
    port=pg.PORT,
    user=pg.USER,
    password=pg.PASSWORD,
    database=pg.DATABASE,
    dsn=pg.DSN,
    *,
    loop,
):
    return await asyncpg.create_pool(
        dsn=dsn,
        # host=host,
        # port=port,
        # user=user,
        # password=password,
        # database=database,
        loop=loop,
    )
