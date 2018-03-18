from lxml import etree
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from html.parser import HTMLParser
import chardet
import io
import gzip

url_heads = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.jianshu.com',
    'Origin': 'https://www.jianshu.com',
    'Referer': 'https://www.jianshu.com/p/569c1c0afe1f',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

url_data = {
    'username': 'elan',
    'password': '1234'
};

try:
    # handle escape character
    html_parser = HTMLParser();
    # encode post data
    encode_data = urlencode(url_data);
    # url address
    url = 'https://www.jianshu.com/p/569c1c0afe1f';
    # prepare request template
    req = Request(url=url, headers=url_heads);
    # fetch raw data
    content_raw = urlopen(req).read();
    # fetch the encoding
    encoding = chardet.detect(content_raw);
    print('encoding:', encoding);
    # gzip
    content_unzip = gzip.GzipFile(fileobj=io.BytesIO(content_raw), mode="rb").read()
    # decode to utf-8
    if encoding not in ( 'utf-8', 'UTF-8' ) :
       content = content_unzip.decode('utf-8', 'ignore')
    else:
       content = content_unzip.read()
    content = html_parser.unescape(content)
    xml = etree.HTML(content)
    # 抓取所有标题
    output = xml.xpath('/html//h2/text() | /html//h1/text()');
    print(output)
except HTTPError as e:
    print(e.code)