import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Set window background color
        master.configure(bg='#1E1E1E')
        
        self.result = tk.StringVar()
        self.result.set("0")
        
        # Create entry with larger font and background color to match the picture
        self.entry = tk.Entry(master, textvariable=self.result, justify='right', font=("Arial", 24), bg='#333333', fg='#FFFFFF', bd=0, insertbackground='#FFFFFF')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")
        
        buttons = [
            '%', 'CE', 'C', '⌫',
            '1/x', 'x²', '√x', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=3, height=2, font=("Arial", 18), fg='#FFFFFF', bg='#2D2D2D', bd=0, activebackground='#555555', activeforeground='#FFFFFF', command=lambda b=button: self.click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def click(self, button):
        current = self.result.get()
        if button == 'C':
            self.result.set("0")
        elif button == 'CE':
            self.result.set("0")
        elif button == '⌫':
            self.result.set(current[:-1])
        elif button == '=':
            try:
                self.result.set(eval(current))
            except Exception as e:
                self.result.set("Error")
        elif button == '1/x':
            try:
                self.result.set(1 / float(current))
            except Exception as e:
                self.result.set("Error")
        elif button == 'x²':
            try:
                self.result.set(float(current) ** 2)
            except Exception as e:
                self.result.set("Error")
        elif button == '√x':
            try:
                self.result.set(float(current) ** 0.5)
            except Exception as e:
                self.result.set("Error")
        elif button == '+/-':
            if current.startswith('-'):
                self.result.set(current[1:])
            else:
                self.result.set('-' + current)
        else:
            if current == "0":
                self.result.set(button)
            else:
                self.result.set(current + button)

if __name__ == "__main__":
    root = tk.Tk()
    # Set the size of the window
    root.geometry("400x600")
    # Configure rows and columns to expand with the window
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    calculator = Calculator(root)
    root.mainloop()
