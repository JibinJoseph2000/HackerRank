n=int(input())
list1=[]
# for loop is used for entering the values in the list
for i in range(0,n):
    temp=[]
    name=input()
    grade=float(input())
    temp.append(name)
    temp.append(grade)
    list1.append(temp)
# for loop used for sorting the grades 
for i in range(0,n):
    for j in range(0,n-i-1):
        if(list1[j][1]>list1[j+1][1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
min=list1[0][1]      # Initialising the lowest mark
for i in range(0,n):
    if(list1[i][1]>min):
        min1=list1[i][1]
        break 
list2=[]
l=0
for i in range(0,n):
    if(list1[i][1]==min1):
        l=l+1
        list2.append(list1[i][0])
list2.sort()
for k in range(0,l):
        if(list2[k]!='NULL'):
                print(list2[k])
        else:
                break
