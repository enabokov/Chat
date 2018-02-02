from functools import partial
from service.settings import STATIC_ROOT


def setup_jinja2(env, app=None):
    def _url(app, router, query=None, **extras):
        return app.router[router].url_for(**extras).with_query(query)

    def _static(css_filename):
        return f'../{STATIC_ROOT}/{css_filename}'

    env.globals['url'] = partial(_url, app)
    env.globals['static'] = _static

    return env
