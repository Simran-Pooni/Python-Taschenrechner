import tkinter as tk

calculation = ""

def add_to_calculation(zahl):
    global calculation
    calculation += str(zahl)
    textfield_result.delete(1.0, "end")
    textfield_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textfield_result.delete(1.0,"end")
        textfield_result.insert(1.0, result)
    except:
        clear_field()
        textfield_result.insert(1.0, "Error")

def clear_field():
    calculation = ""
    textfield_result.delete(1.0, "end")


# mw - "main window"
mw = tk.Tk()
mw.geometry("300x425")
mw.title("Taschenrechner")
mw.configure(bg="#FFB6C1")

# Hintergrundbild
hintergrund = tk.PhotoImage(file="schleife.png")
hintergrund_label = tk.Label(mw, image=hintergrund)
hintergrund_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ergebnistextfeld
textfield_result = tk.Text(mw, height=2, width=16, font=("Century", 24), bg="#FFC0CB", fg="black")
textfield_result.grid(columnspan=5, pady=10)

# Numberpad:
btn_1 = tk.Button(mw, text="1", command=lambda: add_to_calculation(1), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_1.grid(row=2, column=1, pady=10)

btn_2 = tk.Button(mw, text="2", command=lambda: add_to_calculation(2), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_2.grid(row=2, column=2, pady=10)

btn_3 = tk.Button(mw, text="3", command=lambda: add_to_calculation(3), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_3.grid(row=2, column=3, pady=10)

# row 3
btn_4 = tk.Button(mw, text="4", command=lambda: add_to_calculation(4), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_4.grid(row=3, column=1, pady=10)

btn_5 = tk.Button(mw, text="5", command=lambda: add_to_calculation(5), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_5.grid(row=3, column=2, pady=10)

btn_6 = tk.Button(mw, text="6", command=lambda: add_to_calculation(6), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_6.grid(row=3, column=3, pady=10)

# row 4
btn_7 = tk.Button(mw, text="7", command=lambda: add_to_calculation(7), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_7.grid(row=4, column=1, pady=10)

btn_8 = tk.Button(mw, text="8", command=lambda: add_to_calculation(8), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_8.grid(row=4, column=2, pady=10)

btn_9 = tk.Button(mw, text="9", command=lambda: add_to_calculation(9), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_9.grid(row=4, column=3, pady=10)

# row 5
btn_0 = tk.Button(mw, text="0", command=lambda: add_to_calculation(0), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_0.grid(row=5, column=2, pady=10)

# Operatoren:
btn_plus = tk.Button(mw, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_plus.grid(row=2, column=4, pady=10)

btn_min = tk.Button(mw, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_min.grid(row=3, column=4, pady=10)

btn_mul = tk.Button(mw, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_mul.grid(row=4, column=4, pady=10)

btn_div = tk.Button(mw, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_div.grid(row=5, column=4, pady=10)

btn_open = tk.Button(mw, text="(", command=lambda: add_to_calculation("("), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_open.grid(row=5, column=1, pady=10)

btn_close = tk.Button(mw, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Century", 12), bg="#FF69B4", fg="white")
btn_close.grid(row=5, column=3, pady=10)

btn_eq = tk.Button(mw, text="=", command=evaluate_calculation, width=11, font=("Century", 12), bg="#FF69B4", fg="white")
btn_eq.grid(row=6, column=1, columnspan=2, pady=10)

btn_clear = tk.Button(mw, text="C", command=clear_field, width=11, font=("Century", 12), bg="#FF69B4", fg="white")
btn_clear.grid(row=6, column=3, columnspan=2, pady=10)

mw.mainloop()
