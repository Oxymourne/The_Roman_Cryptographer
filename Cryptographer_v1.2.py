import tkinter as tk


def decryption_true():
    global decryption_flag
    decryption_flag = True


def decryption_false():
    global decryption_flag
    decryption_flag = False


def call_functions_encryption():
    decryption_false()
    encryption_text()


def call_functions_decryption():
    decryption_true()
    encryption_text()


def encryption_text():  # Забираем значения из поля ввода шифруем и передаем в поле вывода
    global original_text, decryption_flag
    original_text = ''
    try:
        step = int(step_field.get().strip())
    except:
        error_label.place(x=335, y=325)
    else:
        if decryption_flag is False:
            original_text = input_field.get("1.0", "end").strip()
            output_field.delete("1.0", "end")
            output_field.insert("1.0", encryption(original_text, step))
            error_label.place_forget()
        else:
            original_text = input_field.get("1.0", "end").strip()
            output_field.delete("1.0", "end")
            output_field.insert("1.0", encryption(original_text, -step))
            error_label.place_forget()


def clear_input():  # Очистка окна ввода
    input_field.delete("1.0", "end")
    output_field.delete("1.0", "end")


def encryption(text, encryption_step):  # Функция Шифрования
    new_text = ''
    for i in range(len(text)):
        ascii_code = ord(text[i])
        if 32 <= ascii_code <= 126:  # Условие нахождения символа в таблице символов и инагл алфавита
            new_text += chr(((ascii_code - 32 + encryption_step) % 95 + 95) % 95 + 32)
        elif 1040 <= ascii_code <= 1103:  # Условие нахождения в Русской части символов
            new_text += chr(((ascii_code - 1040 + encryption_step) % 64 + 64) % 64 + 1040)
        else:
            new_text += text[i]

    return new_text


original_text = ''
decryption_flag = True

window = tk.Tk()
window.title('Римский шифратор')
window.geometry("800x600")
window.resizable(False, False)

# Кнопки
button_clear = tk.Button(window, text='Очистить', width=12, height=2, command=clear_input)  # Кнопка очистки поля ввода
button_clear.place(x=550, y=300)
button_encrypt = tk.Button(window, text='Шифровать', width=12, height=2,
                           command=call_functions_encryption)  # Кнопка шифрования
button_encrypt.place(x=50, y=300)
button_decrypt = tk.Button(window, text='Дешифровать', width=12, height=2,
                           command=call_functions_decryption)  # Кнопка дешифрования
button_decrypt.place(x=657, y=300)

# Текстовые блоки
step_field = tk.Entry(window, width=4)
step_field.place(x=310, y=325)
input_field = tk.Text(window)
input_field.place(x=50, y=90, width=700, height=200)
output_field = tk.Text(window)
output_field.place(x=50, y=375, width=700, height=200)

# Лейблы
step_label = tk.Label(window, text='Укажите шаг шифрования')
step_label.place(x=150, y=325)
error_label = tk.Label(window, text='Введите число', fg="#ff0000")
header_label = tk.Label(window, text='The Roman cryptographer', font=("Arial", 32, "bold"), anchor="center")
header_label.place(x=120, y=25)

window.mainloop()
