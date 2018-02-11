import asyncpg
from aiohttp import web

from misc.postgres import PostgresMixin
from misc.setup import Loop


class Storage(
    Loop,
    PostgresMixin,
):
    public_fields = ('name',)
    private_fields = ('password',)

    def __init__(self, app):
        self.loop = self.get_loop()
        self.pool = app['pool']
        self.loop.run_until_complete(self.create_table())

    async def create_table(self):
        sql = '''
            CREATE TABLE users(
              id serial PRIMARY KEY,
              name VARCHAR(20) NOT NULL UNIQUE,
              password VARCHAR(20) NOT NULL
            );
        '''
        return await self.write(self.pool, sql)

    async def get_by_name(self, data):
        sql = '''SELECT name FROM users WHERE name = $1'''
        user = await self.read(self.pool, sql, data['name'])

        user = list(map(dict, user))

        if not user:
            return

        if len(user) > 1:
            raise web.HTTPBadRequest(
                reason='Duplicated names found in postgres!')

        return user[0]

    async def get_by_name_with_password(self, data):
        sql = '''SELECT name FROM users WHERE name = $1 AND password = $2'''
        user = await self.read(
            self.pool, sql, data['name'], data['password'])

        user = list(map(dict, user))

        if not user:
            return

        if len(user) > 1:
            raise web.HTTPBadRequest(
                reason='Duplicated names found in postgres!')

        return user[0]

    async def get_all_users(self):
        sql = '''SELECT * FROM users'''
        users = await self.read(self.pool, sql)
        return list(map(dict, users))

    async def insert(self, data):
        sql = '''INSERT INTO users (name, password) VALUES ($1, $2)'''
        try:
            return await self.write(
                self.pool, sql, data['name'], data['password'])
        except asyncpg.exceptions.UniqueViolationError:
            raise web.HTTPBadRequest(
                reason='User already exists. Try another name')
