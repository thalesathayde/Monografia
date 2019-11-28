:- set(i,2).
:- set(minpos,2).
:- set(record,true).
:- set(recordfile,output).
:- set(nodes, 10000).
:- set(clauselength,10).
:- set(noise, 10).

:- modeh(1,evasao(+matricula)).
:- modeb(1,curso_aluno(+matricula,-curso)).
:- modeb(1,curso_aluno(+matricula,#curso)).
:- modeb(1,cr_aluno(+matricula,-cr)).
:- modeb(1,cor_aluno(+matricula,-cor)).
:- modeb(1,cor_aluno(+matricula,#cor)).
:- modeb(1,genero_aluno(+matricula,-genero)).
:- modeb(1,genero_aluno(+matricula,#genero)).
:- modeb(1,estado_civil(+matricula,-estadocivil)).
:- modeb(1,estado_civil(+matricula,#estadocivil)).
:- modeb(1,ano_semestre_ingresso(+matricula,-ano,-semestre)).
:- modeb(1,professor_turma(-siape,+codturma,+iddisciplina,-anosemestre)).
:- modeb(*,resultado_aluno_turma(+matricula,#resultado,-iddisciplina,-codturma,-ano, -semestre)).
:- modeb(*, n_reprovacao_disciplina(+matricula, -disciplina,#qtd)).
:- modeb(*, n_reprovacao_disciplina(+matricula, #disciplina,#qtd)).
:- modeb(1,qtd_semestres_trancados(+matricula,-qtdsemtrancados)).
:- modeb(1,qtd_semestres_trancados(+matricula,#qtdsemtrancados)).
:- modeb(1,tem_facebook(+matricula,#facebook)).
:- modeb(1,tem_twitter(+matricula,#twitter)).
:- modeb(1,cidade(+matricula,#cidade)).
:- modeb(1,classe_idade_aluno(+matricula,-classe)).
:- modeb(1,classe_idade_aluno(+matricula,#classe)).
:- modeb(1,classe_idade_professor(-siape,-classe)).
:- modeb(1,classe_idade_professor(-siape,#classe)).

:- determination(evasao/1,curso_aluno/2).
:- determination(evasao/1,cr_aluno/2).
:- determination(evasao/1,cor_aluno/2).
:- determination(evasao/1,genero_aluno/2).
:- determination(evasao/1,estado_civil/2).
:- determination(evasao/1,ano_semestre_ingresso/3).
:- determination(evasao/1,professor_turma/4).
:- determination(evasao/1,resultado_aluno_turma/6).
:- determination(evasao/1,qtd_semestres_trancados/2).
:- determination(evasao/1,tem_facebook/2).
:- determination(evasao/1,tem_twitter/2).
:- determination(evasao/1,cidade/2).
:- determination(evasao/1,classe_idade_aluno/2).
:- determination(evasao/1,classe_idade_professor/2).

:- [cursoAluno,crAluno,corAluno,generoAluno,estadoCivil,anoSemestreIngresso,professorTurma,resultadoAlunoTurma,qtdSemTrancados,temFacebook, temTwitter, cidade, classeIdadeAluno, classeIdadeProfessor].
