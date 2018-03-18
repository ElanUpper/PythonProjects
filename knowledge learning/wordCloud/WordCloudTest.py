import matplotlib.pyplot as plt
from wordcloud import WordCloud
filename = 'words.txt'
with open(filename) as fp :
    analysisTxt = fp.read()
wordcloud = WordCloud(width=1440, height=900).generate(analysisTxt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.interactive(False)
plt.show()