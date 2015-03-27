__author__ = 'Alessandro.Dantas'

"""
Matrices are somewhat similar to the array objects described in Recipe 3.9, but follow linear algebra rules for
computation. Here is an example that illustrates a few essential features:
"""

import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

print('\nReturn transpose')
print(m.T)

print('\nReturn inverse')
print(m.I)

print('\nCreate a vector and multiply')
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

"""
More operations can be found int the numpy.linalg subpackage. For example:
"""

import numpy.linalg

print('\nDeterminant')
print(numpy.linalg.det(m))

print('\nEigenvalues')
print(numpy.linalg.eigvals(m))

print('\nSolve for x in mv = v')
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)

"""
Linear algebra is obviously a huge topic that's far beyond the scope of this cookbook. However if you need to manipulate
matrices and vectors, NumPy is a good starting point.
"""
