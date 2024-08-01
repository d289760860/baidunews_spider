# 百度新闻爬虫

#### 介绍
爬取百度新闻上一系列关键词的第一页搜索结果，按照时间排序


#### 环境
1.  python 3.7
2.  beautifulsoup 4.12.3
3.  argparse 1.4
4.  selenium 4.11.2

#### 安装教程

因为国内直接使用pip install安装速度较慢，因此使用清华源安装。


`conda create -n py37 python=3.7`

`conda activate py37`

`pip --default-timeout=100 install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple`

`pip --default-timeout=100 install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple`

`pip --default-timeout=100 install argparse -i https://pypi.tuna.tsinghua.edu.cn/simple`

#### 使用说明
usage: baiduNews.py [-h] [-f FILENAME]

Input filename

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        用户指定的关键词文件名