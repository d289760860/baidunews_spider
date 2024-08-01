from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
import argparse 
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
#user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"

# 我们并不需要浏览器弹出
options = Options()
options.add_argument('--headless')
#options.binary_location = "D:\Programs\ChromeDriver\chromedriver-win64\chromedriver.exe"

class keywords:
    words = []
    def __init__(self, filename): 
        fileHandler  =  open  (filename,  "r", encoding='utf-8')
        # Get list of all lines in file
        listOfLines  =  fileHandler.readlines()
        # Close file
        fileHandler.close()
        for  line in  listOfLines:
            self.words.append(line.strip())
            
    def printWords(self):
        for word in self.words:
            print(word)
            
    def getWords(self):
        return self.words
    
def info_def(html):
    #print(html)
    soup = BeautifulSoup(html, 'html.parser', from_encoding="gb18030") 
    news_list = soup.select('div#content_left > div > div > h3 > a')
    #news_list = soup.select('div.newslist > ul > li > a')
    news_items = []
    for news in news_list:
        print(news['aria-label'])
        print(news['href'])
        print('\n')
        news_items.append(news['aria-label']+ '\n' + news['href'] + '\n\n')

    #for i in range(len(sentence)):
    return news_items
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input filename')
    # 命令行参数
    parser.add_argument('-f','--filename',type=str, help='用户指定的关键词文件名',default='keywords/keywords.txt')
    args = parser.parse_args()
    
    keys = keywords(args.filename)
    now_date = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
    result_file = open(now_date + '.txt','w',encoding = 'utf-8')
    s = Service("D:\Programs\EdgeDriver\msedgedriver.exe")
    driver = webdriver.Edge(service=s, options=options)
    for key in keys.getWords():
        print('当前关键字：',key)
        print('正在百度新闻搜索当日信息……')
        result_file.write(key+' 相关新闻：\n')
        url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd='+key+'&medium=0'
        driver.get(url)
        html = driver.page_source
        news_items = info_def(html)
        for i in range(len(news_items)):
            result_file.write(news_items[i])
    result_file.close()  
    driver.quit()
            