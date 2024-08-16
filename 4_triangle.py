n=7
space=n-1
star=1
for line in range(n):
    print(" "*space + "@"*star)
    space-=1
    star+=1