import secrets
import string
import tkinter as tk
from tkinter import messagebox


class PasswordGeneratorApp:
    BG_COLOR = "#4A71DD"
    BUTTON_COLOR = "#F5425A"

    MAIN_FONT = ("Vazir", 18, "bold")
    SECOND_FONT = ("Vazir", 14, "bold")

    VALID_CHARS = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    def __init__(self, root):
        self.root = root

        self.root.title("Password Generator")
        self.root.geometry("450x420")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG_COLOR)

        self.create_widgets()

    def create_widgets(self):
        self.counter_label = tk.Label(
            self.root, text="تعداد کاراکترها", font=self.MAIN_FONT, bg=self.BG_COLOR
        )
        self.counter_label.pack(pady=(25, 12))

        self.counter_entry = tk.Entry(
            self.root, font=self.SECOND_FONT, justify="center"
        )
        self.counter_entry.pack()
        self.counter_entry.insert(0, "16")

        self.generate_button = tk.Button(
            self.root,
            text="ساخت رمز عبور",
            bg=self.BUTTON_COLOR,
            fg="white",
            font=self.MAIN_FONT,
            command=self.generate_password,
        )
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(
            self.root, text="", bg=self.BG_COLOR, font=self.SECOND_FONT, wraplength=410
        )
        self.password_label.pack(pady=10, padx=15)

        self.status_label = tk.Label(
            self.root, text="", bg=self.BG_COLOR, fg="white", font=("Vazir", 11)
        )
        self.status_label.pack(pady=5)

        self.counter_entry.bind("<Return>", lambda event: self.generate_password())

    def generate_password(self):
        try:
            length = int(self.counter_entry.get().strip())

            if not 1 <= length <= 1000:
                raise ValueError

        except ValueError:
            messagebox.showerror("خطا", "تعداد کاراکترها باید عددی بین ۱ تا ۱۰۰۰ باشد.")
            return

        password = "".join(secrets.choice(self.VALID_CHARS) for _ in range(length))

        self.password_label.config(text=password)

        # Automatically copy the password to the clipboard
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()

            self.status_label.config(text="رمز عبور به‌صورت خودکار کپی شد!")

        except tk.TclError:
            self.status_label.config(text="رمز ساخته شد، اما کپی انجام نشد.")


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
