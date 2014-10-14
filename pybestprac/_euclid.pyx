# distutils: language = c++

from libcpp.vector cimport vector

from euclid cimport euclidean_norm as _euclidean_norm

cpdef list euclidean_norm(vector[vector[int]] v):
    return _euclidean_norm(v)
