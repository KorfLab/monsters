import sys
import os
import json
import numpy as np
import scipy.stats as st

scores  = {}
lengths = [50, 100, 150, 200, 250]
dir = sys.argv[1]
for rep in os.listdir(dir):
    length = int(rep.split('_')[1])
    if length not in lengths: continue
    with open(f'{dir}/{rep}/ranking_debug.json') as fh:
        ranking = json.load(fh)
        high = ranking['order'][0]
        plddt = ranking['plddts'][high]
        if length not in scores: scores[length] = []
        scores[length].append(plddt)

for length in lengths:
    plddts = scores[length]
    # using t distribution
    t_int = st.t.interval(alpha=0.95, df=len(plddts)-1, loc=np.mean(plddts), scale=st.sem(plddts)) 
    print(length)
    print(t_int)
    # using normal distribution
    # n_int = st.norm.interval(alpha=0.95, loc=np.mean(plddts), scale=st.sem(plddts)) 
    # print(n_int)