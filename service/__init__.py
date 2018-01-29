from aiohttp import web
from .routes import setup_routes
import aiohttp_jinja2
import jinja2
from .settings import TEMPLATES_ROOT, STATIC_ROOT


class Server:
    def __init__(self):
        self.app = web.Application()

    def setup(self):
        setup_routes(self.app)

        aiohttp_jinja2.setup(
            self.app, loader=jinja2.FileSystemLoader(TEMPLATES_ROOT))

        self.app.router.add_static(
            '/static/',
            path=STATIC_ROOT,
            name='static')

    def run(self):
        web.run_app(self.app, host='127.0.0.1', port=8000)
