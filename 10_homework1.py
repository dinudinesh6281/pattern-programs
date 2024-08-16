var=7
space=0
num=var
for line in range(1,var+1):
    for line in range(space):
        print(" ",end=" ")
    for line in range(num):
        print(num,end=" ")
    space+=1
    num-=1
    print()
