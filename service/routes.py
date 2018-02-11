

def setup_routes(
    app,
    router,
):

    app.router.add_route(
        'POST',
        '/message',
        router.message.message,
        name='api:message',
    )

    app.router.add_route(
        'POST',
        '/message/cached',
        router.message.get_cached_messages,
        name='api:cached_messages',
    )

    app.router.add_route(
        'POST',
        '/message/current',
        router.message.get_current_messages,
        name='api:current_messages',
    )

    app.router.add_route(
        'GET',
        '/',
        router.auth.index,
        name='page:index',
    )

    app.router.add_route(
        'GET',
        '/signup',
        router.auth.signup_get,
        name='page:signup_get',
    ),

    app.router.add_route(
        'POST',
        '/signup',
        router.auth.signup_post,
        name='page:signup_post'
    )

    app.router.add_route(
        'GET',
        '/login',
        router.auth.login_get,
        name='page:login_get',
    )

    app.router.add_route(
        'POST',
        '/login',
        router.auth.login_post,
        name='page:login_post',
    )

    app.router.add_route(
        'POST',
        '/',
        router.auth.logout,
        name='page:logout',
    )

    app.router.add_route(
        'GET',
        '/chat',
        router.chat.chat,
        name='page:chat',
    )
