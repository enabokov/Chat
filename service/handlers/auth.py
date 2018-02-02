import trafaret as t
from aiohttp import web

from misc.handlers import TemplateHandler
from service.trafaret import SignUpTrafaret

from . import BaseHandler


class Handler(
    BaseHandler,
    TemplateHandler,
):

    async def index(self, request):
        return self.render_template(
            template_name='page/index.html',
            request=request,
            context={},
        )

    async def signup_get(self, request):
        return self.render_template(
            template_name='page/auth.html',
            request=request,
            context={
                'signup': True,
            },
        )

    async def signup_post(self, request):
        get = dict(await request.post())

        try:
            data = SignUpTrafaret(get)  # noqa
        except t.DataError as exc:
            return self.render_template(
                template_name='page/auth.html',
                request=request,
                context={
                    'signup': True,
                    'errors': exc.as_dict()
                }
            )

        return web.Response(
            status=web.HTTPSeeOther.status_code,
            headers={
                'Location': '/chat',
            },
            content_type='text/html',
            charset='utf-8',
            reason=None,
        )

    async def login_get(self, request):
        return self.render_template(
            template_name='page/auth.html',
            request=request,
            context={
                'signup': False,
            },
        )

    async def login_post(self, request):
        return web.Response(
            status=web.HTTPSeeOther.status_code,
            headers={
                'Location': '/chat',
            },
            content_type='text/html',
            charset='utf-8',
            reason=None,
        )

    async def logout(self, request):
        return web.Response(
            status=web.HTTPSeeOther.status_code,
            headers={
                'Location': '/',
            },
            content_type='text/html',
            charset='utf-8',
            reason=None
        )
