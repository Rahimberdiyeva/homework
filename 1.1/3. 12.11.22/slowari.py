x=open('task.txt', encoding="UTF-8").readlines()
print(x)
b={}
for i in x:
    c=i.split(' ')  # разбить строку на элементы
    g=' '.join(c[1:])
    b.update({c[0]:g})
    print(b)
