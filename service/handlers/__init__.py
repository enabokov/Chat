
class BaseHandler:
    pass


class Router:

    auth = None
    chat = None
    message = None

    def __init__(self, app):
        self.app = app
        self.handlers = set()
        self.routers = set()

    def setup_index_handlers(self):
        from .auth import Handler

        handler = Handler(self.app)

        self.handlers.add(handler)

        self.auth = handler

        return handler

    def setup_chat_handlers(self):
        from .chat import Handler

        handler = Handler(self.app)

        self.handlers.add(handler)

        self.chat = handler

        return handler

    def setup_message_handlers(self):
        from .message import Handler

        handler = Handler(self.app)

        self.handlers.add(handler)

        self.message = handler

        return handler
