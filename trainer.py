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

def help(selfName):

    #sys.stderr.write("Simulador de metodos de FEC/codificacao.\n\n")
    #sys.stderr.write("Modo de uso:\n\n")
    #sys.stderr.write("\t" + selfName + " <tam_pacote> <reps> <prob. erro>\n\n")
    #sys.stderr.write("Onde:\n")
    #sys.stderr.write("\t- <tam_pacote>: tamanho do pacote usado nas simulacoes (em bytes).\n")
    #sys.stderr.write("\t- <reps>: numero de repeticoes da simulacao.\n")
    #sys.stderr.write("\t- <prob. erro>: probabilidade de erro de bits (i.e., probabilidade\n")
    #sys.stderr.write("de que um dado bit tenha seu valor alterado pelo canal.)\n\n")

    sys.stderr.write("Modo de uso do " + selfName + ":\n\n")
    sys.stderr.write("\t usar como argumento os metodos que vc quer chamar e na ordem que quer executar, "
                     "sendo o penultimo ultimo argumento o numero de partições que o k fold vai usar \n\n")
    sys.stderr.write("Onde:\n")
    sys.stderr.write("\t- chi2: Feature selection, tem que ser seguido de um numero para os K mais importantes\n")
    sys.stderr.write("\t- pca: Decomposition, tem que ser seguido de um numero para os K mais importantes\n")
    sys.stderr.write("\t- standard: Standard Scale, padroniza os dados em media=0 e variancia=1\n")
    sys.stderr.write("\t- normalize: Normaliza os dados\n")

    sys.exit(1)

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

#SEPARAR A PARTE DE TREINAMENTO COM A PARTE DE ALVO(RESULTADO CERTO)
#botar para abrir arquivos, assim vai ser muito ruim
if len(sys.argv) == 1:
    help(sys.argv[0])
#else:
#   train=sys.argv[1]
#   target=sys.argv[2]

# para teste usando a base de iris
"""iris = load_iris()
train=iris.data
target=iris.target"""

caminho=sys.argv[1]
output=sys.argv[2]

dataset = numpy.loadtxt(caminho, delimiter=',')


""" isso era hard coded para o de 2009-2010 de ciencia da computação
train = dataset[:,0:2229]
target= dataset[:,2230]"""

train = dataset[:,0:dataset.shape[1]-2]
target= dataset[:,dataset.shape[1]-1]

scoreFinal=0
matrixDeConfusao= numpy.zeros( (2, 2) )
f1Score=0
precision=0
recall=0
allScores=[]
allF1=[]
allPrecision=[]
allRecall=[]

precisao, sensibilidade, average_precision= 0,0,0

#print(dataset)
#print()
#print(train)
#print()
#print(target)
#print()


#print("antes:")
#print(train)
continuar=False
for i in range(3,len(sys.argv)-2):
    if continuar:
        continuar=False
        continue
    if sys.argv[i] == "chi2":
        train = featureSelection(train, target, int(sys.argv[i+1]))
        continuar=True
        continue
    if sys.argv[i] == "pca":
        train = decomposition(train, int(sys.argv[i+1]))
        continuar=True
        continue
    if sys.argv[i] == "standard":
        train = standard(train)
        #print("standard")
        #print(train)
        #print()
        continue
    if sys.argv[i] == "normalize":
        train = normalizar(train)
        #print("normalize")
        #print(train)
        #print()
        continue
    print("##########################################################################################\n")
    print(sys.argv[i]+" não é um comando válido\n")
    print("##########################################################################################")

#print("depois:")
#print(train)

#print("\n\n Stratified K Fold:")

#shuffle com um random_state fixo fará com que sempre de a mesma divisão, mas que embaralhe o grupo
skf = StratifiedKFold(n_splits=int(sys.argv[len(sys.argv)-2]), shuffle=True ,random_state=42)
skf.get_n_splits(train, target)

#print(skf)

