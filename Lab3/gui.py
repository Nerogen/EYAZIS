import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext  # Добавлен модуль для многострочного текста
from my import main


class ReferencerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Automatic Referencer')
        self.geometry('1000x700')

        self.file_link = ''  # Добавлено свойство для хранения ссылки из файла

        self.upload_button = tk.Button(self, text="Upload Text Document", command=self.upload_document, width=50,
                                       height=2)
        self.upload_button.pack(pady=20)

        self.result_label = tk.Label(self, text="Result will be shown here...", wraplength=800)
        self.result_label.pack(pady=20, padx=20)

        self.link_label = tk.Label(self, text="", fg="blue", cursor="hand2", font=("Arial", 12, "underline"))
        self.link_label.pack(pady=10)
        self.link_label.bind("<Button-1>", self.open_link)

        self.save_button = tk.Button(self, text="Save Summary", command=self.save_summary, state="disabled", width=50,
                                     height=2)
        self.save_button.pack(pady=20)

        self.print_button = tk.Button(self, text="Print Summary", command=self.print_summary, state="disabled",
                                      width=50, height=2)
        self.print_button.pack(pady=20)

        self.help_button = tk.Button(self, text="Help", command=self.display_help, width=50, height=2)
        self.help_button.pack(pady=20)

    def upload_document(self):
        file_path = filedialog.askopenfilename(title="Select A Text File",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            # Извлечение первой строки из файла и установка ссылки
            with open(file_path, 'r') as file:
                self.file_link = file.readline().strip()
                self.link_label["text"] = self.file_link
            self.data = main(file_path.split("/")[-1])
            # Вызов вашей функции обработки текста здесь и передача 'file_path'
            self.summary = "This is the summary that your text processing function returns"
            self.result_label["text"] = self.summary
            self.save_button["state"] = "normal"
            self.print_button["state"] = "normal"
        else:
            messagebox.showwarning("Warning", "Please select a text file.")

    def save_summary(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(save_path, 'w') as f:
            f.write("\n".join(self.data))
        messagebox.showinfo("Saved", f"Summary saved to {save_path}")

    def print_summary(self):
        print_window = tk.Toplevel(self)
        print_window.title("Printed Summary")

        # Добавлена многострочная область текста
        text_area = scrolledtext.ScrolledText(print_window, wrap=tk.WORD, width=80, height=20)
        text_area.pack(padx=10, pady=10)

        # Установка текста в многострочную область
        text_area.insert(tk.INSERT, "\n".join(self.data))

    def display_help(self):
        messagebox.showinfo("Help",
                            "1. Click 'Upload Text Document' to upload a document.\n2. View the auto-generated summary.\n3. Click 'Save Summary' to save the generated summary.\n4. Click 'Print Summary' to print the summary.")

    def open_link(self, event):
        # Метод для открытия ссылки при клике на неё
        import webbrowser
        webbrowser.open(self.file_link)


if __name__ == "__main__":
    app = ReferencerApp()
    app.mainloop()
