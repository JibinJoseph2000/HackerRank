def kangaroo(x1, v1, x2, v2,f):
    p=x1
    q=x2
    for i in range(10000):
        p=p+v1
        q=q+v2
        if(p==q):
            f=1
            print("YES")
            break
    return f
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
f=0
f=kangaroo(x1, v1, x2, v2,f)
if(f==0):
    print("NO")