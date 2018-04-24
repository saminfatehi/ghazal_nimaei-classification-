# -*- coding: utf-8 -*-

import subprocess

subprocess.call("vw -d vwFile.txt --loss_function logistic --ngram 1  -f  predictor.vw", shell=True)
subprocess.call("vw -d vwFile_test.txt -t -i predictor.vw -p predictions.txt", shell=True)

file1 = open("predictions.txt", 'r',)
file2 = open("vwFile_test.txt", 'r',)

FP1 = 0
TP1 = 0
FN1 = 0
TN1 = 0

for pre, test in zip(file1, file2):
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) > 0:
        TP1 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) > 0:
        FP1 += 1
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) < 0:
        FN1 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) < 0:
        TN1 += 1

precision1 = TP1/(TP1+FP1)
recall1 = TP1/(TP1+FN1)

print(precision1)
print(recall1)

file1.close()
file2.close()


subprocess.call("vw -d vwFile.txt --loss_function logistic --ngram 2  -f  predictor.vw", shell=True)
subprocess.call("vw -d vwFile_test.txt -t -i predictor.vw -p predictions2.txt", shell=True)

file1 = open("predictions2.txt", 'r',)
file2 = open("vwFile_test.txt", 'r',)

FP2 = 0
TP2 = 0
FN2 = 0
TN2 = 0

for pre, test in zip(file1, file2):
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) > 0:
        TP2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) > 0:
        FP2 += 1
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) < 0:
        FN2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) < 0:
        TN2 += 1

precision2 = TP2/(TP2+FP2)
recall2 = TP2/(TP2+FN2)

print(precision2)
print(recall2)


file1.close()
file2.close()


subprocess.call("vw -d vwFile.txt --loss_function logistic --ngram 3  -f  predictor.vw", shell=True)
subprocess.call("vw -d vwFile_test.txt -t -i predictor.vw -p predictions3.txt", shell=True)

file1 = open("predictions3.txt", 'r',)
file2 = open("vwFile_test.txt", 'r',)

FP2 = 0
TP2 = 0
FN2 = 0
TN2 = 0

for pre, test in zip(file1, file2):
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) > 0:
        TP2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) > 0:
        FP2 += 1
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) < 0:
        FN2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) < 0:
        TN2 += 1

precision3 = TP2/(TP2+FP2)
recall3 = TP2/(TP2+FN2)

print(precision3)
print(recall3)


file1.close()
file2.close()


subprocess.call("vw -d vwFile.txt --loss_function logistic --ngram 4  -f  predictor.vw", shell=True)
subprocess.call("vw -d vwFile_test.txt -t -i predictor.vw -p predictions4.txt", shell=True)

file1 = open("predictions4.txt", 'r',)
file2 = open("vwFile_test.txt", 'r',)

FP2 = 0
TP2 = 0
FN2 = 0
TN2 = 0

for pre, test in zip(file1, file2):
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) > 0:
        TP2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) > 0:
        FP2 += 1
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) < 0:
        FN2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) < 0:
        TN2 += 1

precision4 = TP2/(TP2+FP2)
recall4 = TP2/(TP2+FN2)

print(precision4)
print(recall4)


file1.close()
file2.close()


subprocess.call("vw -d vwFile.txt --loss_function logistic --ngram 5  -f  predictor.vw", shell=True)
subprocess.call("vw -d vwFile_test.txt -t -i predictor.vw -p predictions5.txt", shell=True)

file1 = open("predictions5.txt", 'r',)
file2 = open("vwFile_test.txt", 'r',)

FP2 = 0
TP2 = 0
FN2 = 0
TN2 = 0

for pre, test in zip(file1, file2):
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) > 0:
        TP2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) > 0:
        FP2 += 1
    if int(test.split("|")[0]) == 1 and float(pre.split("\n")[0]) < 0:
        FN2 += 1
    if int(test.split("|")[0]) == -1 and float(pre.split("\n")[0]) < 0:
        TN2 += 1

precision5 = TP2/(TP2+FP2)
recall5 = TP2/(TP2+FN2)

print(precision5)
print(recall5)

file1.close()
file2.close()
