# 20377056-曹云飞-第3周作业
from datetime import datetime
import csv
import re
import jieba
import math
import pandas as pd
import matplotlib.pyplot as plt
# 1.
def fc(filename):
    with open(filename, 'r', encoding='utf-8-sig', errors='ignore') as wb:
        wwb = csv.reader(wb)    # 创建csv 对象,它是一个包含所有数据的列表，每一行为一个元素
        nn = []
        for i in wwb:
            nn.append(i)
        location, text, user, wbtime = [], [], [], []
        for i in range(0,len(nn)):
            location.append(nn[i][0])
            text.append(nn[i][1])
            user.append(nn[i][2])
            wbtime.append(nn[i][3])
    return location, text, user, wbtime
# 1.
def delete(text):
    for i in range(0,len(text)):
        text[i] = re.sub(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", '', text[i])
    stopwords = [line.strip() for line in open('C:\Code\pythonProject\W03\stopwords_list.txt', 'r', encoding='utf-8-sig').readlines()]
    jieba.load_userdict(r'C:\Code\pythonProject\W03\emotion_lexicon\anger.txt')
    jieba.load_userdict(r'C:\Code\pythonProject\W03\emotion_lexicon\disgust.txt')
    jieba.load_userdict(r'C:\Code\pythonProject\W03\emotion_lexicon\fear.txt')
    jieba.load_userdict(r'C:\Code\pythonProject\W03\emotion_lexicon\joy.txt')
    jieba.load_userdict(r'C:\Code\pythonProject\W03\emotion_lexicon\sadness.txt')
    l = len(text)
    sentence=[]
    for i in range(0, l):
        sentence2=[]
        sentence1 = jieba.lcut(text[i])
        for word in sentence1:
            if word not in stopwords and word != ',' and word != ' ':
                sentence2.append(word)
        sentence.append(sentence2)
    return sentence

def emo(n_text):
    anger = [line.strip() for line in
                 open('C:\Code\pythonProject\W03\emotion_lexicon\\anger.txt', 'r', encoding='utf-8-sig').readlines()]
    dis = [line.strip() for line in
                 open('C:\Code\pythonProject\W03\emotion_lexicon\disgust.txt', 'r', encoding='utf-8-sig').readlines()]
    fear = [line.strip() for line in
                 open('C:\Code\pythonProject\W03\emotion_lexicon\\fear.txt', 'r', encoding='utf-8-sig').readlines()]
    joy = [line.strip() for line in
                 open('C:\Code\pythonProject\W03\emotion_lexicon\joy.txt', 'r', encoding='utf-8-sig').readlines()]
    sad = [line.strip() for line in
                 open('C:\Code\pythonProject\W03\emotion_lexicon\sadness.txt', 'r', encoding='utf-8-sig').readlines()]
    l = len(n_text)
    v = []
    vv = []
    for i in range(0, l):
        v0 = [0] * 5
        for word in n_text[i]:
            if word in anger:
                v0[0] += 1
            if word in dis:
                v0[1] += 1
            if word in fear:
                v0[2] += 1
            if word in joy:
                v0[3] += 1
            if word in sad:
                v0[4] += 1
        vv.append(v0)
        k = v0.index(max(v0))
        if v0[k] == 0:
            v.append(0)
        else:
            v.append(k+1)
    return v, vv

def timese(vv, wbtime):
    n = pd.to_datetime(wbtime)

def space(location,vv):
    beijing=[39.5420,116.2529]
    list=[]
    for i in range(0,len(location)):
        num= location[i].strip('[]').split(',')
        num=[float(j) for j in num]
        list.append(num)
    dis=[]
    for i in range(0,len(location)):
        d1=list[i][0]-beijing[0]
        d2=list[i][1]-beijing[1]
        d=math.sqrt(pow(d1,2)+pow(d2,2))
        dis.append(d)
    a, d, f, j, s = [], [], [], [], []
    for i in range(0,len(vv)):
        if sum(vv[i]) != 0:
            a.append(float(vv[i][0]/sum(vv[i])))
            d.append(float(vv[i][1] / sum(vv[i])))
            f.append(float(vv[i][2] / sum(vv[i])))
            j.append(float(vv[i][3] / sum(vv[i])))
            s.append(float(vv[i][4] / sum(vv[i])))
        else:
            a.append(0)
            d.append(0)
            f.append(0)
            j.append(0)
            s.append(0)
    plt.plot(dis, a, dis, f, dis, d, dis, s, dis, j)
    plt.show()

if __name__=='__main__':
    location, text, user, wbtime = fc('C:\Code\pythonProject\W03\wb.csv')
    n_text = delete(text)   #分词并过滤停用词后得到的新二维列表
    v, vv = emo(n_text)
    #ime = timese(vv, wbtime)
    space(location,vv)

