for item in range(1,5):
    for star in range(1,item+1): 
        print("*",end="")
    print()

print("//////////////////////////////////////////////")


for item in range(6,1,-1):
    for star in range(item,1,-1): 
        print("*",end="")
    print()

print("//////////////////////////////////////////////")
n=int(input("enter a number"))
for item in range(n):
    for star in range(item):
        print(" ",end="")
    for star in range(item,n):
        print("*",end="")
    print()

print("//////////////////////////////////////////////")

n=int(input("enter a number"))
for item in range(n,1,-1):
    for star in range(item-1):
        print(" ",end="")
    for star in range(n,item-1,-1):
        print("*",end="")
    print()

