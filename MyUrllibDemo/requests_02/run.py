# -*- coding: utf-8 -*-


import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'biihu__Session=psht869clu425bnaqa0rq03rrs; Hm_lvt_f1d3b035c559e31c390733e79e080736=1562931092; biihu__user_login=Th9bxePwAwubGtEhLRuodzx7tIZyTeB2t6zfagU1y0%2BY1STGtRdrsVWRcRVPgZOzrgzxEoq6AiA%2FO84zvTuil0%2BoB6I%2F6e9HHPUn38xI2DLZ7iYoKBoitt9tXAGjU44lVCl1P1cMKdLzBeS%2FERjnpVZJvq0YGrmVRlE00PjMb1k%3D; Hm_lpvt_f1d3b035c559e31c390733e79e080736=1562931435',
    'Host': 'biihu.cc',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
}


url = 'https://biihu.cc/'
session = requests.session()
res = session.get(url, headers=headers)
print(res.text)
