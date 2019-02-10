from aiohttp import web
import aiohttp_jinja2

routes = web.RouteTableDef()


@routes.view('/hello')
@aiohttp_jinja2.template('hello/base.html')
class Hello(web.View):
    async def get(self):
        return {'result': "hello world"}


@routes.view('/test')
class Test(web.View):
    async def get(self):
        old_urls = self.request.app['old_urls']
        head_urls = old_urls[:100]
        return web.Response(text=f'first 100 urls: {head_urls}')

    async def post(self):
        post_data = await self.request.post()
        data = {k: v for k, v in post_data.items()}
        return web.json_response(f'{data}')
