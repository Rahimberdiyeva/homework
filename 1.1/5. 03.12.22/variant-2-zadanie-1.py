n=int(input("Введите число: "))
k=0
for i in range(1,n+1):
    for j in range(1,i+1):
       k+=1
       if k<=n:
            print(i, end=" ")
       else:
           break
           
       
           
   

