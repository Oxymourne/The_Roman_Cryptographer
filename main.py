import tkinter as tk

original_text = ''
step = ''


def input_text():  # Забираем значения из поля ввода
    global original_text
    original_text = input_field.get("1.0", "end").strip()
    output_field.delete("1.0", "end")
    output_field.insert("1.0", original_text)
    print(step)


window = tk.Tk()
window.title('Римский шифратор')
window.geometry("1280x1024")
window.resizable(False, False)

# Кнопки
'''button_ru = tk.Button(window, text='RU')  # Кнопка Русского языка
button_ru.place(x=100, y=425)
button_eng = tk.Button(window, text='EN')  # Кнопка Английского языка
button_eng.place(x=200, y=425)'''
button_encrypt = tk.Button(window, text='Шифровать', width=12, height=2, command=input_text)  # Кнопка шифрования
button_encrypt.place(x=100, y=425)
button_decrypt = tk.Button(window, text='Дешифровать', width=12, height=2, command=input_text)  # Кнопка дешифрования
button_decrypt.place(x=1091, y=425)
button_ok = tk.Button(window, text='Принять шаг', width=1, height=1)
button_ok.place(x=470, y=450)

# Текстовые блоки
step_field = tk.Entry(window, width=2)
step_field.place(x=450, y=450)
input_field = tk.Text(window)
input_field.place(x=100, y=50, width=1080, height=350)
output_field = tk.Text(window)
output_field.place(x=100, y=624, width=1080, height=350)

# Лейблы
step_label = tk.Label(text='Укажите шаг шифрования')
step_label.place(x=280, y=450)

window.mainloop()
