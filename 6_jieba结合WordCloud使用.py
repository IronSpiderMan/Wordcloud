import jieba
from wordcloud import WordCloud

sentence = "不要温顺的走进那个良夜"

wc = WordCloud(font_path='msyh.ttc')

words = jieba.cut(sentence)

text = " ".join(words)

wc.generate(text)

wc.to_file('wc.png')