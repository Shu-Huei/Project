# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:33:49 2022

@author: sunny
"""

import glob
import pandas as pd

path =r"C:\Users\sunny\Desktop\Final Project\山佳\各月"# use your path

filenames = glob.glob(path + "/*.csv")
count_files = 0
dfs = []
for filename in filenames:
    if count_files ==0:
        dfs.append(pd.read_csv(filename, sep=";")) 
        count_files += 1
    else:
        dfs.append(pd.read_csv(filename, sep=";", skiprows=[0]))
        count_files +=1

big_frame = pd.concat(dfs, ignore_index=True,axis=1)
