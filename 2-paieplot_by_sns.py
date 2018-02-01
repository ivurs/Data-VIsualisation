# -*- coding: utf-8 -*-
'''
Created on 2017��1��24��

@author: ZQZ
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('#########.csv')

#deal with your dataframe.
df = df[['1/sp|P60903|S10AA_HUMAN', '1/sp|Q14974|IMB1_HUMAN', 
         '2/sp|Q13404|UB2V1_HUMAN/sp|Q15819|UB2V2_HUMAN', 
         '1/sp|P60981|DEST_HUMAN', '1/sp|P10809|CH60_HUMAN', 'label']]
        #'1/sp|P60903|S10AA_HUMAN', '1/sp|Q14974|IMB1_HUMAN', '2/sp|Q13404|UB2V1_HUMAN/sp|Q15819|UB2V2_HUMAN', '1/sp|P60981|DEST_HUMAN', '1/sp|P10809|CH60_HUMAN'

df['label'] = df['label'].astype(int)
df = df[(df['label'] ==71) | (df['label'] ==72)]


df.columns = ['P60903|S10AA', 'Q14974|IMB1', 
              'Q13404|UB2V1','P60981|DEST',
              'P10809|CH60', 'label']

df.to_csv('top5_tumor_71_72.csv')
#df['label'] = df['label'].apply(lambda x : 0 if x == 71 else 1)


# As I didn't find the way of change the transparency or other parameters of sns pair plot, so at the end, I draw these plots manually.
markers = ["o", "o"]

sns.pairplot(data=df, kind="reg", 
             vars=['P60903|S10AA', 'Q14974|IMB1', 
              'Q13404|UB2V1','P60981|DEST',
              'P10809|CH60'],
             hue="label", markers=markers, palette="Set2", size=3)
plt.show()


sns.pairplot(data=df, kind="scatter", 
             vars=['P60903|S10AA', 'Q14974|IMB1', 
              'Q13404|UB2V1','P60981|DEST',
              'P10809|CH60'],
             hue="label", markers=markers, palette="Set2", size=3)

plt.show()


