from bs4 import BeautifulSoup
import requests

'''
url_headers = {
  'accept' : 'image/webp,image/apng,image/*,*/*;q=0.8',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_SORT_WRAPPER'
response = requests.get(url, headers=url_headers)
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.select('div.listing_title > a')
images = soup.select('listing_details > div[class="photo_booking non_generic"] > a > img[class="photo_image"]')
rates  = soup.select('div[class="p13n_reasoning_v2"] ')
#print(titles)
print('---------------------------------- images ----------------------------------------')
print(images)
print('---------------------------------- images ----------------------------------------')
print(rates)

for title, img, rate in zip(titles, images, rates):
  data = {
    'title': title.get_text(),
    'image': img.get('src'),
    'rate': list(rate.stripped_strings)
  }
 # print(data)
 '''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
# (for i in range(30, 390, 30));
#urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-{}New_York_City_New_York.html'.format(lambda i=0: '?) for i in range(30, 930, 30)]
#print(urls);