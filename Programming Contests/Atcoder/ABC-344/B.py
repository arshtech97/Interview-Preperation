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

# PS: https://atcoder.jp/contests/abc344/tasks/abc344_b


n = int(input())
result = []
while n != 0:
    result.append(n)
    n = int(input())
result.append(0)
for i in range(len(result)-1, -1, -1):
    print(result[i])

