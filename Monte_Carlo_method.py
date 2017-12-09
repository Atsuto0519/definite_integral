#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# モンテカルロ法を用いて円周率を求める

# 乱数を固定
np.random.seed(1)

# 単位円に乱数座標が入った回数
inside = 0

# 試行回数
iteration = 100000000

# 乱数配列を生成
rand_list1 = np.power(np.random.rand(iteration), 2)
rand_list2 = np.power(np.random.rand(iteration), 2)
rand_dist = rand_list1+rand_list2

for i in rand_dist :
    if (i < 1) :
        # 単位円内だったら
        inside+=1

# 円周率を求める
print("pi="+str(inside/iteration * 4))
