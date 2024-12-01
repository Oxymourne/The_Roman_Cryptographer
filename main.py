import tkinter as tk

window = tk.Tk()
window.title('Римский шифратор')
window.geometry("1280x1024")
window.resizable(False, False)

# Кнопки
button_ru = tk.Button(window, text='RU')   # Кнопка Русского языка
button_ru.place(x=100, y=100)
button_eng = tk.Button(window, text='EN')   # Кнопка Английского языка
button_eng.place(x=200, y=100)
button_encrypt = tk.Button(window, text='Шифровать')   # Кнопка шифрования
button_encrypt.place(x=300, y=100)
button_decrypt = tk.Button(window, text='Дешифровать')   # Кнопка дешифрования
button_decrypt.place(x=400, y=100)



window.mainloop()