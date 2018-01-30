from misc.handlers import TemplateHandler

from . import BaseHandler


class Handler(
    BaseHandler,
    TemplateHandler,
):

    async def index(self, request):
        return self.render_template(
            template_name='page/index.html',
            request=request,
            context={},
        )
