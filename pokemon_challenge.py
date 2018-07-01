import pandas as pd # data processing, csv file I/O(e.g pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns # visulization tool
data = pd.read_csv("pokemon.csv")
data.info()
data_cor = data.corr()
print(data_cor)
# correlation map
f,ax = plt.subplots(figsize = (10, 10))
sns.heatmap(data_cor, annot = True, linewidths = .5, cbar = True, fmt = '.1f', ax = ax)
plt.show()
data_head = data.head(10)
print(data_head)
data_col = data.columns
print(data_col)
# Line Plot
# color = color, lable = lable, linewidth = width of line, alpha = opacity, grid = True, linestyle = style of line
data.Speed.plot(kind = 'line', color = 'g', label = 'speed', linewidth = 1, alpha = 0.5, grid = True, linestyle = ':')
data.Defense.plot(color = 'r', label = 'Defense', linewidth = 1, alpha = 0.5, grid = True, linestyle = '-.')
# legend = puts lable into plot
plt.legend(loc = 'upper right')
# lable = name of lable
plt.xlabel('x axis')
plt.ylabel('y axis')
# title = title of plot
plt.title('Line Plot')
plt.show()
# Scatter Plot
# x = attack, y= defense
data.plot(kind = 'scatter', x = 'Attack', y = 'Defense', alpha = 0.5, color = 'red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Vs Defense Scatter Plot')
plt.show()
# Histogram
# bins = number of bars in figure
data.Speed.plot(kind = 'hist', bins = 50, figsize = (12, 12))
plt.show()
