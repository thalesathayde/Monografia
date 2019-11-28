import fnmatch
import os
import re
import numpy as np

pastas=["cursos_9","cursos_15","cursos_16","cursos_20","cursos_25","cursos_27","cursos_28","cursos_31","cursos_37","cursos_41","cursos_42","cursos_54",
        "groups\\courses_20_25_28_54_41_31_group_1","groups\\courses_15_42_37_27_group_2","groups\\courses_9_16_group_3"]
nome=["Nutrição","Farmácia","Medicina","Matemática","Física","Engenharia Química","Química","Ciências da Computação","Engenharia Civil","Engenharia de Telecomunicações","Engenharia de Produção","Estatística",
      "Cursos de Alta Taxa de Evasão","Cursos de Média Taxa de Evasão","Cursos de Baixa Taxa de Evasão"]

arquivos=["normalize_chi2_*_10_dt.txt","normalize_chi2_*_10_knn.txt","normalize_chi2_*_10_mlp.txt","normalize_chi2_*_10_svm.txt","normalize_chi2_*_10_xgboost.txt",
          "normalize_pca_*_10_dt.txt","normalize_pca_*_10_knn.txt","normalize_pca_*_10_mlp.txt","normalize_pca_*_10_svm.txt","normalize_pca_*_10_xgboost.txt",
          "standard_pca_*_10_dt.txt","standard_pca_*_10_knn.txt","standard_pca_*_10_mlp.txt","standard_pca_*_10_svm.txt","standard_pca_*_10_xgboost.txt"]


