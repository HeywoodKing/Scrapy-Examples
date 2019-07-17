# -*- coding: utf-8 -*-


import requests
import json

try:
    # res = requests.get('http://www.baidu.com')
    # res = requests.put('http://www.baidu.com')
    # res = requests.post('http://www.baidu.com')
    # res = requests.delete('http://www.baidu.com')
    # res = requests.options('http://www.baidu.com')
    # res = requests.head('http://www.baidu.com')
    # res = requests.patch('http://www.baidu.com')
    # data = {
    #     'name': 'zhangsan',
    #     'age': 20
    # }
    # res = requests.get('http://www.baidu.com', params=data)

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    #                   '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    # }
    # res = requests.get('https://www.zhihu.com', headers=headers)
    # res.encoding = 'utf-8'

    # data = {
    #     'name': 'zhangsan',
    #     'age': 20
    # }
    # res = requests.post('http://python.org', data=data)

    # 上传文件
    # files = {'files': open('git.jpg', 'rb')}
    # res = requests.post('http://httpbin.org/post', files=files)

    # 获取cookie
    res = requests.get('http://www.baidu.com')

    if res.status_code == requests.codes.ok:
        # print(res.content.decode(encoding='utf-8', errors='出错了'))
        # print(res.text.encode(encoding='utf-8', errors='出错了'))
        # print(res.text)
        # print(res.cookies)
        # print(res.headers)
        # print(res.reason)
        # print(res.apparent_encoding)
        # print(res.url)
        # print(res.json())
        # print(json.loads(res.text))
        # print(res.history)

        for key, value in res.cookies.items():
            print(key + ":" + value)
    else:
        print(res.status_code)
except Exception as e:
    print(e.args)


"""
Requests还附带了一个内置的状态码查询对象
主要有如下内容：

100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),

Redirection.
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
'resume_incomplete', 'resume',), # These 2 to be removed in 3.0

Client Error.
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),

Server Error.
500: ('internal_server_error', 'server_error', '/o\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication'),
"""
