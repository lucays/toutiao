import random
import asyncio
import aiohttp

titles = []


async def get_html(url: str) ->None:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as r:
            await asyncio.sleep(random.random())
            # 如果要多个返回值，比如还要r.text()，那么应该是news, text = await r.json(), await r.text()，不要忽略后一个await
            news = await r.json(content_type=None)
            for i in news['result']:
                titles.append(i['title'])


def get_many(urls):
    loop = asyncio.get_event_loop()
    todo = [get_html(url) for url in urls]
    loop.run_until_complete(asyncio.wait(todo))


async def get_html2(url: str) ->dict:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as r:
            await asyncio.sleep(random.random())
            return await r.json(content_type=None)


def get_title(future):
    news = future.result()
    for i in news['result']:
        titles.append(i['title'])


def get_many2(urls):
    # windows上可以用ProactorEventLoop()避免ValueError: too many file descriptors in select()错误
    # loop = asyncio.ProactorEventLoop()
    # asyncio.set_event_loop(loop)

    loop = asyncio.get_event_loop()
    for url in urls:
        task = asyncio.ensure_future(get_html(url))
        # task = asyncio.ensure_future(get_html2(url))
        # task.add_done_callback(get_title)
    loop.run_until_complete(task)


def main():
    basic_url = 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=102707162&s=30&cp={0}&priority=0&callback='
    urls = [basic_url.format(i) for i in range(10)]
    # get_many(urls)
    get_many2(urls)
    print(len(titles))


if __name__ == "__main__":
    main()
