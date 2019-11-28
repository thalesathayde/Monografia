#!/bin/bash

# esse script será usado para cada execução do aleph
# exemplo: qsub -l nodes=1:ppn=8 run_aleph_oscar.sh proteins/aleph/foldsLC/40 proteins/aleph/proteins_test proteins/aleph/proteins 10
#

T='test_evasao'
B='evasao'

DATASET=$(pwd)/
TEST=$(pwd)/$T
BK=$(pwd)/$B
FOLDS=10
DIRLOGS=$(pwd)/$dataset'/logs'
DIRRULES=$(pwd)/$dataset'/rules'
YAP='/usr/local/bin/yap'
ALEPH=$(pwd)/aleph.pl

#echo $TEST

if [ ! -d "$DIRLOGS" ]
then
        mkdir $DIRLOGS
fi

if [ ! -d "$DIRRULES" ]
then
        mkdir $DIRRULES
fi

i=1

while [ $i -le $FOLDS ]
do
        echo $i
        LOG=$DIRLOGS'/log'$i
        RULES=$DIRRULES'/rules'$i
        TESTPOS=$TEST$i'.f'
        TESTNEG=$TEST$i'.n'
        TRAIN=$DATASET'/train_evasao'$i
        #echo $BK
        #echo $TESTPOS
        #echo $TESTNEG
        #echo $TRAIN

        "$YAP" << EOF > /dev/null 2>&1
        consult('$ALEPH').
        read_all('$BK','$TRAIN').
        set(test_pos,'$TESTPOS').
        set(test_neg,'$TESTNEG').
        set(clauselength,10).
        set(noise,10).
        set(nodes,10000).
        set(minpos,2).
        set(i,2).
        set(record,true).
        set(recordfile,'$LOG').
        induce.

		write_rules('$RULES').

	halt.
EOF
	i=$(($i + 1))
done

# importante não colocar espaço antes do EOF
