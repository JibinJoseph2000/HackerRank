def timeConversion(l):
    st=[]
    st=l.split(':')
    if('AM' in st[2]):
        a=int(st[0])
        if (a==12):
            print('00'+':'+st[1]+':'+st[2][0]+st[2][1])
        else:
            print(str(st[0])+':'+str(st[1])+':'+str(st[2][0])+str(st[2][1]))
    elif('PM' in st[2]):
        b=int(st[0])
        if (b==12):
            print(str(st[0])+':'+str(st[1])+':'+str(st[2][0])+str(st[2][1]))
        else:
            b=b+12
            print(str(b)+':'+str(st[1])+':'+str(st[2][0])+str(st[2][1]))
if __name__ == '__main__':
    s = input()
    timeConversion(s)