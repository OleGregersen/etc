import numpy

n, m = [int(x) for x in input().strip().split()]
a = numpy.array([[int(x) for x in input().strip().split()] for _ in range(n)], dtype = float)
print(numpy.mean(a, axis = 1))
print(numpy.var(a, axis = 0))
s = numpy.around(numpy.std(a), 11)
print(s)
