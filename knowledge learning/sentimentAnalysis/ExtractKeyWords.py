from jieba.analyse import *
with open('sample.txt', encoding='UTF-8') as fp:
  data = fp.read()

print('------------------ Term Frequency - inverse document frequency ------------------------- ')

for keyword, weight in extract_tags(data, topK=5, withWeight=True):
  print('%s %s' %(keyword, weight))

#for keyword, weight in extract_tags(data, topK=10, withWeight=True):
#  print('%s %s' % (keyword, weight))

print('------------------ Text rank ------------------------- ')

for keyword, weight in textrank(data, topK=5, withWeight=True):
    print('%s %s' % (keyword, weight))