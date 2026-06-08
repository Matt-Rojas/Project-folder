
import tkinter as tk
from tkinter import font
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')
        
        # Input fields for numbers
        input_frame = tk.Frame(root, bg='#f0f0f0')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Number 1:", font=font.Font(size=10), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(input_frame, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Number 2:", font=font.Font(size=10), bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(input_frame, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons for operations
        button_frame = tk.Frame(root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        add_button = tk.Button(button_frame, text="Add", width=10, command=self.add)
        add_button.grid(row=0, column=0, padx=5)
        
        subtract_button = tk.Button(button_frame, text="Subtract", width=10, command=self.subtract)
        subtract_button.grid(row=0, column=1, padx=5)
        
        multiply_button = tk.Button(button_frame, text="Multiply", width=10, command=self.multiply)
        multiply_button.grid(row=1, column=0, padx=5)
        
        divide_button = tk.Button(button_frame, text="Divide", width=10, command=self.divide)
        divide_button.grid(row=1, column=1, padx=5)
        
        # Result display area
        self.result_label = tk.Label(root, text="Result: ", font=font.Font(size=12), bg='#f0f0f0')
        self.result_label.pack(pady=20)

    # Helper method to get numbers from input fields
    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return None, None

    # Methods for each operation   
    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")
    
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")
    
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")
    
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()