import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def clear_entries(weight_entry, height_entry):
    weight_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    weight_entry.focus()

def is_valid(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        if 0.5 <= height <= 3 and 20 <= weight <= 1000:
            return True
        else:
            messagebox.showinfo(title="Data Entry Error:", message="Enter reasonable height (m) and weight(Kg)")
            return False
    except ValueError:
        messagebox.showinfo(title="Data Entry Error:", message="Enter numeric values for height and weight")
        return False

def calc_bmi(weight_entry, height_entry, result_label):
    height = height_entry.get()
    weight = weight_entry.get()
    if is_valid(height, weight):
        height = float(height)
        weight = float(weight)
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        result = f"Your BMI is: {bmi}"
        result_label.config(text=result)
    else:
        weight_entry.delete(0, 'end')
        height_entry.delete(0, 'end')
        weight_entry.focus()

def create_gui():
    form = tk.Tk()
    form.title("Welcome to BMI calculator")
    form.geometry("700x220")
    style = ttk.Style()
    style.theme_use('clam')

    welcome_label = tk.Label(form, text=" Welcome to my BMI calculator", font=("Helvetica", 16))
    welcome_label.config(font=("Courier", 14))
    welcome_label.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    weight_label = tk.Label(form, text="Weight (Kg)", font=("Helvetica", 12))
    weight_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    height_label = tk.Label(form, text="Height (M)", font=("Helvetica", 12))
    height_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    weight_entry = tk.Entry(form, width="30")
    weight_entry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    height_entry = tk.Entry(form, width="30")
    height_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    result_label = tk.Label(form, text="")
    result_label.grid(row=4, column=1, columnspan=3, sticky="W", padx=10, pady=10)

    exit_button = tk.Button(form, text="Exit", width=12, command=quit)
    exit_button.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    clear_button = tk.Button(form, text="Clear", width=12, command=lambda: clear_entries(weight_entry, height_entry))
    clear_button.grid(row=3, column=1, padx=10, pady=10, sticky="W")

    calc_button = tk.Button(form, text="Calculate", width=12, command=lambda: calc_bmi(weight_entry, height_entry, result_label))
    calc_button.grid(row=3, column=2, padx=10, pady=10, sticky="W")

    weight_entry.focus()
    form.mainloop()

create_gui()
