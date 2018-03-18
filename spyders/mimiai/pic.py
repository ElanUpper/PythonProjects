from lxml import etree
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import threading
from urllib.error import HTTPError
from html.parser import HTMLParser
from time import sleep
from urllib.request import urlretrieve
import chardet
import io, os
import gzip


url_heads = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Host': 'www.mimis9.com',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

fix_pre = 'http://www.mimis9.com/';
arr_urls   = [];
arr_images = [];

def get_links(url, list) :
  try:
    html_parser = HTMLParser();
    req = Request(url=url, headers=url_heads);
    content_raw = urlopen(req).read();
    encoding = chardet.detect(content_raw);
    content_unzip = gzip.GzipFile(fileobj=io.BytesIO(content_raw), mode="rb").read()
    content = content_unzip.decode('gbk', 'ignore')
    xml = etree.HTML(content)
    # 抓取所有标题
    lines = xml.xpath("//td[@class='f_title']/a[1]/text()");
    links = xml.xpath("//td[@class='f_title']/a[1]/@href");
    for (line, link) in zip(lines, links):
      list.append([line, fix_pre + link]);

  except HTTPError as e:
    print(e.code)

def get_images(url_info, image_list) :
  try:
    i = 0;
    html_parser = HTMLParser();
    req = Request(url=url_info[1], headers=url_heads);
    content_raw = urlopen(req).read();
    encoding = chardet.detect(content_raw);
    content_unzip = gzip.GzipFile(fileobj=io.BytesIO(content_raw), mode="rb").read()
    content = content_unzip.decode('gbk', 'ignore')
    xml = etree.HTML(content)
    # 抓取所有标题
    lines = xml.xpath("//div[@class='t_msgfont']/img/@src");
    # 如果文件夹不存在 那么就新建
    curPath = os.getcwd()
    foldername = url_info[0]
    targetPath = curPath + os.path.sep + foldername
    if not os.path.exists(targetPath):
      os.makedirs(targetPath)
    for line in lines :
      image_list.append([url_info[0], line]);
      # 下载文件
      i = i + 1;
      filePath = targetPath + os.path.sep + str(i) + '.jpg'
      print(filePath)
      thread = threading.Thread(target=urlretrieve, args=(line, filePath))
      thread.start();
      thread.join();
      #urlretrieve(line, filePath);
    sleep(20)


  except HTTPError as e:
    print(e.code)


url = 'http://www.mimis9.com/forumdisplay.php?fid=59&page=1';
get_links(url, arr_urls) ;
print(arr_urls)
for s_url in arr_urls :
  sleep(1)
  print(s_url[0], s_url[1])
  get_images(s_url, arr_images) ;
print(arr_images)

