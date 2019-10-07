# -*- coding:utf-8 -*-
# @time:    2019/10/7 上午10:13
# @time:    2019-10-07 10:13:40
# @author:  Flack
# @email:   opencoding@hotmail.com
# @file:    run.PY
# @product: PyCharm

from scrapy import cmdline


name = 'chouti'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
