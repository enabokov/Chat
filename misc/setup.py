import asyncpg

from configs.postgres import DATABASE, HOST, PASSWORD, PORT, USER


async def setup_postgres(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
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
