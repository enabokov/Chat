from aiohttp import web
from .routes import setup_routes
from jinja2 import Environment, FileSystemLoader
from .settings import TEMPLATES_ROOT, STATIC_ROOT, JINJA2_ENVIRONMENT
from .middlewares import TemplateMiddleware
from service.handlers import Router


class Server(
    TemplateMiddleware,
):

    router = None

    def __init__(self):
        self.app = web.Application()

    def setup(self):
        jinja2_env = Environment(
            loader=FileSystemLoader(TEMPLATES_ROOT))
        self.app[JINJA2_ENVIRONMENT] = jinja2_env
        jinja2_env.globals['app'] = self.app

        self.app.router.add_static(
            '/static/',
            path=STATIC_ROOT,
            name='static')

        self.router = Router()
        self.router.setup_index_handlers()
        self.router.setup_chat_handlers()

        setup_routes(self.app, self.router)

        self.app.middlewares.append(self.middleware)

    def run(self):

        self.setup()

        web.run_app(self.app, host='127.0.0.1', port=7777)
