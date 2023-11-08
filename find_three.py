def find_three(a,b,c,AR):
    if a < b:
        small = a
        large = b
    else:
        small = b
        large = a

    if large < c:
        mid = large 
        large = c
    else:
        mid = c

    if mid < small:
        tmp = small 
        small = mid
        mid = tmp

    BR = []
    CR = []
    RR = [0, 0, 0]  # tracks if a number is found for a, b, c respectively

    for i in range(len(AR)):
        print(AR[i],mid)
        if AR[i] > mid:
            BR.append(AR[i])
        elif AR[i] < mid:
            CR.append(AR[i])
        else:
            RR[1] = 1

    for i in range(len(BR)):
        if BR[i] == large:
            RR[2] = 1

    for i in range(len(CR)):
        if CR[i] == small:
            RR[0] = 1

    # returns the result array, where a 1 in each location means
    # a, b, and c were found
    return RR

AR = [4, 7, 12, 2, 8]
result = find_three(1,9,-1,AR)
print(result)

