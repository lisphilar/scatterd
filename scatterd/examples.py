from scatterd import scatterd, import_example
import numpy as np

# %%

# df = import_example()
# scatterd(df['tsneX'], df['tsneY'], z=df['PC2'], labels=df['labx'], gradient='#FFFFFF', cmap='Set1')
# scatterd(df['tsneX'], df['tsneY'], cmap='Set1')
# scatterd(df['tsneX'], df['tsneY'], labels=df['labx'], cmap='Set1')

# %%import some data to play with
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
labels = iris.target


# %% Scatter

# Change figure size
scatterd(X[:,0], X[:,1])
scatterd(X[:,0], X[:,1], c=[1,0,0])

scatterd(X[:,0], X[:,1], fontcolor=[1,0,0])
scatterd(X[:,0], X[:,1], fontcolor='r')
scatterd(X[:,0], X[:,1], c=[1,0,0])

scatterd(X[:,0], X[:,1], labels=labels)
scatterd(X[:,0], X[:,1], labels=labels, gradient='#FFFFFF')
scatterd(X[:,0], X[:,1], labels=labels, cmap='Set2')


# Color based on labels
scatterd(X[:,0], X[:,1], s=100, density=True)
scatterd(X[:,0], X[:,1], labels=labels, density=True)
scatterd(X[:,0], X[:,1], labels=labels, density=True, fontcolor=[0,0,0])

# Set labels
scatterd(X[:,0], X[:,1], labels=labels, s=100, norm=True, cmap='Set2', xlabel='xlabel', ylabel='ylabel', title='Title')
# Change sizes
s=np.random.randint(10, 500,len(labels))
scatterd(X[:,0], X[:,1], labels=labels, s=s, cmap='Set2', xlabel='xlabel', ylabel='ylabel', title='Title', fontsize=25, density=True)

scatterd(X[:,0], X[:,1], labels=labels, s=s, cmap='Set2', xlabel='xlabel', ylabel='ylabel', title='Title', fontsize=25, density=True, fontcolor=[0,0,0])

args_density = {'fill': True, 'thresh': 0, 'levels': 100, 'cmap':"mako", 'cbar': False, 'shade':True}
scatterd(X[:,0], X[:,1], labels=labels, s=s, cmap='Set2', xlabel='xlabel', ylabel='ylabel', title='Title', fontsize=25, density=True, fontcolor=[0,0,0], axiscolor=None, args_density=args_density)

# %%