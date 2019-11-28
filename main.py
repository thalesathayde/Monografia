import sys
def convertLine(string):
    start = string.find("(") + 1
    end = string.find(")")
    return string[start:end].split(",")

def convertFile(file):
    resp=[]
    for x in file:
        resp.append(convertLine(x))
    return resp


caminho=sys.argv[1] #exemplo anon/data_2009_2010/cursos_31/

fileAlunoTurma = open(caminho+"resultadoAlunoTurma.pl", "r")
fileAlunoIngresso = open(caminho+"anoSemestreIngresso.pl", "r")
fileCidade = open(caminho+"cidade.pl", "r")
fileIdade = open(caminho+"classeIdadeAluno.pl", "r")
fileCor = open(caminho+"corAluno.pl", "r")
fileCr = open(caminho+"crAluno.pl", "r")
fileCurso = open(caminho+"cursoAluno.pl", "r")
fileEstadoCivil = open(caminho+"estadoCivil.pl", "r")
fileGenero = open(caminho+"generoAluno.pl", "r")
fileSemTrancados = open(caminho+"qtdSemTrancados.pl", "r")
fileFacebook = open(caminho+"temFacebook.pl", "r")
fileTwitter = open(caminho+"temTwitter.pl", "r")
fileEvadiu = open(caminho+"evasao.f", "r")

resultadoAlunoTurma=convertFile(fileAlunoTurma)
cidades=convertFile(fileCidade)
idades=convertFile(fileIdade)
cores=convertFile(fileCor)
crs=convertFile(fileCr)
cursos=convertFile(fileCurso)
estadosCivil=convertFile(fileEstadoCivil)
generos=convertFile(fileGenero)
semestresTrancados=convertFile(fileSemTrancados)
facebooks=convertFile(fileFacebook)
twitters=convertFile(fileTwitter)
evadiu=convertFile(fileEvadiu)

fileAlunoTurma.close()
fileCidade.close()
fileIdade.close()
fileCor.close()
fileCr.close()
fileCurso.close()
fileEstadoCivil.close()
fileGenero.close()
fileSemTrancados.close()
fileFacebook.close()
fileTwitter.close()


#print(resultadoAlunoTurma)
turmas=[]
for i in resultadoAlunoTurma:
    if i[2:] not in turmas:
        turmas.append(i[2:])
    #    print(str(i[2:]))
    #else:
    #    print("ja tinha=>"+str(i[2:]))
#for i in turmas:
#    print(i)

aIdades=[]
for i in idades:
    if i[1] not in aIdades:
        aIdades.append(i[1])
aIdades.sort()


output = open(caminho+"output.txt","w")
legenda = open(caminho+"legenda.txt","w")
legenda.write("Legenda=> Aluno, ano de ingresso, semestre de ingresso, cidade, classe de idade, cor, cr, curso, estado civil, genero,"
             " semestres trancados, facebook, twitter, Array de turmas que ou passou ou resprovou ou nao fez, evadiu\n"
              "legenda para turmas que reprovou ou passou=> nao inscrito=0, reprovado=1, aprovado=2\n")
legenda.close()
output.close()
output = open(caminho+"output.txt","a")
legenda = open(caminho+"legenda.txt","a")

aCidade=[]
aCores=[]
aEstadoCivil=[]
aGenero=[]
for alunoIngresso in fileAlunoIngresso:
    string=str(convertLine(alunoIngresso))[1:-1].replace("'","").replace(" ","")
    alunoId=convertLine(alunoIngresso)[0]
    achouCidade=False
    for i in cidades:
        if alunoId == i[0]:
            achouCidade=True
            if str(i[1][1:-1]) not in aCidade:
                aCidade.append(i[1][1:-1])
            string+=","+str(aCidade.index(str(i[1][1:-1])))
            #string+=","+str(i[1])[1:-1]
            break
    if not achouCidade:
        if "nao informada" not in aCidade:
            aCidade.append("nao informada")
        string += "," + str(aCidade.index("nao informada"))
    for i in idades:
        if alunoId == i[0]:
            #string+=","+str(i[1])[2:-1]
            string+=","+str(aIdades.index(i[1]))
            break
    for i in cores:
        if alunoId == i[0]:
            if str(i[1]) not in aCores:
                aCores.append(i[1])
            string+=","+str(aCores.index(str(i[1])))
            #string+=","+str(i[1])[1:-1]
            break
    for i in crs:
        if alunoId == i[0]:
            string+=","+str(i[1])
            break
    for i in cursos:
        if alunoId == i[0]:
            string+=","+str(i[1])
            break
    #ver se endireita como o estado civil entra na lista, pq nao eh igual o de todo mundo
    for i in estadosCivil:
        if alunoId == i[0]:
            if str(i[1]) not in aEstadoCivil:
                aEstadoCivil.append(i[1])
            string+=","+str(aEstadoCivil.index(str(i[1])))
            #string+=","+str(i[1])[1:-2]
            break
    for i in generos:
        if alunoId == i[0]:
            if str(i[1]) not in aGenero:
                aGenero.append(i[1])
            string+=","+str(aGenero.index(str(i[1])))
            #string+=","+str(i[1])[1:-1]
            break
    trancouAlgumSemestre=False
    for i in semestresTrancados:
        if alunoId == i[0]:
            trancouAlgumSemestre=True
            string+=","+str(i[1])
            break
    if not trancouAlgumSemestre:
        string += ",0"
    for i in facebooks:
        if alunoId == i[0]:
            string+=","+str(i[1])
            break
    for i in twitters:
        if alunoId == i[0]:
            string+=","+str(i[1])
            break

    for i in turmas:
        temp = 0
        for j in resultadoAlunoTurma:
            if i == j[2:]:
                if alunoId == j[0]:
                    if j[1] == "reprovado":
                        temp = 1
                        break
                    if j[1] == "aprovado":
                        temp = 2
                        break
        string+=","+str(temp)

    for i in evadiu:
        temp = 0;
        if alunoId == i[0]:
            temp = 1;
            break
    string += "," + str(temp)





    output.write(string+"\n")

legenda.write("legenda para cidades => ")
for i in aCidade:
    legenda.write(str(i)+"="+str(aCidade.index(i))+" ")
legenda.write("\n")

legenda.write("legenda para classe de idades=> ")
for i in aIdades:
    legenda.write(str(i)+"="+str(aIdades.index(i))+" ")
legenda.write("\n")

legenda.write("legenda para Cores=> ")
for i in aCores:
    legenda.write(str(i)+"="+str(aCores.index(i))+" ")
legenda.write("\n")

legenda.write("legenda para Estado Civil=> ")
for i in aEstadoCivil:
    legenda.write(str(i)+"="+str(aEstadoCivil.index(i))+" ")
legenda.write("\n")

legenda.write("legenda para genero=> ")
for i in aGenero:
    legenda.write(str(i)+"="+str(aGenero.index(i))+" ")
legenda.write("\n")

legenda.write(str(turmas))

legenda.write("legenda para evasão=> não evadiu = 0, evadiu = 1")

output.close()
legenda.close()
fileAlunoIngresso.close()