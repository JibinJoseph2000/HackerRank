def aVeryBigSum(ar):
    s=0
    for i in ar:
        s=s+int(i)
    return s

n = int(input())
ar = list(map(int, input().rstrip().split()))
result = aVeryBigSum(ar)
print(result)