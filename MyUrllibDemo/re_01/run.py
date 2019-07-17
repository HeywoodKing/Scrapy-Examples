# -*- coding: utf-8 -*-


import re

# 匹配字符串的第一个位置字符串并返回match
# match = re.search(r'[1-9]\d{5}', 'bas 109789')
# if match:
#     print(match.group(0))


# 从字符串开始位置处匹配并返回match，开始处未匹配到则返回空
# match = re.match(r'[1-9]\d{5}', '100894 III 220980')
# if match:
#     print(match.group(0))


# 匹配所有字符串并发挥匹配列表
# ls = re.findall(r'[1-9]\d{5}', 'abcd 232ll12 213233 胜多负少 189002')
# if ls:
#     print(ls)


# 使用匹配字符串分割字符串并返回分割后的列表，第三个参数可设置分割的数量
# ls = re.split(r'[1-9]\d{5}', 'safadf 123887 safdff 213232 090df sfadff 898980')
# ls = re.split(r'[1-9]\d{5}', 'safadf 123887 safdff 213232 090df sfadff 898980', maxsplit=1)
# if ls:
#     print(ls)


# 匹配所有字符串并返回匹配迭代器
# match_iter = re.finditer(r'[1-9]\d{5}', 'saf 223989 898984 389dfsjkdf fsdaf334 343242')
# if match_iter:
#     for m in match_iter:
#         print(m.group(0))


# 将匹配的字符串替换成，然后返回字符串, 还可设置替换数量
# s = re.sub(r'[1-9]\d{5}', ':zipcode', 'fjsk222333 898982 1289uu21 989101', 2)
# if s:
#     print(s)


# regex = re.compile(r'[1-9]\d{5}', flags=re.I|re.S|re.M)
# s = 'afaf 232322 123323u2313239 213231 ewr89'
# ls = re.findall(regex, s)
# if ls:
#     print(ls)


"""
match对象

属性：
.string  待匹配的文本
.re  使用中的匹配正则表达式
.pos  搜索文本的开始位置
.endpos  搜索文本的结束位置

方法：
.group(0)   获得匹配后的字符串
.start()   匹配字符串在原始字符串的开始位置
.end()    匹配字符串在原始字符串的结束位置
.span()   返回(.start(), .end())


"""

# 全文搜索，匹配第一个值
match = re.search(r'[1-9]\d{5}', 'sljf232333 23232r389882r938ss sffsf 321333')
if match:
    print(match)

    print(match.string)
    print(match.re)
    print(match.pos)
    print(match.endpos)

    print(match.group(0))
    print(match.start(), match.end())
    print(match.span())


"""
最小匹配
*?
+?
??
{m, n}?
"""



