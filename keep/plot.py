import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
mpl.rcParams['axes.linewidth'] = 3.5

df = pd.read_csv("for_plot.txt", delim_whitespace=True, header=None)
print df[0], df[2]

plt.bar(df[0], df[2], color="black")
plt.tick_params(width=1.5, length=6, tick2On="on")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.grid(color='r', linestyle='-', linewidth=2)
plt.axhline(y=0, xmin=0, xmax=23, hold=None, color="black")

plt.tight_layout()
plt.show()
