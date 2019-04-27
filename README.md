爬虫框架Scrapy Demo
```
python3.7.1

pip19.0.3

Scrapy1.6.0

scrapyd1.2.0

scrapyd-client1.1.0

selenium3.141.0

pillow5.3.0

Twisted19.2.0

pyecharts0.5.11

pymongo3.8.0

virtualenv16.4.0
```

All Demo:

1.爬取生物谷文章列表+详情

2.爬取豆瓣影评得分

3.爬取新浪新闻+详情

4.爬取StackOverFlow站问题+star数量

5.爬取腾讯社招信息（使用rules规则爬取1页的数据）

6.爬取腾讯社招信息（爬取多页数据）

7.爬取西刺IP代理数据

8.爬取天猫商城商品信息



使用scrapyd部署爬虫

1.安装scrapyd
pip install scrapyd

2.启动scrapyd服务
直接在cmd中输入：scrapyd 即启动了服务

3.在浏览器检查是否服务启动成功，打开浏览器输入：localhost:6800

4.Example using curl:
curl http://localhost:6800/schedule.json -d project=default -d spider=somespider

5.安装上传工具
pip install scrapyd-client

6.上传命令
python D:\python37\Scripts\scrapyd-deploy localhost -p project

7.安装调度工具curl
pip install curl

8.调度
curl http://localhost:6800/schedule.json -d project=MyScrapyDouBan -d spider=DouBanMovie

9.取消调度
curl http://localhost:6800/cancel.json -d project=MyScrapyDouBanMovie -d job=第8部调度产生的jobid

10.查看部署了哪些工程
curl http://localhost:6800/listprojects.json



