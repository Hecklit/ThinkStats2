"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    femResp = ReadFemResp()
    femPreg = nsfg.ReadFemPreg()
    pregMap = nsfg.MakePregMap(femPreg)
    pregancies = {};
    print(femResp.pregnum.value_counts().sort_index())

    for key, value in pregMap.items():
        if len(value) in pregancies:
            pregancies[len(value)] += 1
        else:
            pregancies[len(value)] = 1
    
    print(pregancies);
    print('%s: All tests passed.' % script)



if __name__ == '__main__':
    main(*sys.argv)
