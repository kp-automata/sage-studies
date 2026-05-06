#!/usr/bin/env sage -python
"""Benchmark: naive vs Molien-guided Reynolds operator.
Measures application count and wall time across multiple groups.
"""
from sage.all import *
from invariants import invariant_pipeline
import time

def benchmark_group(group, polynomial_ring, name, num_runs=1):
    print("===", name, "| order:", group.order(), "| vars:", polynomial_ring.ngens(), "===")

    # Warmup — Sage caches some group computations on first call
    invariant_pipeline(group, polynomial_ring, use_molien=False)

    # Naive
    naive_times = []
    for run in range(num_runs):
        start = time.perf_counter()
        naive_groebner, naive_applications = invariant_pipeline(group, polynomial_ring, use_molien=False)
        naive_times.append(time.perf_counter() - start)

    # Molien-guided
    molien_times = []
    for run in range(num_runs):
        start = time.perf_counter()
        molien_groebner, molien_applications = invariant_pipeline(group, polynomial_ring, use_molien=True)
        molien_times.append(time.perf_counter() - start)

    naive_median = sorted(naive_times)[num_runs // 2]
    molien_median = sorted(molien_times)[num_runs // 2]
    speedup = naive_median / molien_median if molien_median > 0 else float('inf')

    print(f"  Naive:  {naive_applications} apps, {naive_median:.4f}s (median of {num_runs})")
    print(f"  Molien: {molien_applications} apps, {molien_median:.4f}s (median of {num_runs})")
    print(f"  Speedup: {speedup:.1f}x")
    print()

    return naive_applications, molien_applications, speedup

if __name__ == '__main__':
    benchmark_group(
        MatrixGroup(SymmetricGroup(3)),
        PolynomialRing(QQ, 'x, y, z'),
        'S3')

    benchmark_group(
        MatrixGroup(SymmetricGroup(4)),
        PolynomialRing(QQ, 'x1, x2, x3, x4'),
        'S4')

    benchmark_group(
        MatrixGroup(DihedralGroup(6)),
        PolynomialRing(QQ, 'x1, x2, x3, x4, x5, x6'),
        'D6')
