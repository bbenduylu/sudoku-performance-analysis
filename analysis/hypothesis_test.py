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

#hypothesis 1--- comp. of easy and hard rates
easywrates= df["Kolay Kazanma Oranı (%)"]
hardwrates=df["Zor Kazanma Oranı (%)"]

#t-test
t_num, p_value = ttest_ind(easywrates, hardwrates, equal_var=False)

print("Hypothesis 1 - Easy vs Hard Win Rate Comparison")
print("t statistic: " + str(round(t_num, 3)))
print("p-value: " + str(round(p_value,5)))

if p_value<0.05:
  print("Conclusion: There is a statistically significant difference between the win rates (reject H0).")
else:
    print("Conclusion: No statistically significant difference found (fail to reject H0).")

                         
