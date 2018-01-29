from aiohttp_jinja2 import render_template


async def index(request):
    return render_template(
        'index.html',
        request,
        context={},
    )


async def chat(request):
    return render_template(
        'chat.html',
        request,
        context={},
    )
