#!/usr/bin/env sage -python
"""Examples showing the invariant pipeline across various finite groups.
"""

from sage.all import *
from invariants import invariant_pipeline

def cyclic_group_example():
    # C8 acting on k[x,y] via rotation by pi/4 — toy example from the book
    print("=== C8 on 2 variables ===")
    polynomial_ring = PolynomialRing(CyclotomicField(8), 'x, y')
    cyclotomic_field = CyclotomicField(8)
    zeta = cyclotomic_field.gen()
    rotation = (zeta + zeta**(-1)) / 2  # cos(pi/4) = sin(pi/4) = sqrt(2)/2
    group = MatrixGroup([matrix(cyclotomic_field, [[rotation, -rotation], [rotation, rotation]])])
    invariant_pipeline(group, polynomial_ring)

def symmetric_group_example():
    # S3 acting on k[x,y,z] via permutation matrices
    # Naive: 84 monomials up to degree 6 (|S3|=6)
    print("=== S3 on 3 variables ===")
    group = MatrixGroup(SymmetricGroup(3))
    polynomial_ring = PolynomialRing(QQ, 'x, y, z')
    invariant_pipeline(group, polynomial_ring)

def id_group_example():
    # Group {I, -I} acting on k[x,y]
    print("=== {I, -I} on 2 variables ===")
    identity = matrix(QQ, [[1, 0], [0, 1]])
    neg_identity = matrix(QQ, [[-1, 0], [0, -1]])
    group = MatrixGroup([identity, neg_identity])
    polynomial_ring = PolynomialRing(QQ, 'x, y')
    invariant_pipeline(group, polynomial_ring)

def dihedral_group_example():
    # D4 acting on k[x,y,z,w] via reflections and rotations, |D4|=8
    print("=== D4 on 4 variables ===")
    group = MatrixGroup(DihedralGroup(4))
    polynomial_ring = PolynomialRing(QQ, 'x, y, z, w')
    invariant_pipeline(group, polynomial_ring)


def symmetric_group_s4_example():
    # S4 acting on k[x1,x2,x3,x4] via permutation matrices
    # Naive: huge number of monomials up to degree 24
    print("=== S4 on 4 variables ===")
    group = MatrixGroup(SymmetricGroup(4))
    polynomial_ring = PolynomialRing(QQ, 'x1, x2, x3, x4')
    invariant_pipeline(group, polynomial_ring)


def icosahedral_group_example():
    # A5 (icosahedral symmetry) acting on 5 variables, order 60
    print("=== A5 on 5 variables ===")
    group = MatrixGroup(AlternatingGroup(5))
    polynomial_ring = PolynomialRing(QQ, 'x1, x2, x3, x4, x5')
    invariant_pipeline(group, polynomial_ring)


def binary_icosahedral_example():
    # Binary icosahedral group (2I), order 120, acts on 2 variables
    # Double cover of A5, related to the icosahedron. Classical invariant theory.
    print("=== Binary Icosahedral (2I) on 2 variables ===")
    K = CyclotomicField(5)
    zeta = K.gen()
    # Generators of the binary icosahedral group in SL(2, C)
    gen_s = matrix(K, [[zeta, 0], [0, zeta**(-1)]])
    gen_t = matrix(K, [[0, 1], [-1, 0]])
    group = MatrixGroup([gen_s, gen_t])
    polynomial_ring = PolynomialRing(K, 'x, y')
    invariant_pipeline(group, polynomial_ring)


if __name__ == '__main__':
    id_group_example()
    print()
    cyclic_group_example()
    print()
    symmetric_group_example()
    print()
    dihedral_group_example()
    print()
    symmetric_group_s4_example()
    print()
    binary_icosahedral_example()
    print()
    icosahedral_group_example()