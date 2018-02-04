import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
filename = 'words_cn.txt'
with open(filename, encoding="utf-8") as fp :
    analysisTxt = fp.read()
mytext = " ".join(jieba.cut(analysisTxt))
# print(mytext)
wordcloud = WordCloud(font_path="simsun.ttf", width=2014, height=768).generate(analysisTxt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.interactive(False)
#plt.show()