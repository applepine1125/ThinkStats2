from __future__ import print_function

import numpy as np
import nsfg
import thinkstats2
import thinkplot

def PmfMean(pmf):
    mean = 0.0
    for x, p in pmf.Items():
        mean += p * x
    return mean


def PmfVar(pmf):
    var = 0.0
    mean = PmfMean(pmf)
    for x, p in pmf.Items():
        var += p*(x - mean)**2
    return var

def main():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    pmf = thinkstats2.Pmf(live.prglngth)

    assert(pmf.Mean() == PmfMean(pmf))
    assert(pmf.Var() == PmfVar(pmf))
    print('All test pased')

if __name__ == '__main__':
    main()
