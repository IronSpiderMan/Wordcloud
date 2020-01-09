# 导入模块
from wordcloud import WordCloud
# 准备文本数据
sentence = "不要温顺的走进那个良夜"
# 创建词云对象
wc = WordCloud(font_path='msyh.ttc')
# 根据文本数据生成词云
wc.generate(sentence)
# 保存词云文件
wc.to_file("wc.png")