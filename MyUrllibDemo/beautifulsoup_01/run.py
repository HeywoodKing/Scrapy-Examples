# -*- coding: utf-8 -*-


import requests
import re
from bs4 import BeautifulSoup


try:
    res = requests.get('http://www.python123.io/ws/demo.html')
    res.raise_for_status()
    res.encoding = 'utf-8'
    # print(res.text)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    # print(soup.a)
    # print(soup.a.name)
    # print(soup.a.string)
    # print(soup.a.attrs)
    # print(soup.a.attrs['href'])
    # print(soup.p)
    # print(soup.p.string)
    # print(soup.find_all('p'))

    # print(soup.title, soup.head, soup.body)
    # print(soup.a.parent.name)
    # print(soup.a.parent.parent.name)
    #
    # print(soup.head.contents)
    #
    # print(soup.body.contents)
    # print(len(soup.body.contents))
    # print(soup.body.contents[1])


    # ===============下行遍历================
    # # 遍历儿子  返回列表类型
    # for child in soup.body.contents:
    #     print(child)
    #
    # # 遍历子孙  返回迭代器类型
    # for child in soup.body.children:
    #     print(child)

    # 返回迭代器类型
    # for child in soup.body.descendants:
    #     print(child)
    # ===============下行遍历================

    # ===============上行遍历================
    # for child in soup.a.parent:
    #     print(child)

    # for child in soup.a.parents:
    #     print(child)
    # ===============上行遍历================

    # ===============平行遍历================
    # print(soup.a.previous_sibling)
    # print(soup.a.next_sibling.next_sibling)

    # # 遍历前序节点  返回迭代器
    # for p_node in soup.a.previous_siblings:
    #     print(p_node)
    #
    # # 遍历后续节点  返回迭代器
    # for n_node in soup.a.next_siblings:
    #     print(n_node)
    # ===============平行遍历================

    print(soup.find_all(id='link1'))
    print(soup.find_all(id=re.compile('link')))

    print(soup.find_all(string='Basic Python'))

    print(soup.find_all(string=re.compile('python', re.I)))

    """
    find()   返回字符串类型
    find_all()   返回列表类型
    find_parent()  返回一个结果字符串类型
    find_parents()
    find_next_sibling()
    find_previous_sibling()
    find_next_siblings()
    find_previous_siblings()    
    """

except:
    print('error')

