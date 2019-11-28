import sys
import numpy

caminho=sys.argv[1]

dataset = numpy.loadtxt(caminho, delimiter=',')


print(caminho+" => ")
print(dataset.shape)