bestScore=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bestF1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ScoreB=[]
F1B=[]
PrecisionB=[]
RecallB=[]
for i in range(len(pastas)):
    score = []

    w, h = 4, 15;
    matrix = [["" for x in range(w)] for y in range(h)]
    #matrix = np.zeros( (15, 4) )

    f1 = []

    prec=[]
    rec=[]
    for j in range(len(arquivos)):
        nomeArquivo=fnmatch.filter(os.listdir("resultados/data_2009_2010/"+pastas[i]), arquivos[j])
        file= open("resultados/data_2009_2010/"+pastas[i] +"/"+ nomeArquivo[0], "r")

        lines = file.readlines()

        score.append(str("{0:.2f}".format(float(lines[4])*100)))


        aux = re.findall(r"[-+]?[0-9]*\.?[0-9]+", lines[7], re.MULTILINE)
        aux2 = re.findall(r"[-+]?[0-9]*\.?[0-9]+", lines[8], re.MULTILINE)
        """matrix[j][0]=str("{0:.2f}".format(float(aux[0])))
        matrix[j][1] = str("{0:.2f}".format(float(aux[1])))
        matrix[j][2] = str("{0:.2f}".format(float(aux2[0])))
        matrix[j][3] = str("{0:.2f}".format(float(aux2[1])))"""
        matrix[j][0] = str("{0:.2f}".format(float(aux2[1])))
        matrix[j][1] = str("{0:.2f}".format(float(aux2[0])))
        matrix[j][2] = str("{0:.2f}".format(float(aux[1])))
        matrix[j][3] = str("{0:.2f}".format(float(aux[0])))
        #print(matrix[j])
        #print()

        f1.append(str("{0:.4f}".format(float(lines[11]))))

        prec.append(str("{0:.4f}".format(float(lines[14]))))

        rec.append(str("{0:.4f}".format(float(lines[17]))))

        file.close()

    for k in range(len(score)):
        bestScore[k]=bestScore[k]+float(score[k])
    for k in range(len(f1)):
        bestF1[k] = bestF1[k] + float(f1[k])

    ScoreB.append(score[len(score) - 1])
    F1B.append(f1[len(f1) - 1])
    PrecisionB.append(prec[len(prec) - 1])
    RecallB.append(rec[len(rec) - 1])

    #print(max(rec))
    #por algum motivo o max() estava bugando quando tinha 100.00 como resultado
    if score.count("100.00") > 0:
        scoreMax = [k for k, x in enumerate(score) if x == "100.00"]
        for k in range(len(scoreMax)):
            score[scoreMax[k]] = "\\textbf{" + score[scoreMax[k]] + "}"
    else:
        scoreMax= [k for k, x in enumerate(score) if x == max(score)]
        for k in range(len(scoreMax)):
            score[scoreMax[k]] = "\\textbf{" + score[scoreMax[k]] + "}"

    if f1.count("100.00") > 0:
        f1Max = [k for k, x in enumerate(f1) if x == "100.00"]
        for k in range(len(f1Max)):
            f1[f1Max[k]] = "\\textbf{" + f1[f1Max[k]] + "}"
    else:
        f1Max = [k for k, x in enumerate(f1) if x == max(f1)]
        for k in range(len(f1Max)):
            f1[f1Max[k]] = "\\textbf{" + f1[f1Max[k]] + "}"

    if prec.count("100.00") > 0:
        precMax = [k for k, x in enumerate(prec) if x == "100.00"]
        for k in range(len(precMax)):
            prec[precMax[k]] = "\\textbf{" + prec[precMax[k]] + "}"
    else:
        precMax = [k for k, x in enumerate(prec) if x == max(prec)]
        for k in range(len(precMax)):
            prec[precMax[k]] = "\\textbf{" + prec[precMax[k]] + "}"

    if rec.count("100.00") > 0:
        recMax = [k for k, x in enumerate(rec) if x == "100.00"]
        for k in range(len(recMax)):
            rec[recMax[k]] = "\\textbf{" + rec[recMax[k]] + "}"
    else:
        recMax = [k for k, x in enumerate(rec) if x == max(rec)]
        for k in range(len(recMax)):
            rec[recMax[k]] = "\\textbf{" + rec[recMax[k]] + "}"

    """
    print("\\begin{table}[]\n"
          "\caption {Resultados preditivos para o curso de "+nome[i]+":} \label{acuracia"+nome[i]+"} \n"
          "\\begin{tabular}{ccccccc}\n"
          "\\cline{3-7}\n"
          "\\multicolumn{2}{l|}{}                        & \\multicolumn{1}{p{1.4cm}|}{Árvore de Decisão} & \\multicolumn{1}{c|}{KNN}               & \\multicolumn{1}{c|}{MLP} & \\multicolumn{1}{c|}{SVM}               & \\multicolumn{1}{c|}{XGBoost}               \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{Normalize} & \\multicolumn{1}{p{1.6cm}|}{Qui-Quadrado}  & \\multicolumn{1}{c|}{"+score[0]+"\\%}  & \\multicolumn{1}{c|}{"+score[1]+"\\%}  & \\multicolumn{1}{c|}{"+score[2]+"\\%} & \\multicolumn{1}{c|}{"+score[3]+"\\%}  & \\multicolumn{1}{c|}{"+score[4]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Normalize}          & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+score[5]+"\\%}  & \\multicolumn{1}{c|}{"+score[6]+"\\%}  & \\multicolumn{1}{c|}{"+score[7]+"\\%} & \\multicolumn{1}{c|}{"+score[8]+"\\%}  & \\multicolumn{1}{c|}{"+score[9]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Standard}           & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+score[10]+"\\%} & \\multicolumn{1}{c|}{"+score[11]+"\\%} & \\multicolumn{1}{c|}{"+score[12]+"\\%} & \\multicolumn{1}{c|}{"+score[13]+"\\%} & \\multicolumn{1}{c|}{"+score[14]+"\\%} \\\\ \\cline{1-7}\n"
          "\\end{tabular}\n"
          "\\end{table}\n\n\n\n") """

    """  print("\\begin{table}[]\n"
          "\caption {Matriz de Confusão para "+nome[i]+":} \label{confusao"+nome[i]+"} \n"
"\\begin{tabular}{cccccc}\n"
"\\multicolumn{1}{l}{}                                         & \\multicolumn{2}{c}{Árvore de Decisão}                                                           & \\multicolumn{1}{l}{}  & \\multicolumn{2}{c}{KNN}                                                                         \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+Qui-Quadrado}} & \\multicolumn{1}{c|}{"+matrix[0][0]+"}  & \\multicolumn{1}{c|}{"+matrix[0][1]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[1][0]+"}  & \\multicolumn{1}{c|}{"+matrix[1][1]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[0][2]+"}  & \\multicolumn{1}{c|}{"+matrix[0][3]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[1][2]+"}  & \\multicolumn{1}{c|}{"+matrix[1][3]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{l}{}                                         &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+PCA}}          & \\multicolumn{1}{c|}{"+matrix[5][0]+"}  & \\multicolumn{1}{c|}{"+matrix[5][1]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[6][0]+"}  & \\multicolumn{1}{c|}{"+matrix[6][1]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[5][2]+"}  & \\multicolumn{1}{c|}{"+matrix[5][3]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[6][2]+"}  & \\multicolumn{1}{c|}{"+matrix[6][3]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{l}{}                                         &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Standard+PCA}}           & \\multicolumn{1}{c|}{"+matrix[10][0]+"} & \\multicolumn{1}{c|}{"+matrix[10][1]+"} & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[11][0]+"} & \\multicolumn{1}{c|}{"+matrix[11][1]+"} \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[10][2]+"} & \\multicolumn{1}{c|}{"+matrix[10][3]+"} & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[11][2]+"} & \\multicolumn{1}{c|}{"+matrix[11][3]+"} \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{l}{}                                         & \\multicolumn{1}{l}{}                           & \\multicolumn{1}{l}{}                           & \\multicolumn{1}{l}{}  & \\multicolumn{1}{l}{}                           & \\multicolumn{1}{l}{}                           \\\\ \n"
"                                                             & \\multicolumn{2}{c}{MLP}                                                                         &                       & \\multicolumn{2}{c}{SVM}                                                                         \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+Qui-Quadrado}} & \\multicolumn{1}{c|}{"+matrix[2][0]+"}  & \\multicolumn{1}{c|}{"+matrix[2][1]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[3][0]+"}  & \\multicolumn{1}{c|}{"+matrix[3][1]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[2][2]+"}  & \\multicolumn{1}{c|}{"+matrix[2][3]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[3][2]+"}  & \\multicolumn{1}{c|}{"+matrix[3][3]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{l}{}                                         &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+PCA}}          & \\multicolumn{1}{c|}{"+matrix[7][0]+"}  & \\multicolumn{1}{c|}{"+matrix[7][1]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[8][0]+"}  & \\multicolumn{1}{c|}{"+matrix[8][1]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[7][2]+"}  & \\multicolumn{1}{c|}{"+matrix[7][3]+"}  & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[8][2]+"}  & \\multicolumn{1}{c|}{"+matrix[8][3]+"}  \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{l}{}                                         &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Standard+PCA}}           & \\multicolumn{1}{c|}{"+matrix[12][0]+"} & \\multicolumn{1}{c|}{"+matrix[12][1]+"} & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[13][0]+"} & \\multicolumn{1}{c|}{"+matrix[13][1]+"} \\\\ \\cline{2-3} \\cline{5-6} \n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[12][2]+"} & \\multicolumn{1}{c|}{"+matrix[12][3]+"} & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{"+matrix[13][2]+"} & \\multicolumn{1}{c|}{"+matrix[13][3]+"} \\\\ \\cline{2-3} \\cline{5-6} \n"
"                                                             &                                                &                                                &                       &                                                &                                                \\\\ \n"
"                                                             & \\multicolumn{2}{c}{XGBoost}                                                                     &                       &                                                &                                                \\\\ \\cline{2-3} \n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+Qui-Quadrado}} & \\multicolumn{1}{c|}{"+matrix[4][0]+"}  & \\multicolumn{1}{c|}{"+matrix[4][1]+"}  &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[4][2]+"}  & \\multicolumn{1}{c|}{"+matrix[4][3]+"}  &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"                                                             &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize+PCA}}          & \\multicolumn{1}{c|}{"+matrix[9][0]+"}  & \\multicolumn{1}{c|}{"+matrix[9][1]+"}  &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[9][2]+"}  & \\multicolumn{1}{c|}{"+matrix[9][3]+"}  &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"                                                             &                                                &                                                &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\multicolumn{1}{c|}{\\multirow{2}{*}{Standard+PCA}}           & \\multicolumn{1}{c|}{"+matrix[14][0]+"} & \\multicolumn{1}{c|}{"+matrix[14][1]+"} &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\multicolumn{1}{c|}{}                                        & \\multicolumn{1}{c|}{"+matrix[14][2]+"} & \\multicolumn{1}{c|}{"+matrix[14][3]+"} &                       &                                                &                                                \\\\ \\cline{2-3}\n"
"\\end{tabular}\n"
"\\end{table}\n\n\n\n")

"""
    #OLD
    """print("\\begin{table}[]\n"
"\\caption {Matriz de Confusão para "+nome[i]+":} \\label{tab:title} \n"
"\\begin{tabular}{cccccc}\n"
"                             &                              &                               &                               & \\multicolumn{2}{c}{Árvore de Decisão}                                                           &  &                               &                               & \\multicolumn{2}{c}{KNN}                                                                         \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+Qui-Quadrado}} &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[0][3]+"}  & \\multicolumn{1}{c|}{"+matrix[0][2]+"}  &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[1][3]+"}  & \\multicolumn{1}{c|}{"+matrix[1][2]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[0][1]+"}  & \\multicolumn{1}{c|}{"+matrix[0][0]+"}  &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[1][1]+"}  & \\multicolumn{1}{c|}{"+matrix[1][0]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+PCA}}          &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[5][3]+"}  & \\multicolumn{1}{c|}{"+matrix[5][2]+"}  &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[6][3]+"}  & \\multicolumn{1}{c|}{"+matrix[6][2]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[5][1]+"}  & \\multicolumn{1}{c|}{"+matrix[5][0]+"}  &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[6][1]+"}  & \\multicolumn{1}{c|}{"+matrix[6][0]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Standard+PCA}}           &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[10][3]+"} & \\multicolumn{1}{c|}{"+matrix[10][2]+"} &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[11][3]+"} & \\multicolumn{1}{c|}{"+matrix[11][2]+"} \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[10][1]+"} & \\multicolumn{1}{c|}{"+matrix[10][0]+"} &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[11][1]+"} & \\multicolumn{1}{c|}{"+matrix[11][0]+"} \\\\ \\cline{5-6} \\cline{10-11} \n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"                             &                              &                               &                               & \\multicolumn{2}{c}{MLP}                                                                         &  &                               &                               & \\multicolumn{2}{c}{SVM}                                                                         \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+Qui-Quadrado}} &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[2][3]+"}  & \\multicolumn{1}{c|}{"+matrix[2][2]+"}  &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[3][3]+"}  & \\multicolumn{1}{c|}{"+matrix[3][2]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[2][1]+"}  & \\multicolumn{1}{c|}{"+matrix[2][0]+"}  &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[3][1]+"}  & \\multicolumn{1}{c|}{"+matrix[3][0]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+PCA}}          &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[7][3]+"}  & \\multicolumn{1}{c|}{"+matrix[7][2]+"}  &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[8][3]+"}  & \\multicolumn{1}{c|}{"+matrix[8][2]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[7][1]+"}  & \\multicolumn{1}{c|}{"+matrix[7][0]+"}  &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[8][1]+"}  & \\multicolumn{1}{c|}{"+matrix[8][0]+"}  \\\\ \\cline{5-6} \\cline{10-11} \n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Standard+PCA}}           &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               & Positivo                                       & Negativo                                       \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[12][3]+"} & \\multicolumn{1}{c|}{"+matrix[12][2]+"} &  & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[13][3]+"} & \\multicolumn{1}{c|}{"+matrix[13][2]+"} \\\\ \\cline{5-6} \\cline{10-11} \n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[12][1]+"} & \\multicolumn{1}{c|}{"+matrix[12][0]+"} &  &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[13][1]+"} & \\multicolumn{1}{c|}{"+matrix[13][0]+"} \\\\ \\cline{5-6} \\cline{10-11} \n" 
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"                             &                              &                               &                               & \\multicolumn{2}{c}{XGBoost}                                                                     &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+Qui-Quadrado}} &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[4][3]+"}  & \\multicolumn{1}{c|}{"+matrix[4][2]+"}  &  & \\multirow{2}{*}{}             &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[4][1]+"}  & \\multicolumn{1}{c|}{"+matrix[4][0]+"}  &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Normalize+PCA}}          &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[9][3]+"}  & \\multicolumn{1}{c|}{"+matrix[9][2]+"}  &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[9][1]+"}  & \\multicolumn{1}{c|}{"+matrix[9][0]+"}  &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"                             &                              &                               &                               &                                                &                                                &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{\\multirow{4}{*}{Standard+PCA}}           &                               &                               & \\multicolumn{2}{c}{Verdade}                                                                     &  &                               &                               &                                                &                                                \\\\\n"
"\\multicolumn{2}{c}{}                                        &                               &                               & Positivo                                       & Negativo                                       &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        & \\multirow{2}{*}{Classificado} & \\multicolumn{1}{c|}{Positivo} & \\multicolumn{1}{c|}{"+matrix[14][3]+"} & \\multicolumn{1}{c|}{"+matrix[14][2]+"} &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\multicolumn{2}{c}{}                                        &                               & \\multicolumn{1}{c|}{Negativo} & \\multicolumn{1}{c|}{"+matrix[14][1]+"} & \\multicolumn{1}{c|}{"+matrix[14][0]+"} &  &                               &                               &                                                &                                                \\\\ \\cline{5-6}\n"
"\\end{tabular}\n"
"\\end{table}\n\n\n\n")"""

    """
    print("\\begin{table}[]\n"
          "\caption {F1-measure de "+nome[i]+":} \label{f1"+nome[i]+"} \n"
          "\\begin{tabular}{ccccccc}\n"
          "\\cline{3-7}\n"
          "\\multicolumn{2}{l|}{}                        & \\multicolumn{1}{p{1.4cm}|}{Árvore de Decisão} & \\multicolumn{1}{c|}{KNN}               & \\multicolumn{1}{c|}{MLP} & \\multicolumn{1}{c|}{SVM}               & \\multicolumn{1}{c|}{XGBoost}               \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{Normalize} & \\multicolumn{1}{p{1.6cm}|}{Qui-Quadrado}  & \\multicolumn{1}{c|}{"+f1[0]+"\\%}  & \\multicolumn{1}{c|}{"+f1[1]+"\\%}  & \\multicolumn{1}{c|}{"+f1[2]+"\\%} & \\multicolumn{1}{c|}{"+f1[3]+"\\%}  & \\multicolumn{1}{c|}{"+f1[4]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Normalize}          & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+f1[5]+"\\%}  & \\multicolumn{1}{c|}{"+f1[6]+"\\%}  & \\multicolumn{1}{c|}{"+f1[7]+"\\%} & \\multicolumn{1}{c|}{"+f1[8]+"\\%}  & \\multicolumn{1}{c|}{"+f1[9]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Standard}           & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+f1[10]+"\\%} & \\multicolumn{1}{c|}{"+f1[11]+"\\%} & \\multicolumn{1}{c|}{"+f1[12]+"\\%} & \\multicolumn{1}{c|}{"+f1[13]+"\\%} & \\multicolumn{1}{c|}{"+f1[14]+"\\%} \\\\ \\cline{1-7}\n"
          "\\end{tabular}\n"
          "\\end{table}\n") """
    """
    print("\\begin{table}[]\n"
          "\caption {Precision de "+nome[i]+":} \label{precision"+nome[i]+"} \n"
          "\\begin{tabular}{ccccccc}\n"
          "\\cline{3-7}\n"
          "\\multicolumn{2}{l|}{}                        & \\multicolumn{1}{p{1.4cm}|}{Árvore de Decisão} & \\multicolumn{1}{c|}{KNN}               & \\multicolumn{1}{c|}{MLP} & \\multicolumn{1}{c|}{SVM}               & \\multicolumn{1}{c|}{XGBoost}               \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{Normalize} & \\multicolumn{1}{p{1.6cm}|}{Qui-Quadrado}  & \\multicolumn{1}{c|}{"+prec[0]+"\\%}  & \\multicolumn{1}{c|}{"+prec[1]+"\\%}  & \\multicolumn{1}{c|}{"+prec[2]+"\\%} & \\multicolumn{1}{c|}{"+prec[3]+"\\%}  & \\multicolumn{1}{c|}{"+prec[4]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Normalize}          & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+prec[5]+"\\%}  & \\multicolumn{1}{c|}{"+prec[6]+"\\%}  & \\multicolumn{1}{c|}{"+prec[7]+"\\%} & \\multicolumn{1}{c|}{"+prec[8]+"\\%}  & \\multicolumn{1}{c|}{"+prec[9]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Standard}           & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+prec[10]+"\\%} & \\multicolumn{1}{c|}{"+prec[11]+"\\%} & \\multicolumn{1}{c|}{"+prec[12]+"\\%} & \\multicolumn{1}{c|}{"+prec[13]+"\\%} & \\multicolumn{1}{c|}{"+prec[14]+"\\%} \\\\ \\cline{1-7}\n"
          "\\end{tabular}\n"
          "\\end{table}\n") """

    """
    print("\\begin{table}[]\n"
          "\caption {Recall de "+nome[i]+":} \label{recall"+nome[i]+"} \n"
          "\\begin{tabular}{ccccccc}\n"
          "\\cline{3-7}\n"
          "\\multicolumn{2}{l|}{}                        & \\multicolumn{1}{p{1.4cm}|}{Árvore de Decisão} & \\multicolumn{1}{c|}{KNN}               & \\multicolumn{1}{c|}{MLP} & \\multicolumn{1}{c|}{SVM}               & \\multicolumn{1}{c|}{XGBoost}               \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{Normalize} & \\multicolumn{1}{p{1.6cm}|}{Qui-Quadrado}  & \\multicolumn{1}{c|}{"+rec[0]+"\\%}  & \\multicolumn{1}{c|}{"+rec[1]+"\\%}  & \\multicolumn{1}{c|}{"+rec[2]+"\\%} & \\multicolumn{1}{c|}{"+rec[3]+"\\%}  & \\multicolumn{1}{c|}{"+rec[4]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Normalize}          & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+rec[5]+"\\%}  & \\multicolumn{1}{c|}{"+rec[6]+"\\%}  & \\multicolumn{1}{c|}{"+rec[7]+"\\%} & \\multicolumn{1}{c|}{"+rec[8]+"\\%}  & \\multicolumn{1}{c|}{"+rec[9]+"\\%}  \\\\ \\cline{1-7}\n"
          "\\multicolumn{1}{|c|}{Standard}           & \\multicolumn{1}{c|}{PCA}  & \\multicolumn{1}{c|}{"+rec[10]+"\\%} & \\multicolumn{1}{c|}{"+rec[11]+"\\%} & \\multicolumn{1}{c|}{"+rec[12]+"\\%} & \\multicolumn{1}{c|}{"+rec[13]+"\\%} & \\multicolumn{1}{c|}{"+rec[14]+"\\%} \\\\ \\cline{1-7}\n"
          "\\end{tabular}\n"
          "\\end{table}\n") """

    print("\\begin{table}[] \n"
          "\\caption {Resultados preditivos para o curso de "+nome[i]+":} \\label{resultados"+nome[i]+"} \n"
          "\\begin{tabular}{ccc|c|c|c|c|}\n"
          "\\cline{4-7}\n"
          "                                                                                                           &                                                 &                        & Acurácia                 & F1-measure          & Precisão             & Sensitividade       \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{\\multirow{3}{*}{\\begin{tabular}[c]{@{}c@{}}Árvore\\\\de\\\\Decisão\\end{tabular}}} & \\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize}} & {\\begin{math}{}\\chi^2\\end{math}}         & "+score[0]+"\\%  & "+f1[0]+"  & "+prec[0]+"  & "+rec[0]+"  \\\\ \\cline{3-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{}                           & \\multirow{2}{*}{PCA} & "+score[5]+"\\%  & "+f1[5]+"  & "+prec[5]+"  & "+rec[5]+"  \\\\ \\cline{2-2} \\cline{4-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{Standard}                   &                      & "+score[10]+"\\% & "+f1[10]+" & "+prec[10]+" & "+rec[10]+" \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{\\multirow{3}{*}{KNN}}                                                                 & \\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize}} & {\\begin{math}{}\\chi^2\\end{math}}         & "+score[1]+"\\%  & "+f1[1]+"  & "+prec[1]+"  & "+rec[1]+"  \\\\ \\cline{3-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{}                           & \\multirow{2}{*}{PCA} & "+score[6]+"\\%  & "+f1[6]+"  & "+prec[6]+"  & "+rec[6]+"  \\\\ \\cline{2-2} \\cline{4-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{Standard}                   &                      & "+score[11]+"\\% & "+f1[11]+" & "+prec[11]+" & "+rec[11]+" \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{\\multirow{3}{*}{MLP}}                                                                 & \\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize}} & {\\begin{math}{}\\chi^2\\end{math}}         & "+score[2]+"\\%  & "+f1[2]+"  & "+prec[2]+"  & "+rec[2]+"  \\\\ \\cline{3-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{}                           & \\multirow{2}{*}{PCA} & "+score[7]+"\\%  & "+f1[7]+"  & "+prec[7]+"  & "+rec[7]+"  \\\\ \\cline{2-2} \\cline{4-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{Standard}                   &                      & "+score[12]+"\\% & "+f1[12]+" & "+prec[12]+" & "+rec[12]+" \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{\\multirow{3}{*}{SVM}}                                                                 & \\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize}} & {\\begin{math}{}\\chi^2\\end{math}}         & "+score[3]+"\\%  & "+f1[3]+"  & "+prec[3]+"  & "+rec[3]+"  \\\\ \\cline{3-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{}                           & \\multirow{2}{*}{PCA} & "+score[8]+"\\%  & "+f1[8]+"  & "+prec[8]+"  & "+rec[8]+"  \\\\ \\cline{2-2} \\cline{4-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{Standard}                   &                      & "+score[13]+"\\% & "+f1[13]+" & "+prec[13]+" & "+rec[13]+" \\\\ \\hline\n"
          "\\multicolumn{1}{|c|}{\\multirow{3}{*}{XGBoost}}                                                             & \\multicolumn{1}{c|}{\\multirow{2}{*}{Normalize}} & {\\begin{math}{}\\chi^2\\end{math}}         & "+score[4]+"\\%  & "+f1[4]+"  & "+prec[4]+"  & "+rec[4]+"  \\\\ \\cline{3-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{}                           & \\multirow{2}{*}{PCA} & "+score[9]+"\\%  & "+f1[9]+"  & "+prec[9]+"  & "+rec[9]+"  \\\\ \\cline{2-2} \\cline{4-7} \n"
          "\\multicolumn{1}{|c|}{}                                                                                     & \\multicolumn{1}{c|}{Standard}                   &                      & "+score[14]+"\\% & "+f1[14]+" & "+prec[14]+" & "+rec[14]+" \\\\ \\hline\n"
          "\\end{tabular}\n"
          "\\end{table}")



    print("\n\n\n%###########################################################################################################################\n\n\n")

