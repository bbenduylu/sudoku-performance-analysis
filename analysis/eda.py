import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, linregress, pearsonr


df.describe()
df.dtypes
df.shape

#histograms of rates
df= pd.read_csv('sudoku_performance.csv')
df['Kolay Kazanma Oranı (%)'].hist(bins=10)
plt.title('Easy Win Rate Distribution')
plt.xlabel('Win Rate')
plt.ylabel('Frequency')
plt.show()
plt.savefig("histogram_easy.png", dpi=300)

df= pd.read_csv('sudoku_performance.csv')
df['Zor Kazanma Oranı (%)'].hist(bins=10)
plt.title('Hard Win Rate Distribution')
plt.xlabel('Win Rate')
plt.ylabel('Frequency')
plt.show()
plt.savefig("histogram_hard.png", dpi=300)

##boxplots of rates
df.boxplot(column='Kolay Kazanma Oranı (%)')
plt.show()
plt.savefig("boxplot_easy.png", dpi=300)

df.boxplot(column='Zor Kazanma Oranı (%)')
plt.show()
plt.savefig("boxplot_hard.png", dpi=300)








