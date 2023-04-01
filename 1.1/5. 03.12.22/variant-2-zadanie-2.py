a=int(input("Wwedite a: "))
b=int(input("Wwedite b: "))
c=int(input("Wwedite c: "))
d=int(input("Wwedite d: "))
i=1001
while i>1:
    i-=1
    if a*i**3+b*i**2+c*i+d==0:
        print(i, end=" ")
