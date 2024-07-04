import tkinter as tk


m = tk.Tk()
m.title("new")
tk.Label(m, text="test").grid()
tk.Entry(m).grid(row=0, column=1)
tk.Entry(m).grid(row=1, column=1)
tk.Button(m, text='stop', width=50, command=m.destroy).grid()

m.mainloop()