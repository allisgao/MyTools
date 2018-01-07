#! python3
# coding=utf-8

# download_liangzhu.py - Downloads a suite numbered musical notation called Liangzhu, THE BUTTERFLY LOVERS.

import requests, os, bs4,urllib3

url = 'http://www.yueqixuexi.com'
#jp1Url = '/dongxiao/qupu/20141015124007.html'
# 文件存放路径
os.makedirs('D:\\Picture\\简谱\\梁祝', exist_ok=True)

# 先研究第一张简谱
# 打开第一个页面并下载页面
# jp1URL = url + jp1Url
jp1Res = requests.get('http://www.yueqixuexi.com/dongxiao/qupu/20141015124007.html')
jp1Res.raise_for_status()
jp1Soup = bs4.BeautifulSoup(jp1Res.text, "lxml")
#markup_type=
# 从页面查找简谱图片的url
jp1Elem = jp1Soup.select('#icontent img')
jp1NameElem = jp1Soup.select('h2')
# 下载图片
## 图片名
# jpName = jpElem[0].get('alt')
jp1Name = jp1NameElem[0].text
## 图片地址
jp1Addr = jp1Elem[0].get('src')

jp1Url = url + jp1Addr
# 将图片保存在上文规划的目录
print('简谱%s下载中...' %jp1Name)
jp1Res = requests.get(jp1Url)
jp1Res.raise_for_status()
jp1File = open(os.path.join('D:\\Picture\\简谱\\梁祝', jp1Name + '.gif'), 'wb')
for chunk in jp1Res.iter_content(10000):
    jp1File.write(chunk)
jp1File.close()
print('简谱%s下载完成！' %jp1Name)

# 打开“下一页”，循环


for i in range(2,13):
    jpName = '12个不同版本箫谱《梁祝》简谱_' + str(i) + '.gif'
    pgUrl = 'http://www.yueqixuexi.com/dongxiao/qupu/20141015124007_' + str(i) + '.html'
    print('简谱%s下载中...' % jpName)
    jpRes = requests.get(pgUrl)
    jpRes.raise_for_status()
    jpSoup = bs4.BeautifulSoup(jpRes.text,'lxml')
    jpElem = jpSoup.select('#icontent img')
    jpAddr = jpElem[0].get('src')
    jpUrl = url + jpAddr
    ## 这个地方如果不对“jpRes”进行覆盖，保存的是第一个“jpRes”的结果。
    jpRes = requests.get(jpUrl)
    jpRes.raise_for_status()
    jpFile = open(os.path.join('D:\\Picture\\简谱\\梁祝', jpName), 'wb')
    for chunk in jpRes.iter_content(10000):
        jpFile.write(chunk)
    jpFile.close()
    print('简谱%s下载完成！' % jpName)






