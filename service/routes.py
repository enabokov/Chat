

def setup_routes(
    app,
    router,
):
    app.router.add_route(
        'GET',
        '/',
        router.index.index,
        name='index',
    ),

    app.router.add_route(
        'GET',
        '/chat',
        router.chat.chat,
        name='chat',
    )
