def two_sum(S, x):
    S.sort()
    j = len(S) -1
    i = 0
    while i < j:
        if S[i] + S[j] == x:
            return True
        elif S[i] + S[j] < x:
            i = i +1
        else:
            j = j+1
    return False

x = 4
S =[1, 2, 3, 4, 5]
print(two_sum(S,x))
