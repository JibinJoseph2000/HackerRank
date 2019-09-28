if __name__ == '__main__':
    x = int(input())    # The integer is one side of the cuboid
    y = int(input())    # The integer is one side of the cuboid
    z = int(input())    # The integer is one side of the cuboid
    n = int(input())
    list1=[]
# for loops are used to maintain the sequence in the list 
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                temp=[]
                temp.append(i)
                temp.append(j)
                temp.append(k)
                if(i+j+k!=n):
                    list1.append(temp)
    
    print(list1)
