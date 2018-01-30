
class BaseHandler:
    pass


class Router:

    index = chat = None

    def __init__(self):
        self.handlers = set()
        self.routers = set()

    def setup_index_handlers(self):
        from .index import Handler

        handler = Handler()

        self.handlers.add(handler)

        self.index = handler

        return handler

    def setup_chat_handlers(self):
        from .chat import Handler

        handler = Handler()

        self.handlers.add(handler)

        self.chat = handler

        return handler
