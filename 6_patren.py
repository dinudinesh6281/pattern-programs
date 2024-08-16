n=9
speace=n//2
star=1
for line in range(n//2+1):
    print(" "*speace +"@"*star)
    speace-=1
    star+=2
speace=1
star=n-2
for line in range(n//2):
    print(" "*speace +"@"*star)
    speace+=1
    star-=2
