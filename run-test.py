from manacher import *
from naive_2 import *
from generate import *
import time
import cProfile as cp

if __name__ == "__main__":
    length = 10**4

    alph = "A"
    st = genDNA(length, alph)
    print("Alphabet: \t{}".format(list(alph)))
    print("Length: \t{}".format(length))


    start = time.time()
    # run algorithm
    x, y, z = naiveON2(st)
    end = time.time()
    print("NAIVE 0(N^2): \t{}".format(end - start))


    start = time.time()
    # run algorithm
    x, y, z = manacher(st)
    end = time.time()
    print("MANACHER 0(N): \t{}".format(end - start))


    # cp.run("manacher(st)")
