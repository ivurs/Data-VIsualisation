# -*- coding: utf-8 -*-
'''
Created on 2017��1��24��

@author: ZQZ
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
from matplotlib import ticker

df = pd.read_csv('#########.csv')


#change your columns' names
df = df[['1/sp|Q8IX12|CCAR1_HUMAN', '1/sp|P49773|HINT1_HUMAN', 
         '4/sp|P11142|HSP7C_HUMAN/sp|P54652|HSP72_HUMAN/sp|P34931|HS71L_HUMAN/sp|P11021|GRP78_HUMAN', 
         '1/sp|P62906|RL10A_HUMAN', 
         '2/sp|P08670|VIME_HUMAN/sp|P14136|GFAP_HUMAN', 'Tissue']]

df = df[(df['Tissue'] =='T') | (df['Tissue'] =='N')]
df = df.fillna(1)
df.columns = ['Q8IX12|CCAR1', 'P49773|HINT1', 
              'P11142|HSP7C','P62906|RL10A_HUMAN',
              'P08670|VIME', 'Tissue']

#Set bins
n_hist = 50
targets = "Tissue"
columns = ['Q8IX12|CCAR1', 'P49773|HINT1', 
           'P11142|HSP7C','P62906|RL10A_HUMAN',
           'P08670|VIME',]
min_sets = df[columns].values.min()
max_sets = df[columns].values.max()
hist_bins = np.linspace(min_sets, max_sets, n_hist)


# draw a frame work for all these correlation plots.
fig, axes = plt.subplots(nrows=len(columns), ncols=len(columns), 
                         sharex="col",figsize=(25,20))

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
            

# for each subplot, we draw it one by one.
for i,row in enumerate(columns):
    for j,col in enumerate(columns):
        ax= axes[i,j]
        # just show half of the correlation matrix as another half is the same thing, this line can be definately beautified.
        if [i,j] in [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]:
            ax.axis('off')
        else:
            min_current = df[col].values.min()
            max_current = df[col].values.max()
            if i == j:
                # diagonal
                hist_bins = np.linspace(min_current, max_current, n_hist)
                def hist(x):
                    h, e = np.histogram(x.dropna()[col], bins=hist_bins)
                    return pd.Series(h, e[:-1])
                b = df[[col,targets]].groupby(targets).apply(hist).T
                values = np.cumsum(b.values, axis=1)
                for k in range(len(b.columns)):
                    if k == 0:
                        ax_c_1= ax.bar(b.index, values[:,k], 
                                           width=np.diff(hist_bins)[0],
                                           linewidth=10, alpha=0.3)
                        print(b)
                    else:
                        ax_c_2= ax.bar(b.index, (values[:,k] - values[:,k-1]), 
                                           width=np.diff(hist_bins)[0],
                                           #bottom=values[:,k-1], 
                                           linewidth=10, alpha=0.2)
                        legend = ax.legend((ax_c_1,ax_c_2),('N','T'))
                    ax.set_xlabel(col)
                    ax.set_ylabel(row)
                    ax.xaxis.set_major_formatter(formatter)
            else:
                #offdiagonal
                for (n,cat) in df.groupby(targets):
                    ax.scatter(cat[col],cat[row], s = 25,label=n,alpha = 0.09)
                    ax.legend()
                    ax.set_xlabel(col)
                    ax.set_ylabel(row)
                    ax.yaxis.set_major_formatter(formatter)
                    ax.xaxis.set_major_formatter(formatter)
        #plt.yticks(np.arange(min_current, max_current, (max_current-min_current)/4))
        #ax.legend()



plt.tight_layout()

#plt.show() - if show fig first, then the content of fig will be release and thus no fig could be saved
#plt.savefig('tissue-T-N.eps', format='eps', dpi=1000)

