pastas=["9","15","16","20","25","27","28","31","37","41","42","54"]
modos=["normalize chi2","normalize pca","standard pca"]
modos2=["normalize_chi2","normalize_pca","standard_pca"]
#modos=["normalize","standard"]
#modos2=["normalize","standard"]
#modos=["chi2","pca"]
#modos2=["chi2","pca"]
classificacoes=["knn","svm","mlp","dt","xgboost"]
grupos=["courses_9_16_group_3","courses_15_42_37_27_group_2","courses_20_25_28_54_41_31_group_1"]
reducao=["146","177","225","225","225", "225", "149", "225", "187", "158", "203", "119"]


for i in range(len(pastas)):
    #print("python main.py anon/data_2009_2010/cursos_"+pastas[i]+"/")
    for k in range(len(classificacoes)):
        for j in range(len(modos)):
            print("python trainer.py anon/data_2009_2010/cursos_"+pastas[i]+"/output.txt resultados/data_2009_2010/cursos_"+pastas[i]+"/"+modos2[j]+"_119_10_"+classificacoes[k]+".txt "+modos[j]+" 119 10 "+classificacoes[k])

            #sem reducao
            #print("python trainer.py anon/data_2009_2010/cursos_" + pastas[i] + "/output.txt resultados/data_2009_2010/cursos_" + pastas[i] + "/" + modos2[j] + "_3_" +classificacoes[k] + ".txt " + modos[j] + " 3 " + classificacoes[k])

print()
print()
for i in range(len(grupos)):
    #print("python main.py anon/data_2009_2010/groups/"+grupos[i]+"/")
    for k in range(len(classificacoes)):
        for j in range(len(modos)):
            print("python trainer.py anon/data_2009_2010/groups/"+grupos[i]+"/output.txt resultados/data_2009_2010/groups/"+grupos[i]+"/"+modos2[j]+"_119_10_"+classificacoes[k]+".txt "+modos[j]+" 119 10 "+classificacoes[k])

            #Sem reducao
            #print("python trainer.py anon/data_2009_2010/groups/" + grupos[i] + "/output.txt resultados/data_2009_2010/groups/" + grupos[i] + "/" + modos2[j] + "_3_" +classificacoes[k] + ".txt " + modos[j] + " 3 " + classificacoes[k])

print()
print("PAUSE")
# curso 25 está usando hexadecimal, preciso endireitar na leitura