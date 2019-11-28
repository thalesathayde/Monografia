import sys
#import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from xgboost import XGBClassifier
import numpy
import os
from sklearn.metrics import precision_recall_curve
from sklearn import tree
import matplotlib.pyplot as plt
from inspect import signature
from sklearn.metrics import average_precision_score



def featureSelection(train, target, k):
    chi2_selector = SelectKBest(chi2, k)
    return chi2_selector.fit_transform(train, target)

def decomposition(train, k):
    pca = PCA(n_components=k)
    return pca.fit_transform(train)

    #principalDf = pd.DataFrame(data=principalComponents
     #                          , columns=['principal component 1', 'principal component 2'])

#isso bota os dados em media=0 variancia=1
def standard(train):
    return StandardScaler().fit_transform(train)

def normalizar(train):
    return normalize(train)

def arvoreDecisao(X_train, y_train, X_test):
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt.predict(X_test)


def XGBoost(X_train, y_train, X_test):
    xgboost = XGBClassifier()
    xgboost.fit(X_train, y_train)
    # print(xgboost)
    return xgboost.predict(X_test)


pastas=["cursos_9","cursos_15","cursos_16","cursos_20","cursos_25","cursos_27","cursos_28","cursos_31","cursos_37","cursos_41","cursos_42","cursos_54",
        "groups\\courses_20_25_28_54_41_31_group_1","groups\\courses_15_42_37_27_group_2","groups\\courses_9_16_group_3"]
nome=["Nutrição","Farmácia","Medicina","Matemática","Física","Engenharia Química","Química","Ciências da Computação","Engenharia Civil","Engenharia de Telecomunicações","Engenharia de Produção","Estatística",
      "Cursos de Alta Taxa de Evasão","Cursos de Média Taxa de Evasão","Cursos de Baixa Taxa de Evasão"]
colors=["#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabebe", "#469990", "#e6beff", "#9A6324", "#fffac8", "#800000", "#aaffc3", "#808000", "#ffd8b1", "#000075", "#a9a9a9"]

lines = []
labels = []
recall=[]
precision=[]








for i in range(len(pastas)):
    dataset = numpy.loadtxt("anon/data_2009_2010/" + pastas[i] + "/output.txt", delimiter=',')
    train = dataset[:, 0:dataset.shape[1] - 2]
    target = dataset[:, dataset.shape[1] - 1]

    train = dataset[:, 0:dataset.shape[1] - 2]
    target = dataset[:, dataset.shape[1] - 1]
    if i == 4 or i == 5:
        train = normalizar(train)
    else:
        train = standard(train)

    train = decomposition(train, 119)


    X_train, X_test = [], []
    y_train, y_test = [], []

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    skf.get_n_splits(train, target)

    for train_index, test_index in skf.split(train, target):
        X_train, X_test = train[train_index], train[test_index]
        y_train, y_test = target[train_index], target[test_index]


    scoreFinal = 0
    matrixDeConfusao = numpy.zeros((2, 2))
    f1Score = 0
    precision = 0
    recall = 0
    allScores = []
    allF1 = []
    allPrecision = []
    allRecall = []

    precisao, sensibilidade, average_precision = 0, 0, 0


    if i==6 or i == 11:
        y_pred = arvoreDecisao(X_train,y_train,X_test)
    else:
        y_pred = XGBoost(X_train, y_train, X_test)




    precisao, sensibilidade, _ = precision_recall_curve(y_test, y_pred)
    l, = plt.plot(sensibilidade, precisao, color=colors[i], lw=2)
    lines.append(l)
    labels.append("Precision-recall para "+nome[i])




fig = plt.gcf()
fig.subplots_adjust(bottom=0.25)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Curva de Precision-Recall para melhor método de cada Curso')
plt.legend(lines, labels, ncol=3, loc=(0, -.38), prop=dict(size=13))


plt.show()




#print(skf)

"""
precisao, sensibilidade, _ = precision_recall_curve(y_test, y_pred)
    #print("precisão="+str(precision))
    #print("sensibilidade="+str(sensibilidade))
average_precision += average_precision_score(y_test, y_pred)
    #print()

    #print('Average precision-recall score: {0:0.2f}'.format(average_precision))

    # In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
    #step_kwargs = ({'step': 'post'}
    #               if 'step' in signature(plt.fill_between).parameters
    #               else {})
plt.step(sensibilidade, precisao, color='black', alpha=0.2,
             where='post')
    #plt.fill_between(sensibilidade, precisao, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))
plt.show()"""
