from misc.handlers import TemplateHandler

from . import BaseHandler


class Handler(
    BaseHandler,
    TemplateHandler,
):

    async def chat(self, request):
        return self.render_template(
            template_name='page/chat.html',
            request=request,
            context={},
        )