print("\\begin{table}[]\n"
"\caption {Resultados do XGBoost com Standard e PCA por Curso:} \label{bestResult} \n"
"\\begin{tabular}{c|c|c|c|c|}\n"
"\\cline{2-5}\n"
"                                   & Acurácia       & F1-Measure & Precision & Recall  \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[0]+"}  & "+ScoreB[0]+"\\%  & "+F1B[0]+" & "+PrecisionB[0]+" & "+RecallB[0]+"  \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[1]+"}  & "+ScoreB[1]+"\\%  & "+F1B[1]+" & "+PrecisionB[1]+" & "+RecallB[1]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[2]+"}  & "+ScoreB[2]+"\\%  & "+F1B[2]+" & "+PrecisionB[2]+" & "+RecallB[2]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[3]+"}  & "+ScoreB[3]+"\\%  & "+F1B[3]+" & "+PrecisionB[3]+" & "+RecallB[3]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[4]+"}  & "+ScoreB[4]+"\\%  & "+F1B[4]+" & "+PrecisionB[4]+" & "+RecallB[4]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[5]+"}  & "+ScoreB[5]+"\\%  & "+F1B[5]+" & "+PrecisionB[5]+" & "+RecallB[5]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[6]+"}  & "+ScoreB[6]+"\\%  & "+F1B[6]+" & "+PrecisionB[6]+" & "+RecallB[6]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[7]+"}  & "+ScoreB[7]+"\\%  & "+F1B[7]+" & "+PrecisionB[7]+" & "+RecallB[7]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[8]+"}  & "+ScoreB[8]+"\\%  & "+F1B[8]+" & "+PrecisionB[8]+" & "+RecallB[8]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[9]+"}  & "+ScoreB[9]+"\\%  & "+F1B[9]+" & "+PrecisionB[9]+" & "+RecallB[9]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[10]+"} & "+ScoreB[10]+"\\% & "+F1B[10]+" & "+PrecisionB[10]+" & "+RecallB[10]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[11]+"} & "+ScoreB[11]+"\\% & "+F1B[11]+" & "+PrecisionB[11]+" & "+RecallB[11]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[12]+"} & "+ScoreB[12]+"\\% & "+F1B[12]+" & "+PrecisionB[12]+" & "+RecallB[12]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[13]+"} & "+ScoreB[13]+"\\% & "+F1B[13]+" & "+PrecisionB[13]+" & "+RecallB[13]+" \\\\ \\hline\n"
"\\multicolumn{1}{|c|}{"+nome[14]+"} & "+ScoreB[14]+"\\% & "+F1B[14]+" & "+PrecisionB[14]+" & "+RecallB[14]+" \\\\ \\hline\n"
"\\end{tabular}\n"
"\\end{table}\n")


for i in range(len(bestScore)):
    bestScore[i]=bestScore[i]/len(pastas)
    bestF1[i]=bestF1[i]/len(pastas)

print(bestScore)
print()
print(bestF1)