import asyncio

import aiomysql


async def mysql_engine(app):
    mysql_conf = app['config']['mysql']
    host, port, user, password, db = mysql_conf['host'], mysql_conf['port'], mysql_conf['user'], mysql_conf['password'], mysql_conf['db']
    app['mysql_engine'] = await aiomysql.create_pool(host=host, port=port, user=user, password=password, db=db, loop=app.loop)
    yield
    app['mysql_engine'].close()
    await app['mysql_engine'].wait_closed()


async def get_old_urls(app):
    while True:
        async with app['mysql_engine'].acquire() as conn:
            async with conn.cursor() as cur:
                sql = "select url from crawl_result where link!='' and id>7990000 limit 2000"
                await cur.execute(sql)
                app['old_urls'] = {url for url, in await cur.fetchall()}  # 注意逗号
        print('get old_urls!')
        interval = float(app['config']['update_interval'])
        await asyncio.sleep(3600*interval)  # 每隔interval小时运行一次


async def background_tasks(app):
    app['get_old_urls'] = app.loop.create_task(get_old_urls(app))
    yield
    app['get_old_urls'].cancel()
    await app['get_old_urls']
