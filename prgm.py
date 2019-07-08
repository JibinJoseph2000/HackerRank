n=int(input())
list1 = list(map(int , input().split() ))
list1.sort()
if(list1[0]>0):
    for i in range(0,n):
        a=list1[i]
        t=list1[i]
        r=0
        while(a>0):
            d=a%10
            r=(r*10)+d
            a=a//10
        if(r==t):
            print("True")
            break
    else:
        print("False")
else:
    print("False")
    