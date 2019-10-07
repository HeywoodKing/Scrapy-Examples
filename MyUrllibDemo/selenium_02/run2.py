# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect


# 获取途牛网航空机票信息

# 单程
url_s = 'http://flight.tuniu.com/domestic/list/SZX_TAO_ST_1_0_0/?start=2019-07-18'
# 往返
url_t = 'http://flight.tuniu.com/domestic/list/SZX_TAO_SRT_1_0_0?deptDate=2019-07-18&arrvDate=2019-07-20'
try:
    # 1.通过命令行参数指定代理
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=127.0.0.1:8080')

    # 2.使用插件控制代理
    # chrome_options.add_argument('--load-extension=SwitchyOmega')
    # Selenium 的 ChromeOptions 类还提供了一个方法 add_extension 用于直接加载未解压的插件文件
    # 这种做法依赖于 SwitchyOmega 的配置，如何在加载插件之前先把代理都配好？如何运行时动态的切换代理？这对爬虫来说至关重要
    # chrome_options.add_extension('SwitchyOmega.crx')

    # 3.使用自定义插件，自己开发Chrome插件控制代理，自动代理跳转，支持用户名和密码认证，
    # 还可以支持过滤不需要的请求，包括css和js,这样提高爬取效率

    # 使用代理服务器 BrowserMob Proxy，BrowserMob Proxy 简称 BMP，可以这么说，BMP 绝对是为 Selenium 为生的，
    # Selenium + BMP 的完美搭配，可以实现很多你绝对想象不出来的功能
    # 不是一个简单的代理，而是一个 RESTful 的代理服务，通过 BMP 提供的一套 RESTful 接口，
    # 你可以创建或移除代理，设置黑名单或白名单，设置过滤器规则等等
    # 可以说它是一个可编程式的代理服务器。BMP 是使用 Java 语言编写的，它前后经历了两个大版本的迭代，
    # 其核心也是从最初的 Jetty 演变为 LittleProxy，使得它更小巧和稳定
    """
    在 Windows 系统上，我们直接双击执行 bin 目录下的 browsermob-proxy.bat 文件。
　　BMP 启动后，默认在 8080 端口创建代理服务，此时 BMP 还不是一个代理服务器，需要你先创建一个代理：
　　curl -X POST http://localhost:8080/proxy
　　向 /proxy 接口发送 POST 请求，可以创建一个代理服务器。此时，我们在浏览器访问 http://localhost:8080/proxy 这个地址，
    可以看到我们已经有了一个代理服务器，端口号为 8081，现在我们就可以使用 127.0.0.1:8081 这个代理了
    """

    browser = webdriver.Chrome(executable_path=r'E:/Python/webdriver/chromedriver.exe',
                               chrome_options=chrome_options)
    browser.get(url_s)

    Wait(browser, 60).until(
        Expect.presence_of_element_located((By.CLASS_NAME, 'flightlist'))
    )

    flightlist = browser.find_element_by_class_name('flightlist')
    divs = flightlist.find_elements_by_class_name('J-flightlist')
    res_list = []
    # print(len(divs))
    for item in divs:
        res_dict = {}
        flight_name = item.find_element_by_class_name('aircom').text
        flight_no = item.find_element_by_class_name('J-flight').find_element_by_class_name('flihtnumber').find_elements_by_tag_name('span')[0].text
        price = item.find_element_by_class_name('J-right').find_element_by_class_name('wrapper').find_elements_by_tag_name('span')[0].text
        res_dict['flight_name'] = flight_name
        res_dict['flight_no'] = flight_no
        res_dict['price'] = price

        if res_dict not in res_list:
            res_list.append(res_dict)

        print(res_dict)

    print('结果：', res_list)

except:
    print('error')





