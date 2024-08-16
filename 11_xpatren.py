var=5
space=var-1
star=1
for line in range(var):
    for line in range(space):
        print(" ",end=" ")
    for line in range(star):
        print(star,end=" ")
    space-=1
    star+=1
    print()