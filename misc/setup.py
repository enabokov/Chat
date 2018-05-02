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


@retry(times=5)
async def setup_postgres(
    dsn=pg.DSN,
    *,
    loop,
):
    return await asyncpg.create_pool(
        dsn=dsn,
        loop=loop,
    )
