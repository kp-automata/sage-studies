#!/usr/bin/env sage -python
"""Finding minimal generating sets of invariant rings k[x1, ..., xn]^G
for finite matrix groups G acting on polynomial rings.

Pipeline: Reynolds operator (optionally guided by Molien series) -> Groebner basis reduction.

"""
from sage.all import *

def find_invariants_reynolds(group, polynomial_ring, use_molien=False):
    """Find invariant polynomials by applying the Reynolds operator to all monomials
    up to degree |G|. If use_molien=True, the Molien series tells us how many
    invariants exist per degree so we skip unnecessary applications.

    Returns (invariants, application_count).

    """
    invariants = []
    applications = 0
    molien = group.molien_series(prec=group.order() + 1) if use_molien else None
    print(f"molien {molien}")
    for degree in range(1, group.order() + 1):
        expected = molien[degree] if use_molien else None
        found = 0
        for exponents in IntegerVectors(degree, polynomial_ring.ngens()):
            if use_molien and found >= expected:
                break
            monomial = polynomial_ring.monomial(*exponents)
            applications += 1
            projected = group.reynolds_operator(monomial)
            if not projected.is_zero():
                invariants.append(projected)
                found += 1
    return invariants, applications

def invariant_pipeline(group, polynomial_ring, use_molien=True):
    """Full pipeline: find invariants via Reynolds operator, then reduce to
    a minimal generating set via Groebner basis. Returns (groebner_basis, application_count)."""
    invariants, applications = find_invariants_reynolds(group, polynomial_ring, use_molien)
    groebner = polynomial_ring.ideal(invariants).groebner_basis()
    print(f"groebner {groebner}")
    print(len(groebner))
    return groebner, applications
