import os
import re
import jieba
from jieba.analyse import *

def getStopwords():
    stopwords = []
    file = open('stopwords.txt', 'r', encoding='UTF-8')
    for line in file.readlines():
        stopwords.append(line[ : -1])

    return stopwords

stopFile = open('stopwords_candidate.txt', 'w', encoding='UTF-8')
postPath = '../../_posts/'
for file in os.listdir(postPath):
    content = ''
    frontMatter = ''
    frontMatterCount = 0
    filePath = postPath + file
    post = open(filePath, 'r', encoding='UTF-8')
    for line in post.readlines():
        if line[ : -1 ] == '---':
            frontMatterCount += 1
        else:
            if frontMatterCount != 2:
                frontMatter += line
            else:
                content += line
    content = content.replace(' ', '')
    pattern = re.compile('[^\u4e00-\u9fa5]')
    content = re.sub(pattern, '', content)
    cutWords = jieba.lcut(content)

    stopwords = getStopwords()
    words = ''
    for word in cutWords:
        if word not in stopwords:
            words += word + '/'

    keywords = jieba.analyse.extract_tags(words, topK = 30, withWeight = False, allowPOS=('n', 'nr', 'ns'))
    for key in keywords:
        stopFile.write(key + '\n')
    stopFile.write('\n')
