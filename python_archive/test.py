#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    python ==> dyros, [x,y,z,intensity] 필드를 가지고 있는 veloydne_point cloud 데이터를 numpy, pandas로 가공해본
'''

import numpy as np
import pandas as pd


data = open('velodyne_points.dat', 'r').read().split('\n')

# ed: create (0,0,0,0)
data_np = np.zeros(4)

for i in range(0, 10000):
    data_np = np.vstack((data_np, data[i].split(', ')))

    if(i % 2000 == 0):
        print(i)


# ed: remove first zeros (0,0,0,0)
data_np = data_np[1:len(data_np)].astype(np.float)

data_pd = pd.DataFrame(data=data_np)


data_pd.info()
data_pd.hist()
data_pd.sum()
data_pd.describe()


#-------------------------------------------------------------

data2 = open('Grid_JW_1.txt', 'r').read().split('\n')

# ed: create (0,0,0,0)
data_np2 = np.zeros(8)

for i in range(0, 10000):
    data_np2 = np.vstack((data_np2, data2[i].split(', ')))

    if(i % 2000 == 0):
        print(i)


# ed: remove first zeros (0,0,0,0)
data_np2 = data_np2[1:len(data_np2)].astype(np.float)

data_pd2 = pd.DataFrame(data=data_np2)


data_pd2.info()
data_pd2.hist()
data_pd2.sum()
data_pd2.describe()



#-------------

x=[
57,
52,
48,
43,
43,
44,
44,
42,
45,
46,
48,
50,
51,
53,
55
]

u=[
0.877,
0.913,
0.930,
0.947,
0.947,
0.947,
0.930,
0.913,
0.895,
0.877,
0.849,
0.830,
0.811,
0.780,
0.770
]

u2=[
1.346,
1.421,
1.454,
1.471,
1.471,
1.465,
1.443,
1.404,
1.363,
1.340,
1.303,
1.266,
1.240,
1.214,
1.187
        ]


case1_u = [
0.927,
0.965,
0.983,
1.001,
1.001,
1.001,
0.983,
0.965,
0.946,
0.927,
0.898,
0.877,
0.857,
0.825,
0.814
        ]

case1_b=[
0.772,
0.846,
0.917,
1.023,
1.023,
1.000,
1.000,
1.048,
0.978,
0.957,
0.917,
0.880,
0.863,
0.830,
0.800
        ]


case2_u =[
0.918,
0.970,
0.993,
1.004,
1.004,
1.000,
0.985,
0.958,
0.930,
0.914,
0.889,
0.864,
0.846,
0.829,
0.810
        
        ]


case2_b=[
0.772,
0.846,
0.917,
1.023,
1.023,
1.000,
1.000,
1.048,
0.978,
0.957,
0.917,
0.880,
0.863,
0.830,
0.800
        ]



case1_err=[
20.098,
14.037,
7.27,
2.14,
2.14,
0.135,
1.669,
7.893,
3.231,
3.079,
2.076,
0.289,
0.688,
0.641,
1.743
        ]

case2_err=[
18.962,
14.6,
8.274,
1.909,
1.909,
0,
1.504,
8.547,
4.844,
4.421,
2.974,
1.833,
1.893,
0.192,
1.298
        ]






