#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import definite_integral as di

# xの間隔
dx = 0.1

# 定積分でab区間
a = -np.pi/2
b = a*(-1)

# ab区間内の連続したxのリスト
if (a>b) :
    dx *= -1
x = np.array([dx * i for i in range(int((abs(a-b)+abs(dx))/abs(dx)))]) + a
# print(x)

# aからbまでの区間の関数の座標
# y = func_NumDivX(1,x)
y = np.cos(x)
print("x:"+str(x))
print("y:"+str(y))

# モンテカルロ法を用いて積分する(指定なしならN=10000)
sum_M = di.integral_MonteCarloRule(x,y)
# 台形公式を用いて積分する
sum_T = di.integral_TrapezoidalRule(x,y)
# シンプソンの公式を用いて積分する
sum_S = di.integral_SimpsonsRule(x,y)

print("モンテカルロ法:"+str(sum_M))
print("台形公式:"+str(sum_T))
print("シンプソンの公式:"+str(sum_S))
