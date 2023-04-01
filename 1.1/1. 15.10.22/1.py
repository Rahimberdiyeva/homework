def calc(a,b,c):
    if c=='+':
        return(a+b)
    elif c=='-':
        return(a-b)
    elif c=='*':
        return (a*b)
    elif c=='/':
        return (a/b)
    elif c=='//':
        return(a//b)
    else:
        return (a%b)
    try:
        a=int(input("1 число: "))
        b=int(input("2 число: "))
        c='c'
        while c!='+' and c!='-' and c!='*' and c!='/' and c!='//' and c!='%':
            c=str(input("Операции(+,-,*,/,//, %): "))
            try:
                print(calc(a,b,c))
            except ZerodivisionError :
                print("Бесконечность.")
    except ValueError:
            print("Не число, попробуйте снова.")
