from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

now = datetime.now()
pres_year = int(now.year)


def calculate_age():
    if isinstance(year_of_birth_vvod.get(), str) and year_of_birth_vvod.get().isnumeric():
        age = pres_year - int(year_of_birth_vvod.get())
        messagebox.showinfo('Возраст', f'Ваш возраст = {age}')
    else:
        messagebox.showinfo('Возраст', f'Год рождения введен неправильно')


window = Tk()
window.title('Расчет возраста')
window.geometry('400x200')

Frame = ttk.Frame(window)
Frame.pack(padx=20, pady=20)

year_of_birth = ttk.Label(
    Frame,
    text="Введите свой год рождения  "
)
year_of_birth.grid(row=3, column=1)

present_year = ttk.Label(
    Frame,
    text="Текущий год  ",
)
present_year.grid(row=4, column=1)

present_year_value = ttk.Label(
    Frame,
    text = pres_year
)
present_year_value.grid(row=4, column=2)


year_of_birth_vvod = ttk.Entry(
    Frame,
    justify = CENTER
)
year_of_birth_vvod.grid(row=3, column=2, pady=5)

cal_btn = Button(
    Frame,
    text='Рассчитать возраст',
    command=calculate_age
)
cal_btn.grid(row=5, column=2)

window.mainloop()