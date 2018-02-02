from aiohttp import web
from .routes import setup_routes
from jinja2 import Environment, FileSystemLoader
from .settings import TEMPLATES_ROOT, STATIC_ROOT, APP_ROOT, JINJA2_ENVIRONMENT
from .middlewares import TemplateMiddleware
from service.handlers import Router
import asyncio
from misc.jinja2 import setup_jinja2
import logging
import aioreloader


class Server(
    TemplateMiddleware,
):
    remote_host = '0.0.0.0'
    remote_port = 80

    host = '127.0.0.1'
    port = 7777

    router = None
    http_server = None
    loop = asyncio.get_event_loop()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = None

    def __init__(self):
        self.app = web.Application(loop=self.loop)
        self.reloader = aioreloader.start(loop=self.loop)
        logging.info('App initialized')

    def setup(self):
        jinja2_env = Environment(
            loader=FileSystemLoader([TEMPLATES_ROOT, APP_ROOT]))
        self.app[JINJA2_ENVIRONMENT] = jinja2_env

        jinja2_env = setup_jinja2(jinja2_env, self.app)
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

        self.handler = self.app.make_handler(loop=self.loop)

        aioreloader.watch('service/handlers/')

    def run(self):

        self.setup()
        http_server = self.loop.create_server(
            self.handler,
            self.host,
            self.port,
        )

        self.http_server = self.loop.run_until_complete(http_server)

        try:
            logging.info('App was started. '
                         'Running on %(host)s:%(port)s',
                         {'host': self.host, 'port': self.port})
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            logging.info('Aioreloader is closing')
            self.reloader.cancel()

            logging.info('HTTP Server is closing')
            self.http_server.close()
            logging.info('HTTP Server is closed')
            self.loop.run_until_complete(self.http_server.wait_closed())

            self.loop.run_until_complete(self.app.shutdown())
            logging.info('App was shutdown')
            self.loop.run_until_complete(self.handler.shutdown())
            logging.info('Handler is shutting down')

            self.loop.run_until_complete(self.app.cleanup())
            self.loop.close()
            logging.info('App was finished')
