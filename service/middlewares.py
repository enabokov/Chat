# from aiohttp import web
# from aiohttp_jinja2 import render_template


# @web.middleware
# async def middleware(request, handler):
#     try:
#         response = await handler(request)
#     except web.HTTPUnauthorized as exc:
#         return
