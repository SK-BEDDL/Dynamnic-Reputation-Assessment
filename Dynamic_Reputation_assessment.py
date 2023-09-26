# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:46:12 2023

@author: skhan
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
n_user = 10
reputation_history =[]
reputation = np.array([0.5]*10)
reputation_history.append(np.copy(reputation))


#%%
print(reputation_history)

def Reputation_assessment(tmp_report, score_metrics):
    punishment = 1
    for id, malicious in enumerate(tmp_report):
        if malicious == 1:
            for results in score_metrics:
                mean = np.mean(results)
                value = results[id]
                tmp_punishment = value/mean
                if punishment > tmp_punishment:
                    punishment = tmp_punishment


    for id, malicious in enumerate(tmp_report):
        if malicious == 0:
            reputation[id] = min(1, reputation[id] + 0.1)
        else:
            reputation[id] = reputation[id] * punishment

    return reputation

for i in range(15):
    Reputation_assessment([0]*n_user,[])
    reputation_history.append(np.copy(reputation))
#%%
print(reputation_history)

reputation_history0_1 = reputation_history.copy()
reputation_history0_2 = reputation_history.copy()

for _ in range(4):
    tmp_rep = np.copy(reputation_history0_1[-1])
    tmp_rep[2] = tmp_rep[4] = max(0,tmp_rep[2] - 0.1)
    reputation_history0_1.append(tmp_rep)

    tmp_rep = np.copy(reputation_history0_2[-1])
    tmp_rep[2] = tmp_rep[4] = max(0,tmp_rep[2] - 0.2)
    reputation_history0_2.append(tmp_rep)
    
#%%
print(reputation_history0_1)
print(reputation_history0_2)

malicious_report =  np.zeros((n_user,))

for report in [[3,5]*8,[]*2]:
    for id in report:
        malicious_report[id -1] += 1

malicious_report = malicious_report/n_user

print(malicious_report)

malicious_report = np.where(malicious_report > 0.5, 1, 0)

print(malicious_report)

# Sample User Data
user1 = [
    [
        0.31185714285714283,
        0.31442857142857145,
        0.19171428571428573,
        0.31214285714285717,
        0.19057142857142856,
        0.3117142857142857,
        0.30957142857142855,
        0.3167142857142857,
        0.31585714285714284,
        0.31357142857142856,
    ],
    [
        0.1742857142857143,
        0.17642857142857143,
        0.12085714285714286,
        0.17657142857142857,
        0.12385714285714286,
        0.17285714285714285,
        0.17385714285714285,
        0.17757142857142857,
        0.179,
        0.181,
    ]
]

# add users data to each users
# user2, user3, user4..............


score_metrics = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10]

#%%

for i in range(2):
    round_metric = []
    for j in range(n_user):
        round_metric.append(score_metrics[j][i])
    Reputation_assessment(malicious_report,round_metric)
    print(reputation)
    reputation_history.append(np.copy(reputation))
    
print(reputation_history)


#%%

