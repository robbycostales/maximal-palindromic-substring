from __future__ import division
from __future__ import print_function
from generate import *
import math

def naiveON2(OG):
    """
    Finds all maximal palindromic substrings (MPS) in a given string using quadratic approach

    Args:
        OG - (str)
    Returns:
        m - (int) length of MPS(s)
        maxes - (list of ints) starting positions of occurences
        strings - (list of strings) maximal palindromic substrings
    """

    # process string into form for algorithm
    # have *'s separating characters, and @ at beg. and ! at end
    # will make finding even vs odd length seamless
    S = "@*" + "".join([x + "*" for x in list(OG)]) + "!"

    # to store the lengths of palindromes at each location
    # Longest Palindromic Substring (centered at each position)
    LPS = [0 for i in range(len(S))]

    # will store center positions of current max-lengths
    maxes = []
    # max value
    m = 0

    # for each position in string
    for pos in range(1, len(S)-1):
        i = 0
        # always expand...
        while True:
            cl = S[pos-i-1]
            cr = S[pos+i+1]
            if cl == cr:
                i+=1
            # ... until the characters do not match
            else:
                break

        # update LPS at i
        LPS[pos] = i
        # update maxes
        if i > m:
            m = i
            maxes = [math.ceil(pos/2) - 1 - m//2]
        elif i == m:
            maxes.append(math.ceil(pos/2) - 1 - m//2)

    # get positions in original string for return
    strings = []
    for pos in maxes:
        strings.append(OG[int(pos):int(pos+m)])

    return m, maxes, strings


if __name__ == "__main__":

    length = 10**6

    st = genDNA(10**6)

    # run algorithm
    x, y, z, s = naiveON2("ASDFJSJAJFKDASFDFDFDFDF")
    print(length)
    print(x)
    print(y)
