from __future__ import division
from __future__ import print_function
from generate import *
import math

def manacher(OG):
    """
    Finds all maximal palindromic substrings (MPS) in a given string using Manacher's Algorithm

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

    # starting center
    C = 0
    # starting right boundary
    R = 0

    # for each position in string
    for i in range(2, len(S)-1):
        # find mirror
        mi = 2*C - i

        # if in boundary
        if i < R:
            # if mirror expands beyond left boundary,
            # it will expand beyond right as well
            # so take R - i instead
            if R-i < LPS[mi]:
                LPS[i] = R - i
            # if mirror does not expand beyond boundary,
            # use it
            else:
                LPS[i] = LPS[mi]
            # min function would suffice above

        # regardless, try to expand
        while S[i + LPS[i]+1] == S[i-LPS[i]-1]:
            LPS[i]+=1

        # if i outside of boundary
        # update positions
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

        # update maxes
        if LPS[i] > m:
            m = LPS[i]
            maxes = [math.ceil(i/2) - 1 - m//2]
        elif LPS[i] == m:
            maxes.append(math.ceil(i/2) - 1 - m//2)

    # get positions in original string for return
    strings = []
    for pos in maxes:
        strings.append(OG[int(pos):int(pos+m)])

    return m, maxes, strings


if __name__ == "__main__":

    length = 10**8

    st = genDNA(10**6)

    # run algorithm
    x, y = manacher("ASDFJSJAJFKDASFDFDFDFDF")
    print(x)
    print(y)
