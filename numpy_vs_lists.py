'''
Nathaniel Yee

'''

import numpy as np
import time
import sys

def list_version(length):
    tstart = time.time()

    # allocating lists
    X = list(range(length))
    Y = list(range(length))
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    tend = time.time()
    runtime = tend - tstart
    print('Using Numpy:')
    print('Length of List:', len(Z))
    print('Size of the List:', sys.getsizeof(Z))
    print('Runtime:', runtime)
    return runtime

def numpy_version(length):
    tstart = time.time()

    # allocating lists
    X = np.arange(length)
    Y = np.arange(length)
    Z = X + Y
    tend = time.time()
    runtime = tend - tstart
    print('Using Lists:')
    print('Length of List:', len(Z))
    print('Size of the List:', sys.getsizeof(Z))
    print('Runtime:', runtime)
    return runtime
    pass

def main():
    length = 10000000
    list_runtime = list_version(length)
    numpy_runtime = numpy_version(length)
    print(list_runtime, numpy_runtime)
    print(f"Numpy is {list_runtime / numpy_runtime} times faster")
    pass


# only call main when running it as main program
# if you're importing then you are not running it as the main program
if __name__ == "__main__":
    main()