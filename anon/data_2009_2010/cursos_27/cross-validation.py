from random import shuffle
import sys

def read_file(namefile):
    examples = []
    fread = open(namefile)
    examples = [line for line in fread]
    fread.close()
    return examples

def set_folds(examples, numfolds):
    dict_folds = {}
    how_many = len(examples) // numfolds;
    print how_many
    j = 0
    for i in range(numfolds-1):
        dict_folds[i] = examples[how_many*i:how_many+how_many*i]
    dict_folds[numfolds-1] = examples[how_many*(numfolds-1):]
    return dict_folds

def shuffle_exs(examples):
    index_shuf = range(len(examples))
    shuffle(index_shuf)
    shuffled_examples = []
    for i in index_shuf:
        shuffled_examples.append(examples[i])
    return shuffled_examples

def write_test_set(dict_folds, prefix, suffix):
    for fold in dict_folds:
        ftest = open(prefix+str(fold+1)+'.'+suffix, 'w')
        for example in dict_folds[fold]:
            ftest.write(example)
        ftest.close()

def write_training_set(dict_folds, prefix, suffix):
    folds = range(len(dict_folds))
    for fold in folds:
        ftraining = open(prefix+str(fold+1)+'.'+suffix, 'w')
        for foldtrain in folds:
            if foldtrain != fold:
                for example in dict_folds[foldtrain]:
                    ftraining.write(example)
        ftraining.close()

def size_file(namefile):
    with open(namefile) as f:
        return sum(1 for _ in f)

def undersampling(inputfile, outputfile, basenumexs):
    index_shuf = range(size_file(inputfile))
    shuffle(index_shuf)
    filein = open(inputfile)
    exs = filein.readlines()
    filein.close()
    fileout = open(outputfile, 'w')
    for i in index_shuf[:basenumexs]:
        fileout.write(exs[i])
    fileout.close()



def create_folds(inputfile, numfolds, prefixtest, suffixtest, prefixtrain, suffixtrain):
    exs = read_file(inputfile)
    exs = shuffle_exs(exs)
    folds = set_folds(exs,int(numfolds))
    write_test_set(folds, prefixtest, suffixtest)
    write_training_set(folds, prefixtrain, suffixtrain)

if sys.argv[1] == 'create_folds':
    create_folds(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

if sys.argv[1] == 'undersampling':
    undersampling(sys.argv[2], sys.argv[3], int(sys.argv[4]))

#python cross-validation.py 'create_folds' evasao.f 10 test_evasao n train_evasao f
