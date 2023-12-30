import tkinter as tk

root = tk.Tk()

root.title('visual')
root.geometry('400x400')

text = tk.Label(root, text="hello", height=40, width=100, bg='red', font=('Arial', 20))
text.pack()


root.mainloop()