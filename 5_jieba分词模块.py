import jieba
# 准备分词的句子
sentence = "不要温顺的走进那个良夜"
# 默认采用精确模式分词
words = jieba.cut(sentence)
# 将分好的词用" "连接
text = " ".join(words)
# 输出
print(text)