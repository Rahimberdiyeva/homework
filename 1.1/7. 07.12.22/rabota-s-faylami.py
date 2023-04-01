import os
b=0
k=0
g=0
for root, dirs, files in os.walk(input('Введите путь к каталогу: ')):
    for i in files:
        if('.jpg' or '.jpeg' or '.gif' or '.png') in i:
            b+=1
        elif('.docx' or '.txt' or '.dat') in i:
            k+=1
        elif '.xlsx' in i:
            g+=1
    file=open(input('Введите имя результирующего файла: '), 'w')
    file.writelines('text files: '+str(k)+ ' graphic files: '+ str(b))
    file.close()
