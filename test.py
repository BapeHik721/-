import tkinter as tk

class ImportantApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Очень важное приложение")
        self.root.configure(bg="white")

        # Настройка кнопки
        self.btn = tk.Button(
            self.root,
            text="НАЖМИ МЕНЯ",
            bg="#c80000",
            fg="white",
            font=("Arial", 24),
            activebackground="#ff0000",
            activeforeground="white",
            relief="flat",
            command=self.on_click
        )
        
        # Размещаем кнопку
        self.btn.place(x=100, y=110, width=200, height=80)

        # Подвязка ховера, потому что Tkinter кнопка 
        # сама по себе не особо любит меняться
        self.btn.bind("<Enter>", lambda e: self.btn.config(bg="#ff0000"))
        self.btn.bind("<Leave>", lambda e: self.btn.config(bg="#c80000"))

    def on_click(self):
        # Удаляем кнопку, когда пользователь наконец-то совершил действие
        self.btn.destroy()

        # Выводим сообщение
        msg = tk.Label(
            self.root, 
            text="я обкакался", 
            font=("Arial", 36, "bold"), 
            bg="white", 
            fg="black"
        )
        msg.pack(expand=True)

        # Таймер на 10 секунд и закрытие
        self.root.after(10000, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImportantApp(root)
    root.main
  loop()
