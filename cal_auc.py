""" AUC metric
    AUC is frequently used to evaluate machine learning models
    like logistic regression. Several methods are used to calculate it. 
    This one is simple and more understandable: The expectation that a
    uniformly drawn random positive is ranked before a uniformly drawn
    random negative.

    Since the code origins from evaluating click through rate prediction 
    model, we keep the variable name like pv_num and click_num, referring
    to the number of all instances and the positive.
"""

import sys
import os

def AUC(label, pred):
    pv_num = len(pred)
    click_num = 0.0
    area_num = 0.0
    list_eval = zip(label, pred)

    # sort by label
    list_eval = sorted(list_eval, key = lambda x : x[1], reverse = True)
    # sum up correct ordered pairs
    for i in range(len(list_eval)):
        area_num += click_num * (1 - list_eval[i][0])
        click_num += list_eval[i][0]

    auc = 0.0
    if pv_num == click_num:
        auc = 1
    elif click_num == 0:
        auc = 0
    else:
        auc = area_num / (pv_num - click_num) / click_num
    return (pv_num, click_num, auc)


if __name__ == "__main__":
    # reference label
    label = []
    # predicted result
    pred = []
   
    # read data from file
    # line format: index"\t"label"\t"predctedresult
    fin = open(sys.argv[1], "r")
    for line in fin:
        line = line.strip().split("\t")
        if len(line) != 4:
            continue
        label.append(float(line[2]))
        pred.append(float(line[3]))

    # calculate AUC
    pv_num, click_num, auc = AUC(label, pred)
    print pv_num, click_num, auc