for train_index, test_index in skf.split(train, target):
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = train[train_index], train[test_index]
    y_train, y_test = target[train_index], target[test_index]

    #Classificador KNN
    if sys.argv[len(sys.argv)-1] == "knn":
        #testar o n_neighbors com o codigo
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train,y_train)
        y_pred=knn.predict(X_test)

    #classificador svm
    if sys.argv[len(sys.argv) - 1] == "svm":
        #confirmar esses parametros com a aline
        #testar os parametros
        svmClassifier =svm.SVC(gamma='scale',kernel='linear')
        svmClassifier.fit(X_train,y_train)
        y_pred=svmClassifier.predict(X_test)

    #rede neural mlp
    if sys.argv[len(sys.argv) - 1] == "mlp":
        #mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
        #Ver com aline quais parametros passar aqui
        #testar os parametros
        mlp = MLPClassifier()
        mlp.fit(X_train, y_train)
        y_pred=mlp.predict(X_test)

    #Arvore de decisão
    if sys.argv[len(sys.argv) - 1] == "dt":
        #dt = DecisionTreeClassifier(criterion="gini", random_state=100,max_depth=3, min_samples_leaf=5)
        #testar os parametros
        dt = DecisionTreeClassifier()
        dt.fit(X_train, y_train)
        y_pred = dt.predict(X_test)
        #plot_tree(dt, filled=True)
        #plt.show()

            #XGBoost
    if sys.argv[len(sys.argv) - 1] == "xgboost":
        xgboost = XGBClassifier()
        xgboost.fit(X_train, y_train)
        #print(xgboost)
        y_pred = xgboost.predict(X_test)



    """
    print(sys.argv[len(sys.argv) - 1])
    print("score:")
    print(metrics.accuracy_score(y_test, y_pred))
    print("confusion matrix:")
    print(metrics.confusion_matrix(y_test, y_pred))
    #print("classification report:")
    #print(metrics.classification_report(y_test, y_pred))
    print("f1 score")
    print(metrics.f1_score(y_test, y_pred))
    print()"""

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
    plt.show()

    scoreFinal+=metrics.accuracy_score(y_test, y_pred)
    matrixDeConfusao+=metrics.confusion_matrix(y_test, y_pred)
    f1Score+=metrics.f1_score(y_test, y_pred)
    precision+=metrics.precision_score(y_test, y_pred)
    recall+=metrics.recall_score(y_test, y_pred)

    allScores.append(metrics.accuracy_score(y_test, y_pred))
    allF1.append(metrics.f1_score(y_test, y_pred))
    allPrecision.append(metrics.precision_score(y_test, y_pred))
    allRecall.append(metrics.recall_score(y_test, y_pred))


scoreFinal=scoreFinal/int(sys.argv[len(sys.argv)-2])
matrixDeConfusao=matrixDeConfusao/int(sys.argv[len(sys.argv)-2])
f1Score=f1Score/int(sys.argv[len(sys.argv)-2])
precision=precision/int(sys.argv[len(sys.argv)-2])
recall=recall/int(sys.argv[len(sys.argv)-2])


print("#########################################################")
print(sys.argv[len(sys.argv) - 1])
print()
print("Score Final:")
print(scoreFinal)
print()
print("Matriz de Confusão final:")
print(matrixDeConfusao)
print()
print("F1 Score Final:")
print(f1Score)
print()
print("Precision Final:")
print(precision)
print()
print("Recall Final:")
print(recall)
print()

os.makedirs(os.path.dirname(output), exist_ok=True)
with open(output, "w") as f:
    resultado = open(output, "w")
    resultado = open(output, "a")


for i in range(len(sys.argv)):
    resultado.write(sys.argv[i]+" ")
resultado.write("\n#########################################################")
resultado.write("\n\n")
resultado.write("Score Final:\n")
resultado.write(str(scoreFinal))
resultado.write("\n\n")
resultado.write("Matriz de Confusão final:\n")
resultado.write(str(matrixDeConfusao))
resultado.write("\n\n")
resultado.write("F1 Score Final:\n")
resultado.write(str(f1Score))
resultado.write("\n\n")
resultado.write("Precision Score Final:\n")
resultado.write(str(precision))
resultado.write("\n\n")
resultado.write("Recall Score Final:\n")
resultado.write(str(recall))
resultado.write("\n")
resultado.write("Todos Scores:\n")
resultado.write(str(allScores))
resultado.write("\n\n")
resultado.write("Todos F1 Scores:\n")
resultado.write(str(allF1))
resultado.write("\n\n")
resultado.write("Todas Precisions:\n")
resultado.write(str(allPrecision))
resultado.write("\n\n")
resultado.write("Todos Recalls:\n")
resultado.write(str(allRecall))
resultado.write("\n")
