def plusMinus(arr):
    l=len(arr)
    p=0
    n=0
    z=0
    for i in arr:
        if i>0:
            p=p+1
        elif i<0:
            n=n+1
        else:
            z=z+1
    print('{:0.6f}'.format((p/l)))
    print('{:0.6f}'.format((n/l)))
    print('{:0.6f}'.format((z/l)))
n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)
