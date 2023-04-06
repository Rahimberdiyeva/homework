#1. Удвоить каждый элемент коллекции.
def first(x):
    return x*2
a=[1,2,3,4,5,6]
new_a=list(map(first,a))
print(new_a)
print('---------')
#2. Найти произведение по-элементно элементов из трех коллекций.
b=[3,7,8,9,9,8]
composition_list=[]
x=-1
for i,j,k in zip(a,new_a,b):
    x+=1
    composition_list.insert(x,i*j*k)
print(composition_list)
print('--------')
#3. Найти длину каждого элемента из коллекции.
str_composition_list=list(map(lambda x: len(str(x)),composition_list))
print(str_composition_list)
print('--------')
#4. Оставить только четные элементы коллекции.
x=0
def filtr(x):
    return x%2==0
c=[12,34,954,34343,121213,0,987,343,34657,345,34212]
filter_c=list(filter(filtr,c))
print(filter_c)
print('--------')
#5. Оставить только непустые элементы коллекции.
c=[12,34,0,34343,0,0,987,0,34657,0,34212,1,0,9,87,0,0,0,234,1,0]
c_none=list(filter(None,c))
print(c_none)
print('--------')
#6. Есть три коллекции, нужно упаковать элементы тройками.
list_123=list(zip(new_a,b,c_none))
print(list_123)
print('--------')
#7. Есть две коллекции, нужно упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.
list_122=list(zip(new_a,list(map(lambda x:x*2,c_none))))
print(list_122)
