import os, psutil

# 1
def task_1(a, b, c):
     d = b
     b, c, a = c, a, d
     return a,b,c
#2_1
def task_2_1(a,b):
   return a+b
#2_2 
def task_2_2(a):
    return a
# 3_1
def task_3_1(x):
    return x**5
# 3.2
def task_3_2(x):
    for _ in range(0,5):
        x*=x
    return x
# 4
def task_4(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a == n:
        return 'Yes'  
    else:
        return 'No'
# 5
def task_5(n):
    if n == 1 or n == 2 or n == 12:
        return 'Зима'
    if n == 3 or n == 4 or n ==5 :
        return 'Весна'
    if n == 6 or n == 7 or n == 8 :
        return 'Лето'
    if n == 9 or n == 10 or n == 11 :
        return 'Осень'
    
    match n:
        case 1: return 'Зима'
        case 2: return 'Зима'
        case 12: return 'Зима'

        case 3: return 'Весна'
        case 4: return 'Весна'
        case 5: return 'Весна'

        case 6: return 'Зима'
        case 7: return 'Зима'
        case 8: return 'Зима'

        case 9: return 'Лето'
        case 10: return 'Лето'
        case 11: return 'Лето'
# 6
def task_6(n):
    s = 0 
    s_1 = 0
    for i in range(n):
        b = int(input(f"Введите число {i + 1}: "))
        if  b % 2 == 0:
            s += b
        else:
            s_1 += b
    return 'сумма четных чисел =' , s, 'сумма нечетных чисел =', s_1
# 7
# 8
def task_8(n,m):
    l = False
    for i in range (n,m+1):
        for j in range (i+1,m+1):
            for k in range (n,m+1):
                if i**2 + j**2 == k**2:
                    return (i, j, k)
                    l = True
    if l == False:
        return 'NO'
# 9
def task_9(n,m):
    l = False
    for i in range (n,m+1):
        t, k = i, 0
        while t!=0:
            k+= t%10
            t/=10
        if i % k ==0:
            return i
            l = True
    if l == False:
        return 'No'
# 10
def task_10(n):
    i=k=0
    while i!=n:
        k+=1
        s=0
        for _ in range(k+1):
            if k%_ == 0:
                s+= _
        if k == s:
            return k
            i+=1
# 11
def task_11(a):
    return a[-1]
    
# 12
def task_12(a):
    a.reverse()
    return a
# 13
def task_13(a):
    if len(a) ==0:
        return 0
    else:
        return a[0] + task_13(a[1:])
# 14
# 15
def print_task_15(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(f"{i} x {j} = {i * j}\t", end="")
        print()  # Переход на новую строку после каждой строки таблицы
# 16
while( True):
     cmd = input('Выберите задачу: ')
     match cmd:
        case 'task_1':
            a, b, c = map (int, input().split())
            print(task_1(a, b, c))
        
        case 'task_2_1':
            while True:
                try:
                    a = float (input('Введите первое число:')) 
                    b = float( input('Введите второе число:'))
                    break
                except ValueError:
                    print( 'ошибка')
            print(task_2_1(a,b))

        case 'task_2_2':
            n = int(input("Введите количество чисел: "))
            a = []
            for i in range(n):
                k = False
                while True:
                        b = float(input(f"Введите число {i + 1}: "))
                        if b not in a:
                            a.append(b)
                            k = True
                            break
            print(task_2_2(a))

        case 'task_3_1':
             x = int (input('Введите х:'))
             print(task_3_1(x))
           

        case 'task_3_2':
             x = int (input('Введите х:'))
             print(task_3_2(x))

        case 'task_4':
             n = int (input('Введите n:'))
             print(task_4(n))

        case 'task_5':
             n =int( input('Введите нoмер месяца:'))
             
             print(task_5(n))

        case 'task_6':
             n = int (input('Введите n:'))
          
             print(task_6(n))
        case 'task_8':
             n , m = map(int(input().slpit()))
             print(task_8(n,m))

        case 'task_9':
             n , m = map(int(input().slpit()))
             print(task_9(n,m))
        
        case 'task_10':
             n = int(input())
             print(task_9(n))

        case 'task_11':
             print ("Задайте элементы массива: ")
             a = [int(i) for i in input().split()]
             print(task_11(a))
             a.reverse()
             print("второй способ:", a[0])
             a.reverse()
             print("третий способ:",a.pop())

        case 'task_12':
             print ("Задайте элементы массива: ")
             a = [int(i) for i in input().split()]
             print(task_12(a))

        case 'task_13':
             print ("Задайте элементы массива: ")
            #  s = 0
             a = [int(i) for i in input().split()]
             print(task_13(a))
        
        case 'task_15':
            n = int(input("Введите количество строк: "))
            m = int(input("Введите количество столбцов: "))
            print_task_15(n, m)

        case 'X':
            break