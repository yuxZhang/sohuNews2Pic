#!/usr/bin/python
# coding:utf-8
# auther: zhangyuxiang
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from collections import defaultdict


def textRank(document, window=6):
    word_dict = defaultdict(lambda :1.0)
    d = 0.85
    for line in document:
        for i in range(0, max(len(line) - window + 1, 1)):
            window_dict = dict([[x, word_dict[x]] for x in line[i: min(i + window, len(line))]])
            win_num = len(window_dict)
            if win_num > 1:
                for wi in window_dict:
                    delta = 0
                    for wj in window_dict:
                        if wi != wj:
                            delta = delta + word_dict[wj]
                    window_dict[wi] = (1 - d) + d * delta / (win_num - 1)
                for wi in window_dict:
                    word_dict[wi] = window_dict[wi]
    return word_dict


