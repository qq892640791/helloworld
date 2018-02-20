#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取百度贴吧图片
import urllib.request
import re
import time
# 根据url获取网页html内容
def get(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('UTF-8')
    print(html)
    return html
    #return page.read()

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg,html)
    
    return jpgs

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl,fileName):
    urllib.request.urlretrieve(imgUrl,fileName)
    
# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(nub,imgUrls,path = './c/'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        urllib.request.urlretrieve(url,''.join([path,str(nub)+'{0}.jpg'.format(count)]))
        count = count + 1

# 封装：从百度贴吧网页下载图片
def download(url,nub):
    
    html = get(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(nub,jpgs)
    
#def main():
for i in range(0,100):
    url = 'http://tieba.baidu.com/p/2256306796?pn='+str(i)
    download(url,i)
    time.sleep(10)
#if __name__ == '__main__':
    #main()
