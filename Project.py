# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv(r"C:\Users\sunny\Desktop\Final Project\山佳\各月\C0A520-2017-01.csv", header =1)
data2 = pd.read_csv(r"C:\Users\sunny\Desktop\Final Project\山佳\各月\C0A520-2017-02.csv", header =1)

DailyTemperature1 = data1[["ObsTime","Temperature", "T Max", "T Min"]]


for i in range (1,3):
    test = [["ObsTime","Temperature", "T Max", "T Min"]]



print("data"+str(i))


#mean = DailyTemperature1.mean()