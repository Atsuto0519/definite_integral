#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import definite_integral as di

# xの間隔
dx = 0.001

# 定積分でab区間
a = 80
b = 1000

# ab区間内の連続したxのリスト
if (a>b) :
    dx *= -1
x = np.array([dx * i for i in range(int((abs(a-b)+abs(dx))/abs(dx)))]) + a
# print(x)

# aからbまでの区間の関数の座標
# y = func_NumDivX(1,x)
sigma = 10
ave = 50
y = 1/np.sqrt(2*np.pi*sigma*sigma) * np.exp(-np.power(x-ave,2)/(2*sigma*sigma))
print(y)

# 台形公式を用いて積分する
sum_T = di.integral_TrapezoidalRule(x,y)
# シンプソンの公式を用いて積分する
sum_S = di.integral_SimpsonsRule(x,y)

print("台形公式:"+str(sum_T))
print("シンプソンの公式:"+str(sum_S))
