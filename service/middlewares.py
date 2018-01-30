from aiohttp import web

from misc.handlers import TemplateHandler


class TemplateMiddleware:

    encoding = 'utf-8'
    handler = TemplateHandler()

    @web.middleware
    async def middleware(self, request, handler):
        try:
            return await handler(request)
        except web.HTTPUnauthorized as exc:
            return self.handler.render_template(
                template_name='errors/Unauthorized.html',
                request=request,
                context={'error': exc.reason},
                status=exc.status,
            )

        except web.HTTPNotFound as exc:
            return self.handler.render_template(
                template_name='errors/NotFound.html',
                request=request,
                context={'error': exc.reason},
                status=exc.status,
            )

        except web.HTTPBadRequest as exc:
            return self.handler.render_template(
                template_name='errors/BadRequest.html',
                request=request,
                context={'error': exc.reason},
                status=exc.status,
            )
