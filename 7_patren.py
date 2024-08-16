n=5
speace=n//2
star=1
num=1
for line in range(n//2+1):
    print(" "*speace +str(num)*star)
    speace-=1
    star+=2
    num+=1
speace=1
star=n//2+1
for line in range(n//2):
    print(" "*speace +str(num)*star)
    speace+=1
    star-=2
    num+=1