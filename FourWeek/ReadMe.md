
## 安装必选库

### requests
`pip install requests`

### selenium
下载chrome driver,确保[最新release](http://npm.taobao.org/mirrors/chromedriver/)已经放入path可见的位置
完成后安装selenium
`pip install selenium` 
**测试**
```python
from selenium import webdriver
driver = webdriver.Chrome();
driver.get('http://www.baidu.com');
```

### phantomjs
通过[下载地址](http://phantomjs.org/download.html)进行下载并选择windows版本
完成后将phantomjs.exe加入到path中
**测试**
```python
from selenium import webdriver
driver = webdriver.PhantomJS();
driver.get('http://www.baidu.com');
print(driver.page_source);
```
### lxml
`pip install lxml`

### beautifulsoup
`pip install beautifulsoup4`
**测试**
```python
from bs4 import BeautifulSoup
html='<html><head>Hello world</head></html>'
soup = BeautifulSoup(html, 'lxml');
print(soup.p)
```

### pyquery
`pip install pyquery`


### pymysql
`pip install pymysql`
**测试**
```python
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='Abcd1234',
                       port=3306, db='elan');
cursor = conn.cursor();
cursor.execute('select * from stus');
print(cursor.fetchall());
```

### pymongo
`pip install pymongo`
**测试**
```python
import pymongo
client = pymongo.MongoClient('localhost');
db = client['test'] # db name
db['user'].insert({'elan3':'elan3'}, {'elan4':'elan4'});
db['user'].find_one({'elan3':'elan3'})
```

### redis
`pip install redis`
**测试**
```python
import redis
rd = redis.Redis('localhost', 6379);
rd.set('name', 'jem');
print(rd.get('name'));
```

### flask
`pip install flask`
**测试**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello world!';

if __name__ == '__main__' :
  app.run();
```

### django
`pip install django`
**测试**
`python -m django --version`

### python notebook:jupyter
`pip install jupyter`
**测试**
`jupyter notebook`
