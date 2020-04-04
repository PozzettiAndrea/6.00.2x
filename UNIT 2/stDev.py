def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np
    import math
    
    result = 0
    
    if len(L) == 0:
        result = float('NaN')

    lengths = [len(x) for x in L]

    mean = math.fsum(lengths)/len(lengths)
    result = math.sqrt(sum([(x - mean)**2 for x in lengths])/float(len(L)))
    return result