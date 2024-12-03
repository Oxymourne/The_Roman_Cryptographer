import tkinter as tk

original_text = ''
step = ''


def input_text():  # Забираем значения из поля ввода
    global original_text, step
    flag = True
    step = step_field.get().strip()
    if step == '':
        flag = False
    for digit in step:
        if not digit.isdigit():
            flag = False
    if flag is True:
        step = int(step)
        original_text = input_field.get("1.0", "end").strip()
        output_field.delete("1.0", "end")
        output_field.insert("1.0", encryption(original_text, step))
        error_label.place_forget()
    else:
        error_label.place(x=500, y=550)


def clear_input():  # Очистка окна ввода
    input_field.delete("1.0", "end")


def encryption(text, encryption_step):
    new_text = ''
    for i in range(len(text)):
        ascii_code = ord(text[i])
        if 32 <= ascii_code <= 126:  # Условие нахождения символа в таблице символов и инагл алфавита
            if ascii_code + encryption_step > 126:
                new_text += chr(ascii_code - 95 + encryption_step)
            else:
                new_text += chr(ascii_code + encryption_step)
        if 1040 <= ascii_code <= 1103:  # Условие нахождения в Русской части символов
            if ascii_code + encryption_step > 1103:
                new_text += chr(ascii_code - 64 + encryption_step)
            else:
                new_text += chr(ascii_code + encryption_step)
        else:
            new_text += text[i]

    return new_text


window = tk.Tk()
window.title('Римский шифратор')
window.geometry("1280x1024")
window.resizable(False, False)

# Кнопки
button_clear = tk.Button(window, text='Очистить', width=12, height=2, command=clear_input)  # Кнопка очистки поля ввода
button_clear.place(x=950, y=525)
'''
button_eng = tk.Button(window, text='EN')  # Кнопка Английского языка
button_eng.place(x=200, y=425)'''
button_encrypt = tk.Button(window, text='Шифровать', width=12, height=2, command=input_text)  # Кнопка шифрования
button_encrypt.place(x=100, y=525)
button_decrypt = tk.Button(window, text='Дешифровать', width=12, height=2, command=input_text)  # Кнопка дешифрования
button_decrypt.place(x=1090, y=525)

# Текстовые блоки
step_field = tk.Entry(window, width=4)
step_field.place(x=450, y=550)
input_field = tk.Text(window)
input_field.place(x=100, y=150, width=1080, height=350)
output_field = tk.Text(window)
output_field.place(x=100, y=624, width=1080, height=350)

# Лейблы
step_label = tk.Label(window, text='Укажите шаг шифрования')
step_label.place(x=280, y=550)
error_label = tk.Label(window, text='Введите число', fg="#ff0000")
header_label = tk.Label(window, text='The Roman cryptographer', font=("Arial", 32, "bold"), anchor="center")
header_label.place(x=350, y=50)

window.mainloop()
