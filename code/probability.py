"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot


def MakeFigures(firsts, others):
    """Plot Pmfs of pregnancy length.

    firsts: DataFrame
    others: DataFrame
    """
    # plot the PMFs
    first_pmf = thinkstats2.Pmf(firsts.prglngth, label='first')
    other_pmf = thinkstats2.Pmf(others.prglngth, label='other')

    width = 0.45
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_pmf, align='right', width=width)
    thinkplot.Hist(other_pmf, align='left', width=width)

    thinkplot.Save(root='probability_nsfg_pmf',
                   title='PMF',
                   xlabel='weeks',
                   ylabel='probability',
                   axis=[27, 46, 0, 0.6])

    # plot the differences in the PMFs
    weeks = range(35, 46)
    diffs = []
    for week in weeks:
        p1 = first_pmf.Prob(week)
        p2 = other_pmf.Prob(week)
        diff = 100 * (p1 - p2)
        diffs.append(diff)

    thinkplot.Bar(weeks, diffs)
    thinkplot.Save(root='probability_nsfg_diffs',
                   title='Difference in PMFs',
                   xlabel='weeks',
                   ylabel='percentage points',
                   legend=False)


def main(script):
    live, firsts, others = first.MakeFrames()
    MakeFigures(firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)

