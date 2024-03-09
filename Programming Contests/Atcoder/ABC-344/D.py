# PS: https://atcoder.jp/contests/abc344/tasks/abc344_d

import sys
import math

sys.setrecursionlimit(10**9)

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))


# TODO: Implement the 2D version as well.

# This function will return minimum number of moves to add strings upto T
# Here T and Bags are constant and just used for referance purpose

cache = {} # We will memoize
# We have two choices:
    # 1. Either we look into bag for strings which makes up the String T
    # 2. Or to ignore the entire bag and check out the next bag. (This is given in question)
def rec(i, S, T, bags, N):
    if (i, S) in cache:
        return cache[(i, S)]

    if i == N or S == T:
        return 0 if S == T else math.inf

    result = math.inf
    # Check whether a string
    for ss in bags[i][1:]:
        if T.startswith(S + ss):
            # Adding +1 Here because we used the string from the bag
            result = min(result, rec(i + 1, S + ss, T, bags, N) + 1)

    # Ignore the all the strings from this bag and go to next bag
    result = min(result, rec(i + 1, S, T, bags, N))

    cache[(i, S)] = result
    return result


# Variation of 0/1 Kanpsack Problem

if __name__ == '__main__':
    # Take the input
    T = input() # String which we want
    lenT = len(T)
    N = int(input()) # Number of bags
    temp = N
    bags = []
    while temp:
        bag = input().split() # ['3' 'ab' 'abc' 'abcd']
        bags.append(bag)
        temp -= 1

    S = "" # initial String
    minimumSteps = rec(0, S, T, bags, N) # Starting Looking from the first bag.
    print(-1 if minimumSteps == math.inf else minimumSteps)
