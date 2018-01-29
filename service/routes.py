from .views import chat, index


def setup_routes(
    app,
):
    app.router.add_route(
        'GET',
        '/',
        index,
        name='views:index',
    ),
    app.router.add_route(
        'GET',
        '/chat',
        chat,
        name='views:chat',
    )
