# english version
from textblob import TextBlob
text = "I am happy today. I feel sad today."
analysisRet = TextBlob(text)
for sentence in analysisRet.sentences :
  print(sentence, sentence.sentiment);
print(analysisRet, analysisRet.sentiment)

# chinese version
from snownlp import SnowNLP
text_cn = u"我今天很快乐。我今天很愤怒。"
analysisRet_cn = SnowNLP(text_cn)
# each statement's analysis
for sentence in analysisRet_cn.sentences:
  print(sentence, SnowNLP(sentence).sentiments)
# integral analysis
print(analysisRet_cn.sentences, analysisRet_cn.sentiments)