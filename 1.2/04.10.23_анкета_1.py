import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.title("Анкета")
root.geometry("400x500")
game=[ 
    ("Стратегии ",  tk.IntVar()), 
    ("Три в ряд ",  tk.IntVar()),
    ("Головоломки ",  tk.IntVar()),
    ("Обучающие ",  tk.IntVar()),
    ("Симуляторы ",  tk.IntVar()),
    ("Настольные ",  tk.IntVar()) 
]


btn = ttk.Button(text="Введите свое имя:")
btn.pack(anchor="n", padx=8, pady= 8)

entry = ttk.Entry()
entry.pack(anchor="n", padx=8, pady= 8)

btn = ttk.Button(root, text="Выбирайте вид игры:")
btn.pack(anchor="n", padx=8, pady= 8)

for name, var in game:
        enabled_checkbutton = ttk.Checkbutton(text=name[:name.find('tk.IntVar()')], variable=var)
        enabled_checkbutton.pack(padx=6, pady=6, anchor='n')

enabled_label = ttk.Label(textvariable=var)

def message():
    messagebox.showinfo(title="Информация" , message="результаты сохранены на game.txt")

    label=root.Entry.entry.get()     # получаем введенный текст
    games = [name[:name.find('tk.IntVar()')] for name in game if name[name.find('tk.IntVar()'):].get()]

    def write_txt():
        with open("game.txt", "a", encoding='utf8') as f:
            f.write(f"Имя пользователя: {label}\n")
            f.write("Вид игры: " + ", ".join(games) + "\n")
    
    entry.delete(0, root.END)
    
#def message():

    


btn = tk.Button(root, text="Сохранить и отправить", command=message)
btn.pack(anchor="n", padx=6, pady=6)


btn=tk.Button(root, text="Выход", command=root.destroy)
btn.pack(anchor="n", padx=6, pady=6)

root.mainloop()
