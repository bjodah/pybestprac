from libcpp.vector cimport vector

cdef extern from "euclid.h" namespace "euclid":
    cdef vector[double] euclidean_norm(vector[vector[int]] v) except +
