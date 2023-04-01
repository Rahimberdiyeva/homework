a=int(input("число 1: "))
b=int(input("число 2: "))
c=int(input("число 3: "))
if a>b and a>c:
    print(a)
else:
    if b>a and b>c:
        print(b)
    else:
        if c>a and c>b:
            print(c)
        else:
                print("числа равны ")
