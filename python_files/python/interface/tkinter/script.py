from tkinter import *

# создание окна 
window = Tk()
# заголовок для окна
window.title('Мой первый интервэйс tkinter')

def clicked():
    # получение результата с поля вводы
    res = txt.get()
    # замена текста
    lbl.configure(text='Кнопка сработала' + res, fg='red', font = 20)

# создание текста
lbl = Label(window, text='Hello', font=('Roboto', 50), padx=25, pady=25) # padx=5, pady=5 padding
# положение текста
lbl.grid(column = 0, row = 0)

# создание кнопки
btn = Button(window, text="Кнопка", bg='blue', fg='#fff', command=clicked)
btn.grid(column=1, row=0)

txt = Entry(window, width=50)
txt.grid(column=2,row=0)
# установка фокуса на поле
txt.focus()

# выпадающий список
from tkinter.ttk import Combobox

combo = Combobox(window)
combo['values'] = (1,2,True, 'Текст', '2+2')
combo.current(1) # вариант по умолчанию
combo.grid(column = 0, row = 1)

# checkbutton
from tkinter.ttk import Checkbutton

chk_state = BooleanVar()  
chk_state.set(True)  # задайте проверку состояния чекбокса  
chk = Checkbutton(window, text='Выбрать', var=chk_state)  
chk.grid(column=0, row=2) 

#radiobutton
from tkinter.ttk import Radiobutton  
  
rad1 = Radiobutton(window, text='Первый', value=1)  
rad2 = Radiobutton(window, text='Второй', value=2)  
rad3 = Radiobutton(window, text='Третий', value=3)  
rad1.grid(column=0, row=3)  
rad2.grid(column=1, row=3)  
rad3.grid(column=2, row=3) 

# alert
from tkinter import messagebox  
  
def clicked2():  
    messagebox.showinfo('Заголовок', 'Текст')
    messagebox.askokcancel('Заголовок', 'Текст')

btn2 = Button(window, text='Alert', command=clicked2)  
btn2.grid(column=0, row=4)  

# spinbox
spin = Spinbox(window, from_=0, to=100, width=5)  
spin.grid(column=0, row=5) 

# progressbar
from tkinter.ttk import Progressbar  
from tkinter import ttk  
  
style = ttk.Style()  
style.theme_use('default')  
style.configure("black.Horizontal.TProgressbar", background='black')  
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')  
bar['value'] = 70  
bar.grid(column=0, row=6)

# menu
from tkinter import Menu  
  
menu = Menu(window)  
new_item = Menu(menu , tearoff=0)  
new_item.add_command(label='Новый')
new_item.add_separator()  
new_item.add_command(label='Изменить') 
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  

# files
from tkinter import filedialog

def clicked3():  
    file = filedialog.askopenfilename()
    messagebox.showinfo('Заголовок', file)

btn3 = Button(window, text='Открыть', command=clicked3)  
btn3.grid(column=0, row=7)  
'''
Возможность указания типа файлов доступна при использовании параметра filetypes, однако при этом важно указать расширение в tuples.
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
Вы можете запросить каталог, используя метод askdirectory :
dir = filedialog.askdirectory()
'''

# Notebook
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Первая')  
tab_control.add(tab2, text='Вторая')  
lbl1 = Label(tab1, text='Вкладка 1')  
lbl1.grid(column=0, row=0)  
lbl2 = Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  
tab_control.grid(column=0, row=8)

# размеры окна
window.geometry('1900x900')

# цикл для программы
window.mainloop()