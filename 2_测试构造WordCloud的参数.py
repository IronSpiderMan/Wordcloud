# 导入模块
from wordcloud import WordCloud
# 准备文本数据
sentence = "He had already passed sixty of the stages leading to it, and he had brought from his journey nothing but errors and remorse. Now his health was poor, his mind vacant, his heart sorrowful, and his old age short of comforts."
# 准备禁用词，需要为set类型
stopwords = set(['go', 'to'])
# 设置参数，创建WordCloud对象
wc = WordCloud(
    width=200,					# 设置宽为400px
    height=150,					# 设置高为300px
    background_color='white',	 # 设置背景颜色为白色
    stopwords=stopwords,		 # 设置禁用词，在生成的词云中不会出现set集合中的词
    max_font_size=100,			 # 设置最大的字体大小，所有词都不会超过100px
    min_font_size=10,			 # 设置最小的字体大小，所有词都不会超过10px
    max_words=10,				 # 设置最大的单词个数
    scale=2						# 扩大两倍
)
# 根据文本数据生成词云
wc.generate(sentence)
# 保存词云文件
wc.to_file('wc.png')