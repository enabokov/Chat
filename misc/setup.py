import asyncpg

from configs import postgres as pg
from misc.core import retry


@retry(times='forever')
async def setup_postgres(
    host=pg.HOST,
    port=pg.PORT,
    user=pg.USER,
    password=pg.PASSWORD,
    database=pg.DATABASE,
    *,
    loop,
):
    return await asyncpg.create_pool(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        loop=loop,
    )
