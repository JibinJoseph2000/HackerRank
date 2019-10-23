def diagonalDifference(arr):
    p=0
    s=0
    r=0
    for i in range(n):
        p=p+arr[i][i]
    for j in range(0,n):
        s=s+arr[j][n-1-j]
    #print(p)
    #print(s)
    r=p-s
    if(r<0):
        r=r*-1
    return r
n = int(input().strip())
arr = []
for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)