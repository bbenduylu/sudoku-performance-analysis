import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats import ttest_ind, linregress, pearsonr

df= pd.read_csv("../data/sudoku_performance.csv")
df["Gün"] = range(1, len(df)+1)

def zamanduzelt(t):
  dk, sn = map(int, t_str.split(":"))
  return dk + sn/60

df["Kolay Süre"]= df["Kolay Ortalama Tamamlama Süresi (dakika)"].apply(zamanduzelt)
df["Zor Süre"] = df["Zor Ortalama Tamamlama Süresi (dakika)"].apply(time_to_float)
