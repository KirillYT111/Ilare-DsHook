import tkinter as tk
from tkinter import messagebox 

root = tk.Tk()
root.title("Ilare dshoock")

def send():
    res = messagebox.askyesno('Отправка сообщения', 'Вы действительно ходите опубликовать сообщение?')
    if res == False:
        messagebox.showwarning('Ошибка', 'Отправка отменена')  
    if res == True:
        messagebox.showerror('Ошибка')

chk = tk.Checkbutton(root, text="Пинг @everyone")
chk.grid(column=0, row=0)

chk = tk.Checkbutton(root, text="Пинг @here")
chk.grid(column=1, row=0)

#
#

line3 = tk.Label(root, text="Автор")
line3.grid(row=4, column=0)

inputc2 = tk.Entry(root)
inputc2.grid(row=4, column=1)

line4 = tk.Label(root, text="Аватар(URL)")
line4.grid(row=5, column=0)

inputc3 = tk.Entry(root)
inputc3.grid(row=5, column=1)

line5 = tk.Label(root, text="Ссылка(URL)")
line5.grid(row=6, column=0)

inputc5 = tk.Entry(root)
inputc5.grid(row=6, column=1)

#

line1 = tk.Label(root, text="Название")
line1.grid(row=7, column=0)

inputc1 = tk.Entry(root)
inputc1.grid(row=7, column=1)


line6 = tk.Label(root, text="Основной текст")
line6.grid(row=8, column=0)


txt = tk.Text(root, width=30, height=10) 
txt.grid(row=8, column=1)

#

line6 = tk.Label(root, text="Текст подвала")
line6.grid(row=9, column=0)

inputc7 = tk.Entry(root)
inputc7.grid(row=9, column=1)

line6 = tk.Label(root, text="Изоброжение подвала (URL)")
line6.grid(row=10, column=0)

inputc8 = tk.Entry(root)
inputc8.grid(row=10, column=1)

spliter = tk.Label(root, text="""‎
‎""")
spliter.grid(row=11)

line8 = tk.Label(root, text="URL вебхука")
line8.grid(row=12, column=0)

inputc9 = tk.Entry(root)
inputc9.grid(row=12, column=1)

sendbtn = tk.Button(root, text="Отправить", command=send)
sendbtn.grid(row=13, column=0)
root.mainloop()
