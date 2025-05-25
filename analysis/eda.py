import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, linregress, pearsonr


df.describe()
df.dtypes
df.shape

#histograms of rates
# easy win rate histogram
df['Easy Win Rate (%)'].hist(bins=10)
plt.title('Easy Win Rate Distribution')
plt.xlabel('Win Rate (%)')
plt.ylabel('Frequency')
plt.show()
plt.savefig("histogram_easy.png", dpi=300)

# hard win rate histogram
df['Hard Win Rate (%)'].hist(bins=10)
plt.title('Hard Win Rate Distribution')
plt.xlabel('Win Rate (%)')
plt.ylabel('Frequency')
plt.show()
plt.savefig("histogram_hard.png", dpi=300)

##boxplots of rates
plt.figure(figsize=(10, 6))
df.boxplot(column='Hard Time', showfliers=True)
plt.title('Hard Average Completion Time (Minutes) - Boxplot')
plt.xlabel('Hard Time (Minutes)')
plt.ylabel('Value')
plt.grid(True)
plt.savefig('outlier_hard.png', dpi=300)
plt.show()

def zamanduzelt(t):
    dk, sn = map(int, t.split(":"))  # ":" ile ayırıp sayılara dönüştür
    return dk + sn / 60  # dakika ve saniyeyi dakikaya çevir












