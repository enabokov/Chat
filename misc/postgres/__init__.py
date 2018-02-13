import asyncpg


class PostgresMixin:

    async def write(self, pool, sql, *params):
        try:
            async with pool.acquire() as connection:
                async with connection.transaction():
                    await connection.execute(sql, *params)
        except asyncpg.DuplicateTableError:
            pass

        return

    async def read(self, pool, sql, *params):
        async with pool.acquire() as connection:
            async with connection.transaction():
                result = await connection.fetch(sql, *params)
        return result
