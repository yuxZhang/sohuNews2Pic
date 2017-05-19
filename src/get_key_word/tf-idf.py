#!/usr/bin/python
# coding:utf-8
__author__ = '353677403@qq.com'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from collections import defaultdict

class Tfidf(object):
    def __init__(self, idf_file, txt_dir, mode=1):
        if mode == 1:
            self.idf_dict = dict()
            with open(idf_file) as fi:
                for line in fi:
                    word, idf_value = line.decode('utf-8').strip().split('\t')
                    self.idf_dict[word] = idf_value
        else:
            pass




    def tfidf(document, window=6):
        """function: ues textrank algorithm to find key words of web news.

        Args:
            document: (list of lists) News contend.
            window: (int) Window size

        Return:
            word_dict: (dict) Words and weights
        """
        word_dict = defaultdict(lambda: 0.0)
        sum = 0.0
        for line in document:
            for word in line:
                word_dict[word] += 1.0

        for word in word_dict:
            pass
        return word_dict
