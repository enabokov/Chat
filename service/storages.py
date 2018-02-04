import asyncpg
from aiohttp import web


class Storage:
    public_fields = ('name',)
    private_fields = ('password',)

    def __init__(self, app, loop):
        self.pool = app['pool']
        loop.run_until_complete(self.create_table())

    async def create_table(self):
        sql = '''
            CREATE TABLE users(
              id serial PRIMARY KEY,
              name VARCHAR(20) NOT NULL UNIQUE,
              password VARCHAR(20) NOT NULL
            );
        '''

        try:
            async with self.pool.acquire() as connection:
                await connection.execute(sql)
        except asyncpg.DuplicateTableError:
            pass

        return

    async def get_by_name(self, data):
        sql = '''
            SELECT name FROM users WHERE name = $1
        '''

        name = data['name']

        async with self.pool.acquire() as connection:
            user = await connection.fetch(sql, name)

        return list(map(dict, user))[0]

    async def get_all_users(self):
        sql = ''' SELECT * FROM users'''

        async with self.pool.acquire() as connection:
            result = await connection.fetch(sql)

        return list(map(dict, result))

    async def insert(self, data):
        sql = '''
            INSERT INTO users (name, password) VALUES ($1, $2)
        '''

        name = data['name']
        password = data['password']

        try:
            async with self.pool.acquire() as connection:
                await connection.execute(sql, name, password)
        except asyncpg.exceptions.UniqueViolationError:
            raise web.HTTPBadRequest(reason='User already exists. '
                                            'Try another name')
        return
