import datetime
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import pylab as pl
import seaborn as sns

df = pd.read_csv('######.csv')


df = df.ix[:,1:]

iris = sns.load_dataset("iris")
species = iris.pop("species")


# your first target column
labels = df['label']
lut_lbs = dict(zip(labels.unique(), ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]))
print(lut_lbs)                   
row_colors_lbs = labels.map(lut_lbs)

# your second target column
tissues = df['Tissue']
lut_tius = dict(zip(tissues.unique(), "br"))
row_colors_tius = tissues.map(lut_tius)

df_for_clustermap=df.ix[:,4:]

new_feature_names = [str(x)[5:11] for x in list(df_for_clustermap.columns)]

df_for_clustermap.columns = new_feature_names



#if you want to change the position of colorbar, then you need to ensure keep the xticklabel and yticklabels.
g = sns.clustermap( np.log(df_for_clustermap), 
                   #xticklabels=False, 
                   #yticklabels=False, 
                   #col_cluster = False, 
                   row_cluster=False,
                   #cbar_kws={'label': 'colorbar title'}, 
                   row_colors=[row_colors_lbs,row_colors_tius], 
                   cmap='RdBu',
                   figsize=(28, 12)
                   )


# To be honest, there are plenty ways of beautifing the following code, but I admit that I am lazy.. lol.
g.ax_row_colors.axes.annotate("60",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 30),
                              color = 'white', 
                              fontsize=15)#.set_yticklabels(list(labels.unique()))#(xtickslabels='common xlabel', ytickslabels='common ylabel')

g.ax_row_colors.axes.annotate("71",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 430),
                              color = 'white', 
                              fontsize=15)
g.ax_row_colors.axes.annotate("72",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 960),
                              color = 'white', 
                              fontsize=15)
g.ax_row_colors.axes.annotate("80",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 1230),
                              color = 'white', 
                              fontsize=15)
g.ax_row_colors.axes.annotate("90",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 1380),
                              color = 'white', 
                              fontsize=15)
'''

#Too small, so did not add this category.
g.ax_row_colors.axes.annotate("60",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(0.25, 1450),
                              #color = 'white', 
                              fontsize=15)
'''

g.ax_row_colors.axes.annotate("N",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 25),
                              color = 'white', 
                              fontsize=12)#.set_yticklabels(list(labels.unique()))#(xtickslabels='common xlabel', ytickslabels='common ylabel')

g.ax_row_colors.axes.annotate("T",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 60),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("N",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 280),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("T",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 600),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("N",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 880),
                              color = 'white', 
                              fontsize=12)
g.ax_row_colors.axes.annotate("T",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 1060),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("N",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 1180),
                              color = 'white', 
                              fontsize=12)
g.ax_row_colors.axes.annotate("T",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 1260),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("N",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 1330),
                              color = 'white', 
                              fontsize=12)

g.ax_row_colors.axes.annotate("T",rotation=90, 
                              xy=(0.5, 0.5), 
                              xytext=(1.3, 1400),
                              color = 'white', 
                              fontsize=12)

print(len(g.ax_row_colors.axes.get_xticklabels()))

# This is very strange as the color bar cannot be relocated if there are too many columns(~1500 columns in this data)
g.cax.set_position([.15, .2, .03, .45])
#g.ax_col_dendrogram.legend(loc="center", ncol=3)
#plt.tight_layout()
#dendro_box = g.ax_row_dendrogram.get_position()
#dendro_box.x0 = (dendro_box.x0 + 2 * dendro_box.x1) / 3
#g.cax.set_position(dendro_box)
#col = g.ax_col_dendrogram.get_position()
#print(col)
#g.ax_col_dendrogram.set_position([col.x0, col.y0, col.width, col.height*0.01])

