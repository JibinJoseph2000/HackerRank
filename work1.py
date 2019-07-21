if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if(n>=2):
        for i in range(n):
            if(arr[i]>=-100 and arr[i]<=100):
                    arr.sort()
    max=arr[n-1]
    j=n-1
    while(j>-1000):
        if(arr[j]<max):
            print(arr[j])
            break
        else:
            j=j-1


