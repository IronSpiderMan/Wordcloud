import cv2
import jieba
from wordcloud import WordCloud,ImageColorGenerator

im = cv2.imread('1.jpg')
im_color = ImageColorGenerator(im)

f = open('csb.txt', 'r', encoding='utf8')
article = f.read()
words = jieba.cut(article)
text = " ".join(words)

wc = WordCloud(
    background_color='white',
    font_path='msyh.ttc',
    mask=im,

)

wc.generate(text)
wc.recolor(color_func=im_color)
wc.to_file('wc.png')