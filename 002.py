# 20377056-曹云飞-第2周作业
import csv
import jieba
from collections import Counter
import random
import numpy as np
np.seterr(divide='ignore',invalid='ignore')
import wordcloud as ww
import matplotlib.pyplot as plt
from cv2 import imread

# 1.读入danmuku.csv弹幕文件，,并将分词后的存入words
def fc(filename):
    with open(filename, 'r', encoding='utf-8') as dm:
        dmm = csv.reader(dm)    # 创建csv 对象,它是一个包含所有数据的列表，每一行为一个元素
        data = [row[0] for row in dmm]
    data = data[5555:15555]
    l = len(data)
    words = []
    for i in range(0, l):
        sentence = jieba.lcut(data[i])
        ll = len(sentence)
        for j in range(0, ll):
            words.append(sentence[j])
    return words, data

# 2.过滤词
def delete(words):
    stopwords = [line.strip() for line in open('C:\Code\pythonProject\stopwords_list.txt', 'r', encoding='utf-8-sig').readlines()]
    n_words = []
    for word in words:
        if word not in stopwords:
            n_words.append(word)
    return n_words

# 2.统计词频
# 3.保留特征集
def countw(n_words):
    c = Counter()
    for x in n_words:  # 进行词频统计
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    transfer = {}
    for i in c:
        transfer[i]= c[i]
    for i in transfer:
        if c[i] < 10:
            del c[i]
    return c

# 4.特征向量
def vector(f_words, data):
    f_key = list(f_words.keys())
    vectorlen,vectoramount=len(f_words), len(data)
    data_vector = {}
    for i in data:
        pervector = [0]*vectorlen
        for j in range(0,vectorlen):
            if f_key[j] in i:
                pervector[j] = f_words[f_key[j]]
        data_vector[i] = pervector
    return data_vector

# 5.相似度
def similarity(vectors):
    x = random.randint(0, len(vectors))
    items = list(vectors.keys())
    s = items[x]
    ch = vectors[s]
    re = {}
    print('选取弹幕：'+ s )
    for i in items:
        v = vectors[i]
        a = np.array(v)
        b = np.array(ch)
        dist = np.linalg.norm(a - b)
        re[i] = dist
    re = sorted(re.items(), key=lambda d: d[1], reverse=False)
    print('\n距离小对应弹幕：' + re[0][0] + '\n' + re[1][0] + '\n' + re[2][0] + '\n' + re[3][0] + '\n' + re[4][0])
    print('\n距离大对应弹幕：' + re[-1][0] + '\n' + re[-2][0] + '\n' + re[-3][0] + '\n' + re[-4][0] + '\n' + re[-5][0])
    return re

# 6.词云
def cloud(ctop):
    ms = imread('C:\Code\pythonProject\sss.png')
    wcp=ww.WordCloud(background_color="white",
                     font_path='simhei.ttf',
                     mask=ms)
    wordd=list(ctop.keys())
    wordddd=[]
    for i in range(0, 66): wordddd.append(wordd[i])
    strtoshow = ' '.join(wordddd)
    wcp.generate(strtoshow)
    wcp.to_file("wordcloudpicture.png")
    plt.show()

if __name__ == '__main__':
    words, data = fc('C:\Code\pythonProject\danmuku.csv')
    n_words = delete(words)
    f_words = countw(n_words)
    vectors = vector(f_words, data)
    l = similarity(vectors)
    cloud(f_words)
