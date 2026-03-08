#!/usr/bin/env python3
"""
Poisson test: Compare observed mutations vs literature expectation
Usage: python poisson_test.py <days> <observed_mutations>
Example: python poisson_test.py 26 25
"""

import sys
import argparse
from scipy.stats import chi2, poisson
from mpmath import mp, mpf

# Set high precision for tiny p-values
mp.dps = 50

# Literature parameters (fixed)
lit_rate_bp_cycle = 3.4e-5   # mutations/bp/cycle
cycle_days = 1.2             # days per replication cycle
bp_region = 2500             # base pairs in region

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Poisson test for mutation rate vs literature')
    parser.add_argument('days', type=float, help='Number of observation days')
    parser.add_argument('observed_mutations', type=int, help='Number of mutations observed')
    args = parser.parse_args()
    
    days = args.days
    x = args.observed_mutations
    
    # Calculate literature expectation
    cycles = days / cycle_days
    mu_expected = bp_region * lit_rate_bp_cycle * cycles
    
    alpha = 0.01  # 99% confidence
    
    # 1. Exact 99% Poisson CI for total mutations over observation period
    mu_low = 0.5 * chi2.ppf(alpha/2, 2*x)
    mu_high = 0.5 * chi2.ppf(1 - alpha/2, 2*(x + 1))
    
    print(f"Observed: {x} mutations over {days} days")
    print(f"Literature expectation: {mu_expected:.2f} mutations over {days} days")
    print(f"99% Poisson CI: [{mu_low:.1f}, {mu_high:.1f}]")
    print(f"Literature value is {'INSIDE' if mu_expected >= mu_low and mu_expected <= mu_high else 'OUTSIDE'} the CI")
    
    # 2. One-sided p-value: P(X >= observed | μ = expected) - HIGH PRECISION
    mu_mp = mpf(mu_expected)
    x_mp = mpf(x)
    
    p_value_mp = mpf('0')
    for k in range(x, 100):  # sum until terms become negligible
        term = mp.exp(-mu_mp) * (mu_mp**k) / mp.factorial(k)
        p_value_mp += term
        if term < 1e-50:
            break
    
    p_value_str = f"{float(p_value_mp):.2e}"
    print(f"\nOne-sided p-value (P(X >= {x} | μ = {mu_expected:.2f})): {p_value_str}")
    print("p < 0.001" if float(p_value_mp) < 0.001 else f"p = {float(p_value_mp):.4f}")
    
    # 3. Rate comparison
    rate_ratio = x / mu_expected
    print(f"Your observed rate is {rate_ratio:.1f}x the literature rate")
    
    # 4. Summary
    print(f"\n{'✓' if mu_expected < mu_low else '✗'} Significantly higher than literature (99% CI excludes expectation)")

if __name__ == "__main__":
    main()
