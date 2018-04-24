# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from collections import Counter
import re
from hazm import *
import math

prob_dict1 = {}
prob_dict2 = {}

TP = 0
TN = 0
FP = 0
FN = 0

file1 = open("nimaei_b.txt",'r')
file2 = open("ghazal_b.txt",'r')
file1_test = open("nimaei_b_test.txt",'r')
file2_test = open("ghazal_b_test.txt",'r')

text1 = file1.read()
text2 = file2.read()
text1_tokens = word_tokenize(text1)
text2_tokens = word_tokenize(text2)
l1 = len(text1_tokens)
l2 = len(text2_tokens)

unique_words1 = Counter(text1.split())
unique_words2 = Counter(text2.split())

for token in unique_words1:
    count1 = unique_words1.get(token)
    if count1 != None:
        prob_dict1[token] = math.log((count1+1)/(l1+len(unique_words1)))

for token in unique_words2:
    count2 = unique_words2.get(token)
    if count2 != None:
        prob_dict2[token] = math.log((count2+1)/(l2+len(unique_words2)))

for line in file1_test:
    tokens = word_tokenize(line.split("\n")[0])
    p1 = 0
    p2 = 0
    for i in tokens:
        if i in prob_dict1:
            p1 += prob_dict1[i]
        else:
            p1 += math.log(1/(l1+len(unique_words1)))

        if i in prob_dict2:
            p2 += prob_dict2[i]
        else:
            p2 += math.log(1/(l1 + len(unique_words2)))

    c1 = p1+ math.log(l1/(l1+l2))
    c2 = p2+ math.log(l2/(l2+l1))
    if c1 > c2:
        TP += 1
    else:
        FN += 1

for line in file2_test:
    tokens = word_tokenize(line.split("\n")[0])
    p1 = 0
    p2 = 0

    for i in tokens:
        if i in prob_dict1:
            p1 += prob_dict1[i]
        else:
            p1 += math.log(1 / (l1 + len(unique_words1)))

        if i in prob_dict2:
            p2 += prob_dict2[i]
        else:
            p2 += math.log(1 / (l1 + len(unique_words2)))

    c1 = p1+ math.log(l1/(l1+l2))
    c2 = p2+ math.log(l2/(l2+l1))
    if c1 < c2:
        TN += 1
    else:
        FP += 1

file1.close()
file2.close()
file1_test.close()
file2_test.close()

precision = TP/(TP+FP)
recall = TP/(TP+FN)

print("precision : ")
print(precision)
print("recall : ")
print(recall)




