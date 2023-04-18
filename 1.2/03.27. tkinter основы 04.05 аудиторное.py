from tkinter import*
from tkinter import ttk
def sum_numbers():
    a=int(EntryNum1_en.get())

    b=int(EntryNum2_en.get())

    c=str(a+b)
    EntrySum_12.delete(0,END)
    EntrySum_12.insert(0,c)

root=Tk()
frm=ttk.Frame(root,padding=5)
frm.grid()
ttk.Label(frm,text="Введите числа:").grid(column=0, row=0)
EntryNum1_en=ttk.Entry(frm)    #первое число
EntryNum1_en.grid(column=0,row=1)
ttk.Label(frm,text="").grid(column=1, row=1)
EntryNum2_en=ttk.Entry(frm)    #второе число
EntryNum2_en.grid(column=2,row=1)

EntrySum_12=ttk.Entry(frm)     #сумма
EntrySum_12.grid(column=2, row=3)
ttk.Button(frm,text="Ответ:",command=sum_numbers).grid(column=0, row=3)

root.mainloop()
