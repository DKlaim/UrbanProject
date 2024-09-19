import tkinter as tk  # tkinter - библиотека графического интерфейса (as tk переназначает обращение к библиотеке на tk)


window = tk.Tk()  # Создаём переменную окна для дальнейшего наполнения
# Всё что будет относиться к будущему окну window, должно находится между window = tk.Tk() и window.mainloop()
window.title('Калькулятор')  # название окна
window.geometry('350x350')  # задаём размер окна
window.resizable(False, False)  # блокируем возможность изменения размера окна

# Создаём виджеты (элементы окна)
button_add = tk.Button(window, width=5, height=3, text='+')  # Создаём переменную кнопки, привязываем к нашему окну, задаём размеры и добавляем текстовое наполнение
button_add.place(x=100, y=200)  # метод .place размещает виджет в окне по координатам

button_sub = tk.Button(window, width=5, height=3, text='-')
button_sub.place(x=150, y=200)

button_mul = tk.Button(window, width=5, height=3, text='*')
button_mul.place(x=200, y=200)

button_div = tk.Button(window, width=5, height=3, text='/')
button_div.place(x=250, y=200)

number1_entry = tk.Entry(window, width=32)  # Создаём переменную текстового поля для ввода, привязываем к нашему окну, задаём ширину
number1_entry.place(x=100, y=62)

number2_entry = tk.Entry(window, width=32)
number2_entry.place(x=100, y=106)

answer_entry = tk.Entry(window, width=32)
answer_entry.place(x=100, y=150)

number1 = tk.Label(window, text='Введите первое число')  # Создаём переменную для надписи, привязываем к нашему окну
number1.place(x=100, y=40)

number2 = tk.Label(window, text='Введите второе число')
number2.place(x=100, y=84)

answer = tk.Label(window, text='Ответ')
answer.place(x=100, y=128)

window.mainloop()  # Запускаем цикл обновления событий (.mainloop обновляет информацию о происходящем на экране)

