from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text='Hello, world')


@routes.get('/test')
async def get_conf(request):
    old_urls = request.app['old_urls']
    head_urls = old_urls[:100]
    return web.Response(text=f'first 100 urls: {head_urls}')


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
