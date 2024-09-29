import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg='black')

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 48), justify='right', bg='black', fg='white', bd=10, insertwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '²', '0', '√', '/',
            '=', 'CLEAR'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button in ['+', '-', '*', '/', '²', '√']:
                color = 'green'
            else:
                color = 'white'

            if button == '=':
                tk.Button(root, text=button, font=("Arial", 36), command=self.on_equal_click, bg='black', fg=color, bd=5).grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
                col_val += 2
            elif button == 'CLEAR':
                tk.Button(root, text=button, font=("Arial", 36), command=lambda: self.result_var.set(""), bg='black', fg=color, bd=5).grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
                col_val += 2
            else:
                tk.Button(root, text=button, font=("Arial", 36), command=lambda b=button: self.on_button_click(b), bg='black', fg=color, bd=5).grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i + 1, weight=1)

        self.entry.grid_configure(sticky="ew")

    def on_button_click(self, char):
        current_text = self.result_var.get()
        new_text = current_text + char
        self.result_var.set(new_text)

    def on_equal_click(self):
        try:
            expression = self.result_var.get()
            if '²' in expression:
                base = float(expression.replace('²', ''))
                result = base ** 2
                self.result_var.set(result)
            elif '√' in expression:
                radicand = float(expression.replace('√', ''))
                result = math.sqrt(radicand)
                self.result_var.set(result)
            else:
                result = eval(expression)
                self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")
        finally:
            self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")
    app = Calculator(root)
    root.mainloop()
