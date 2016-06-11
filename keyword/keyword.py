#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# jieba.load_userdict("userdict.txt")
import jieba.analyse
import codecs
from textrank4zh import TextRank4Keyword

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

class keyWordGenerator():
    @staticmethod
    def tfidf_keywords(text):
        # seg_list = jieba.cut(text, cut_all=True)
        seg_list = jieba.analyse.extract_tags(text, 20, True)  # 默认是精确模式
        for seg in seg_list:
        	print seg[0],seg[1]
        #return ";".join(seg_list)

    @staticmethod
    def jieba_textrank_keywords(text):
        # seg_list = jieba.cut(text, cut_all=True)
        seg_list = jieba.analyse.textrank(text, 20, True)  # 默认是精确模式

        for seg in seg_list:
        	print seg[0],seg[1]
        #return ";".join(seg_list)

    @staticmethod
    def textrank_keywords(text):
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=text,lower=True, window=3, pagerank_config={'alpha':0.85})

        seg_list = tr4w.get_keywords(20, word_min_len=2)
        for item in seg_list:
        	print item.word, item.weight

    @staticmethod
    def keywords(text):
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=text,lower=True, window=3, pagerank_config={'alpha':0.85})

        tf_list = jieba.analyse.extract_tags(text, 20, True) 
        jieba_rank_list = jieba.analyse.textrank(text, 20, True) 
        rank_list = tr4w.get_keywords(20, word_min_len=2)
        res = [x for x in tf_list for y in rank_list if x[0]==y.word]
        for seg in res:
        	print seg[0],seg[1]


text = codecs.open('../sample/doc/01.txt', 'r', 'utf-8').read()
print keyWordGenerator.tfidf_keywords(text)
print keyWordGenerator.textrank_keywords(text)
print keyWordGenerator.jieba_textrank_keywords(text)
print keyWordGenerator.keywords(text)