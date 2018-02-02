from aiohttp import web

from service.settings import JINJA2_CONTEXT, JINJA2_ENVIRONMENT


class TemplateHandler:

    encoding = 'utf-8'

    def render_string(self,
                      template_path,
                      request,
                      context,
                      jinja2_key=JINJA2_ENVIRONMENT):
        env = request.app.get(jinja2_key)
        template = env.get_template(template_path)

        if request.get(JINJA2_CONTEXT):
            context = dict(request[JINJA2_CONTEXT], **context)

        return template.render(context)

    def render_template(self,
                        template_name,
                        request,
                        context,
                        *,
                        jinja2_key=JINJA2_ENVIRONMENT,
                        encoding=encoding,
                        status=web.HTTPOk.status_code):
        if context is None:
            context = {}

        text = self.render_string(
            template_path=template_name,
            request=request,
            context=context,
            jinja2_key=jinja2_key)

        return web.Response(
            status=status,
            text=text,
            content_type='text/html',
            charset=encoding,
        )
