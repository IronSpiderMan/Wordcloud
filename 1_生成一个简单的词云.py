# 导入模块
from wordcloud import WordCloud
# 准备文本数据
sentence = "Do not go gentle into that good night!"
# 创建词云对象
wc = WordCloud()
# 根据文本数据生成词云
wc.generate(sentence)
# 保存词云文件
wc.to_file("wc.png")    