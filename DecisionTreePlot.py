import matplotlib.pyplot as plt
import numpy
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


dataset = numpy.loadtxt("anon/data_2009_2010/cursos_16/output.txt", delimiter=',')


train = dataset[:,0:dataset.shape[1]-2]
target= dataset[:,dataset.shape[1]-1]
train = StandardScaler().fit_transform(train)
pca = PCA(n_components=119)
train=pca.fit_transform(train)

dt = DecisionTreeClassifier()
dt.fit(train, target)
plot_tree(dt, filled=True)
plt.show()


dataset = numpy.loadtxt("anon/data_2009_2010/cursos_25/output.txt", delimiter=',')

train = dataset[:,0:dataset.shape[1]-2]
target= dataset[:,dataset.shape[1]-1]
train = StandardScaler().fit_transform(train)
pca = PCA(n_components=119)
train=pca.fit_transform(train)

dt = DecisionTreeClassifier()
dt.fit(train, target)
plot_tree(dt, filled=True)
plt.show()