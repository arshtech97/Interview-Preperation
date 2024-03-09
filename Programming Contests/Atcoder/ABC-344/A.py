############ ---- Input Functions ---- ############
# For integer inputs
def inp():
    return(int(input()))

# For taking list inputs
def inlt():
    return(list(map(int,input().split())))

# This function takes string as a input and returns list of characters
def insr():
    s = input()
    return(list(s[:len(s)]))

 # For taking space seperated integer variable inputs.
def invr():
    return(map(int,input().split()))


# Problem Statement: https://atcoder.jp/contests/abc344/tasks/abc344_a

"""
    T.C: O(N)
    S.C: O(1)

"""

# Write the JAVA Code as well once you get time for these Methods.
def removeCharacter1(char_list):
    count = 0 # count of | character
    result = []
    for char in str:
        if char != '|' and (count == 0 or count == 2):
            result.append(char)
        if char == '|':
            count += 1
    return ''.join(result)

"""
    T.C: O(N)
    S.C: O(1)
"""
def removeCharacter(char_list):
    string = ''.join(char_list)
    arr = string.split("|")
    return arr[0] + arr[2]


string = insr()
print(removeCharacter(string))