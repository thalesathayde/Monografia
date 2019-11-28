import fnmatch
import os
import re
from collections import Counter
from scipy import stats


pastas=["cursos_9","cursos_15","cursos_16","cursos_20","cursos_25","cursos_27","cursos_28","cursos_31","cursos_37","cursos_41","cursos_42","cursos_54",
        "groups\\courses_20_25_28_54_41_31_group_1","groups\\courses_15_42_37_27_group_2","groups\\courses_9_16_group_3"]
nome=["Nutrição","Farmácia","Medicina","Matemática","Física","Engenharia Química","Química","Ciências da Computação","Engenharia Civil","Engenharia de Telecomunicações","Engenharia de Produção","Estatística",
      "Cursos de Alta Taxa de Evasão","Cursos de Média Taxa de Evasão","Cursos de Baixa Taxa de Evasão"]

arquivos=["normalize_chi2_*_10_dt.txt","normalize_chi2_*_10_knn.txt","normalize_chi2_*_10_mlp.txt","normalize_chi2_*_10_svm.txt","normalize_chi2_*_10_xgboost.txt",
          "normalize_pca_*_10_dt.txt","normalize_pca_*_10_knn.txt","normalize_pca_*_10_mlp.txt","normalize_pca_*_10_svm.txt","normalize_pca_*_10_xgboost.txt",
          "standard_pca_*_10_dt.txt","standard_pca_*_10_knn.txt","standard_pca_*_10_mlp.txt","standard_pca_*_10_svm.txt","standard_pca_*_10_xgboost.txt"]

x=[]
ps=[]

for i in range(len(pastas)):
    for j in range(len(arquivos)-1):
        #for k in range((j+1),len(arquivos)):
            nomeArquivo = fnmatch.filter(os.listdir("resultados/data_2009_2010/" + pastas[i]), arquivos[j])
            file = open("resultados/data_2009_2010/" + pastas[i] + "/" + nomeArquivo[0], "r")
            #nomeArquivo2 = fnmatch.filter(os.listdir("resultados/data_2009_2010/" + pastas[i]), arquivos[k])
            nomeArquivo2 = fnmatch.filter(os.listdir("resultados/data_2009_2010/" + pastas[i]), arquivos[14])
            file2 = open("resultados/data_2009_2010/" + pastas[i] + "/" + nomeArquivo2[0], "r")


            lines = file.readlines()
            score = re.findall(r"[-+]?[0-9]*\.?[0-9]+", lines[19], re.MULTILINE)
            score = list(map(float,score))


            lines2 = file2.readlines()
            score2 = re.findall(r"[-+]?[0-9]*\.?[0-9]+", lines2[19], re.MULTILINE)
            score2 = list(map(float, score2))

            #print(score)
            #print(score2)

            t, p = stats.ttest_ind(score, score2)

            if p > 0.05:
                x.append(arquivos[j])
                print("resultados/data_2009_2010/" + pastas[i] + "/" + nomeArquivo[0], "r")
                print("resultados/data_2009_2010/" + pastas[i] + "/" + nomeArquivo2[0], "r")
                print("t = " + str(t))
                print("p = " + str(p))
                ps.append(p)

            #print()
            file.close()
            file2.close()
    print()

print(Counter(x))

#hardcoded
standard_pca__10_dt = []
standard_pca__10_svm = []
normalize_chi2__10_xgboost = []
normalize_chi2__10_dt = []
normalize_pca__10_dt = []
normalize_pca__10_xgboost = []
for i in range(len(x)):
    if x[i] == 'standard_pca_*_10_dt.txt':
        standard_pca__10_dt.append(ps[i])
    if x[i] == 'standard_pca_*_10_svm.txt':
        standard_pca__10_svm.append(ps[i])
    if x[i] == 'normalize_chi2_*_10_xgboost.txt':
        normalize_chi2__10_xgboost.append(ps[i])
    if x[i] == 'normalize_chi2_*_10_dt.txt':
        normalize_chi2__10_dt.append(ps[i])
    if x[i] == 'normalize_pca_*_10_dt.txt':
        normalize_pca__10_dt.append(ps[i])
    if x[i] == 'normalize_pca_*_10_xgboost.txt':
        normalize_pca__10_xgboost.append(ps[i])

print(standard_pca__10_dt)
print(standard_pca__10_svm)
print(normalize_chi2__10_xgboost)
print(normalize_chi2__10_dt)
print(normalize_pca__10_dt)
print(normalize_pca__10_xgboost)
