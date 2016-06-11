#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import MySQLdb.cursors
import math


'''
    A basic Mysql Manaher
'''
class SQLDBManager(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            db='media_center',
            user='root',
            passwd='root',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        self.cursor = self.conn.cursor()
    
    def execute(self , sql):
        self.cursor.execute(sql)
    
    def insert_id(self):
        return self.conn.insert_id()

    def commit(self):
        return self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()
    
    def fetchall(self):
        return self.cursor.fetchall()

    def format(self, text):
        return self.conn.escape_string(str(text))
    
    
    def get_matrix(self):
        sql_keyword = "SELECT * FROM keyword"
        self.execute(sql_keyword)
        res_kws = self.fetchall()
        keyword_cnt = len(res_kws)

        sql_category = "SELECT * FROM category"
        self.execute(sql_category)
        res_cat = self.fetchall()
        matrix = dict()
        for e1 in res_cat:
            matrix[e1['category']] = dict()
        
        sql_keyword_category = "SELECT * FROM keyword_category"
        self.execute(sql_keyword_category)
        result = self.fetchall()
        for e in result:
            matrix[e['category']][e['keyword']] = e['probability']
        return matrix, keyword_cnt

    def get_category_probability(self, category, keywords):
        matrix = self.get_matrix()[0]
        keyword_cnt = self.get_matrix()[1]
        
        proba = float(0);
        for keyword in keywords:
            if keyword in matrix[category]:
                p = matrix[category][keyword]
            else:
                p = float(1) / keyword_cnt
            proba += math.log(p, 2)
        return proba

db = SQLDBManager()
category = "sport"
keywords = ["nba", "cba", "xxx"]
print db.get_category_probability(category, keywords)
