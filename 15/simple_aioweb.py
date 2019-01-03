from aiohttp import web


async def hello(request):
    return web.Response(text='Hello, world')


async def test(request):
    return web.Response(text='test')


app = web.Application()
app.add_routes([web.get('/', hello),
                web.post('/', hello),
                web.get('/test', test),
                web.post('/test', test)
                ])
'''
app.add_routes([web.get('/', hello),
                web.get('/test', test),
                web.post('/', hello),
                web.post('/test', test)
                ])
'''
web.run_app(app)
