import aiomysql


async def mysql_engine(app):
    mysql_conf = app['config']['mysql']
    host, port, user, password, db = mysql_conf['host'], mysql_conf['port'], mysql_conf['user'], mysql_conf['password'], mysql_conf['db']
    app['mysql_engine'] = await aiomysql.create_pool(host=host, port=port, user=user, password=password, db=db, loop=app.loop)
    yield
    app['mysql_engine'].close()
    await app['mysql_engine'].wait_closed()
