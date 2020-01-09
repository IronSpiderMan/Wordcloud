from wordcloud import WordCloud
import cv2
# 打开文件
f = open('jobs.txt', 'r', encoding='utf8')
# 读取文件
article = f.read()
# 关闭文件
f.close()
# 读取图片
im = cv2.imread('1.jpg')
# 生成词云
wc = WordCloud(
    width=400,
    height=500,
    background_color='white',
    max_font_size=50,
    mask=im		# 设置mask属性，让词语按照im轮廓绘制词云（背景必须是全白的）
)
# 根据文本生成词云
wc.generate(article)
# 保存词云文件
wc.to_file('w2.png')