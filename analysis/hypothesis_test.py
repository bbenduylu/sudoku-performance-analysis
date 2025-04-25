import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, linregress, pearsonr

df= pd.read_csv("../data/sudoku_performance.csv")
df["Gün"] = range(1, len(df)+1)

def zamanduzelt(t):
  dk, sn = map(int, t.split(":"))
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


#hypothesis 2--- win rates over time

slope_easy, intercept_easy, r_value_easy,p_value_easy, std_err_easy = linregress(df["Gün"], df["Kolay Kazanma Oranı (%)"])
slope_hard,intercept_hard, r_value_hard,p_value_hard, std_err_hard= linregress(df["Gün"], df["Zor Kazanma Oranı (%)"])

print("\nHypothesis 2 - Trend Analysis of Win Rates Over Time")

print("Easy Level → slope: "+ str(round(slope_easy,3)) +" → p-value: "+ str(round(p_value_easy, 5)))
if p_value_easy < 0.05:
    print("Conclusion (Easy): There is a statistically significant increasing trend in win rate over time.")
else:
    print("Conclusion (Easy): No significant trend detected over time.")

print("Hard Level → slope: " +str(round(slope_hard,3))+ " → p-value: "+ str(round(p_value_hard,5)))
if p_value_hard < 0.05:
    print("Conclusion (Hard): There is a statistically significant increasing trend in win rate over time.")
else:
    print("Conclusion (Hard): No significant trend detected over time.")

#hypothesis 3----- corr. between average time and win rate

corr_easy, p_easy = pearsonr(df["Kolay Süre"], df["Kolay Kazanma Oranı (%)"])
corr_hard, p_hard = pearsonr(df["Zor Süre"], df["Zor Kazanma Oranı (%)"])

print("\nHypothesis 3 - Correlation Between Completion Time and Win Rate")

print("Easy Level → correlation: " + str(round(corr_easy,3)) +" → p-value: " + str(round(p_easy,5)))
if p_easy < 0.05:
    print("Conclusion (Easy): There is a statistically significant relationship between completion time and win rate.")
else:
    print("Conclusion (Easy): No significant relationship detected.")

print("Hard Level → correlation: " + str(round(corr_hard,3)) +" → p-value: " + str(round(p_hard,5)))
if p_hard < 0.05:
    print("Conclusion (Hard): There is a statistically significant relationship between completion time and win rate.")
else:
    print("Conclusion (Hard): No significant relationship detected.")
