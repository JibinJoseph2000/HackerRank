def birthdayCakeCandles(ar):
    ar.sort()
    max=ar[len(ar)-1]
    x=0
    for i in ar:
        if i==max:
            x=x+1
    print(x)

    
ar_count = int(input())
ar = list(map(int, input().rstrip().split(' ')))
birthdayCakeCandles(ar)