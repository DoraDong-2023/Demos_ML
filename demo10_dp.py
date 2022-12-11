# DP Problem:
# Maximize the number of boxes from the given boxes list which obeying the rules as
# Ri>R(i+1) and Hi>H(i+1)

# This problem is actually to find the maximum monotonically decreasing array
# The dynamic programming solution is:
# f(i): the length of maximum monotonically decreasing array
# by the i-th element
# Thus the formula is f(i)=f(j)+1 for j is the index of previous element of i-th element
# To maximum the f(i), we maximum the f(j)
# f(i)=max(f(j)|j<i & a_j>a_i)+1

# Thus the pseudocode is
# initialize f to zero array
# for i in range(1,len(array)):
#    for j in range(i-1):
#        if j-th element> i-th element:
#           f[i] = max(f[i], f[j] + 1)
# To simplify the computation, we insert a number large enough at the beginning of array
# Finally to extract the series, we return it by the index of variation of f

# The time complexity is O(n^2) for n=len(array), space complexity is O(n)




import numpy as np

def dp(array):
    # fi, length of maximum series ended by i
    f=np.zeros((len(array)))
    for i in range(1,len(array)):
        for j in range(i):
            if array[j][0]>array[i][0] and array[j][1]>array[i][1]:
                f[i] = max(f[i], f[j] + 1)
    # return the series
    series = []
    for i in range(1,len(f)-1):
        if f[i]+1==f[i+1]:
            series.append(array[i])
    if f[-1]==f[-2]+1:
        series.append(array[-1])
    
    return series, f
    


a=[[10000000000,10000000], [1,1.5], [6,5], [3,4], [5,2], [4,1], [3,0.5]]

series, f = dp(a)
print(series)
print(f)
