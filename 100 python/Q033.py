# Q033
# Created by JKChang
# 28/04/2017, 13:58
# Tag: dictionary initialization
# Description: Define a function which can print a dictionary where the keys are numbers between 1 and 3
#              (both included) and the values are square of keys.

def creatDict(num):
    d = {}
    for i in range(1, num + 1):
       d[i] = i **2

    return d

# print creatDict(5)
