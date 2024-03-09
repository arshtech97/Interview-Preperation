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

# PS: https://atcoder.jp/contests/abc344/tasks/abc344_c

# Preprocess all the possible sums from list a, b, and c
# Then just query the set to get the result. 
def preProcessing(a, b, c, s):
    n, m, l = len(a), len(b), len(c) 

    for i in range(n):
        for j in range(m):
            for k in range(l):
                s.add(a[i] + b[j] + c[k])
            


N = inp()
listA =  inlt()
# Sort every input list

M = inp()
listB = inlt()

L = inp()
listC = inlt()
  

Q = inp()
queries = inlt()

s = set()

preProcessing(listA, listB, listC, s)

for num in queries:
    if num in s:
        print("Yes")
    else:
        print("No")