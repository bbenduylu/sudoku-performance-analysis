import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, linregress, pearsonr

df= pd.read_csv('sudoku_performance.csv')
df['Kolay Kazanma Oranı (%)'].hist(bins=10)
plt.title('Easy Win Rate Distribution')
plt.xlabel('Win Rate')
plt.ylabel('Frequency')
plt.show()
