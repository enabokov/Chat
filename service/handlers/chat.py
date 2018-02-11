from aiohttp_security import authorized_userid

from misc.handlers import TemplateHandler

from . import BaseHandler
from ..storages.users import Storage


class Handler(
    BaseHandler,
    TemplateHandler,
):
    def __init__(self, app):
        self.storage = Storage(app)

    async def chat(self, request):
        username = await authorized_userid(request)

        if username is None:
            return self.render_template(
                template_name='page/index.html',
                request=request,
                context={},
            )

        user_counter = await self.storage.get_all_users()

        return self.render_template(
            template_name='page/chat.html',
            request=request,
            context={
                'user_name': username,
                'user_count': len(user_counter),
            },
        )
