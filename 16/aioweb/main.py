from aiohttp import web

from settings import config

from db import mysql_engine
from views import routes


if __name__ == '__main__':
    app = web.Application()
    app['config'] = config
    app.cleanup_ctx.append(mysql_engine)
    app.add_routes(routes)
    web.run_app(app)
