from functools import namedtuple
from aiohttp_security.abc import AbstractAuthorizationPolicy


class DictAuthorization(AbstractAuthorizationPolicy):

    def __init__(self, user_map):
        super().__init__()
        self.user_map = user_map

    async def authorized_userid(self, identity):
        if identity in self.user_map:
            return identity
        else:
            return 'Should be remembered'

    async def permits(self, identity, permission=None, context=None):
        user = self.user_map.get(identity)
        if not user:
            return False
        return permission in user.permissions


async def check_credentials(user_map, username, password):
    user = user_map.get(username)
    if not user:
        return False

    return user.password == password

User = namedtuple('User', ['username', 'password'])

user_map = {}


def add_user(name, password):
    user_map[name] = User(name, password)
