from aiohttp import web
import jinja2
import aiohttp_jinja2

from settings import config

from db import mysql_engine, background_tasks
from views import routes


if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    app['config'] = config
    app.cleanup_ctx.append(mysql_engine)
    app.cleanup_ctx.append(background_tasks)
    app.add_routes(routes)
    web.run_app(app)
