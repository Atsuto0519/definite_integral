#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# 関数
# y = num / x
def func_NumDivX(num, x) :
    res = num/np.array(x)
    if (len(res) == 1) :
        res = res[0]
    return res

# リストからある値に最も近い値のindexを返却する関数
def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    return np.abs(np.asarray(list) - num).argmin()

# モンテカルロ法を用いて積分する(指定なしならN=10000)
def integral_MonteCarloRule(x,y,*,N=10000) :
    max_x = max(x)
    min_x = min(x)
    min_y = min(y)
    scale = abs(max_x) + abs(min_x)

    # aからbまでの範囲の正方形内にランダムに点を取る
    # (正方形のy座標はyの最小値に底辺を合わせる)
    rand_x = np.random.rand(N) * scale + min_x
    rand_y = np.random.rand(N) * scale + min_y

    # 正方形の中に乱数が入っているかカウントする
    count = 0
    for (x_i,y_i) in zip(rand_x,rand_y) :
        near_inx = getNearestValue(x,x_i)
        # 乱数が最も近い座標が関数内かどうか
        if (y[near_inx] >= y_i) :
            count+=1

    # (正方形の面積)*(入った数)/(乱数点の数)
    return scale*scale*count/N

# 台形公式を用いて積分する
def integral_TrapezoidalRule(x,y) :
    dx = x[1] - x[0]

    res = 2*sum(y) - y[0] - y[-1]
    return dx*res/2

# シンプソンの公式を用いて積分する
def integral_SimpsonsRule(x,y) :
    h = x[1] - x[0]
    res = 0

    if (len(x) == len(y)):
        for i in range(len(y)-2) :
            res += 2 * ((i+1)%2+1) * y[i+1]
        res = h/3 * (res + y[0] + y[-1])

    else :
        print("Error.")

    return res
