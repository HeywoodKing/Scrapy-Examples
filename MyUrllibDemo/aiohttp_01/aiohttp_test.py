# -*- coding: utf-8 -*-


import asyncio
import aiohttp
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
domain = 'https://www.datasheets.com'


async def get_body(url, loop=None):
    conn = aiohttp.TCPConnector(ssl=False,
                                use_dns_cache=True,
                                limit=200
                                )
    async with aiohttp.ClientSession(
                                     connector=conn,
                                     # conn_timeout=10,
                                     # read_timeout=10,
                                     headers=headers
                                     ) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            return html


async def get_result(item, html, loop=None):
    status = 1000
    pdf_urls = []
    try:
        status = 200
        soup = BeautifulSoup(html, 'html.parser')
        a_list = soup.find_all('a', class_='partdetail-link')
        for a in a_list:
            print(a, a.attrs)
            try:
                href = a['href']
                model_no = href.split('/')[-1]
                new_url = '{}/datasheet/{}'.format(domain, model_no)
                await asyncio.sleep(2)
                html = await get_body(new_url, loop)
                soup = BeautifulSoup(html, 'html.parser')
                a_link = soup.find('a', class_='button datasheet-download-button gtm-datasheet-download_button -main')
                pdf_urls.append(a_link['href'])
            except Exception as ex:
                print('901 error {}'.format(ex))

        if pdf_urls:
            print("{},{},{}".format(status, item, pdf_urls))
        else:
            status = 900
        return status, item, pdf_urls
    except Exception as ex:
        status = 1000
        print(status, item, ex)
        return status, item, pdf_urls


async def handler_result(item, loop=None):
    url = '{}/search/{}'.format(domain, item)
    html = await get_body(url, loop)
    print(html)
    return await get_result(item, html, loop)
    # await asyncio.sleep(3)


def callback(future):
    print('callback:{}'.format(future.result()))


async def main(loop=None):
    jobs = [
        'BOERMS712',
        'WCM5936',
    ]
    tasks = []
    for job in jobs:
        task = asyncio.create_task(handler_result(job, loop))
        task.add_done_callback(callback)
        tasks.append(task)

    results = await asyncio.gather(*tasks)


def eventloop():
    print('开始事件循环')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.run_until_complete(asyncio.sleep(0.3))
        loop.close()
        print('关闭事件循环')


if __name__ == '__main__':
    eventloop()
