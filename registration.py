import tkinter as tk
from tkinter import messagebox

def submit():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Username: {username}, Password: {password}")
    messagebox.showinfo("Реєстрація", "Дані відправлено!")

def cancel():
    root.destroy()

# Створення головного вікна
root = tk.Tk()
root.title("Форма реєстрації")
root.geometry("350x250")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Кадр для форми
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
frame.pack(pady=20)

# Мітки та поля введення
tk.Label(frame, text="Ім'я користувача:", bg="#ffffff", font=("Arial", 10)).pack(pady=5)
entry_username = tk.Entry(frame, font=("Arial", 10), width=25)
entry_username.pack(pady=5)

tk.Label(frame, text="Пароль:", bg="#ffffff", font=("Arial", 10)).pack(pady=5)
entry_password = tk.Entry(frame, show="*", font=("Arial", 10), width=25)
entry_password.pack(pady=5)

# Кнопки
btn_frame = tk.Frame(frame, bg="#ffffff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="OK", command=submit, font=("Arial", 10), bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Скасувати", command=cancel, font=("Arial", 10), bg="#f44336", fg="white", width=12).grid(row=0, column=1, padx=5)

# Запуск головного циклу
root.mainloop()
