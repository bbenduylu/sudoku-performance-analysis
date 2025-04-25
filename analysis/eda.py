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

##boxplot for tamamlama süreleri
def zamanduzelt(t):
    dk, sn = map(int, t.split(":"))  # ":" ile ayırıp sayılara dönüştür
    return dk + sn / 60  # dakika ve saniyeyi dakikaya çevir

df['Kolay Süre'] = df['Kolay Ortalama Tamamlama Süresi (dakika)'].apply(zamanduzelt)
plt.figure(figsize=(10, 6))
df.boxplot(column='Kolay Süre', showfliers=True)
plt.title('Kolay Ortalama Tamamlama Süresi (Dakika) Boxplot')
plt.xlabel('Kolay Süre (Dakika)')
plt.ylabel('Frekans')
plt.grid(True)
plt.savefig('boxplot_easy_time_corrected.png', dpi=300)
plt.show()

df['Zor Süre'] = df['Zor Ortalama Tamamlama Süresi (dakika)'].apply(zamanduzelt)
plt.figure(figsize=(10, 6))
df.boxplot(column='Zor Süre', showfliers=True)
plt.title('Zor Ortalama Tamamlama Süresi (Dakika) Boxplot')
plt.xlabel('Zor Süre (Dakika)')
plt.ylabel('Frekans')
plt.grid(True)
plt.savefig('outlier_hard.png', dpi=300)
plt.show()










