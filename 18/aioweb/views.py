from aiohttp import web

routes = web.RouteTableDef()


@routes.view('/')
class Hello(web.View):
    async def get(self):
        return web.Response(text='Hello, world')


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


# 自己改写成基于类的视图吧，试试看！
@routes.get('/id/{id}')
async def get_counts(request):
    """
    从数据库中获取id对应的url
    """
    id_ = request.match_info['id']  # 从url中读取id
    async with request.app['mysql_engine'].acquire() as conn:
        async with conn.cursor() as cur:
            # 从名为crawl_result的表中获取id对应的url
            sql = "select url from crawl_result where id=%s"
            await cur.execute(sql, (id_, ))
            (url, ) = await cur.fetchone()
    return web.Response(text=f'{id_} url: {url}')
