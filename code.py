import tkinter as tk
import math

# Function to handle button clicks
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to calculate result
def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("x²", "**2")
        expr = expr.replace("%", "/100")
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Square root function
def square_root():
    try:
        current = entry.get()
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Square function
def square():
    try:
        current = entry.get()
        result = float(current) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear
def clear():
    entry.delete(0, tk.END)

# Keyboard input handler
def key_press(event):
    key = event.char
    if key in "0123456789.+-*/()":
        click(key)
    elif key == "\r":  # Enter key
        calculate()
    elif key == "\x08":  # Backspace
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])

# Main window
window = tk.Tk()
window.title("Calculator")
window.geometry("346x420")
window.resizable(False, False)
window.config(bg="#2c3e50")

# Bind keyboard
window.bind("<Key>", key_press)

# Display Entry
entry = tk.Entry(window, font=("Arial", 22), justify="right", bd=0,
                  bg="#1c2833", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we", ipady=10)
entry.focus_set()

# Button layout
buttons = [
    ["AC", "√", "x²", "%"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Color scheme
colors = {
    "num": "#6eb3f9",
    "num_fg": "white",
    "op": "#e67e22",
    "op_fg": "white",
    "eq": "#27ae60",
    "clr": "#e74c3c",
    "func": "#f2d55f"
}

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(window, text=text, width=6, height=2,
                          font=("Arial", 14, "bold"), bg=colors["eq"], fg="white",
                          activebackground="#229954", bd=0,
                          command=calculate)
        elif text == "AC":
            btn = tk.Button(window, text=text, width=6, height=2,
                          font=("Arial", 14, "bold"), bg=colors["clr"], fg="white",
                          activebackground="#c0392b", bd=0,
                          command=clear)
        elif text == "√":
            btn = tk.Button(window, text=text, width=4, height=1,
                          font=("Arial", 22, "bold"), bg=colors["func"], fg="white",
                          activebackground="#732d91", bd=0,
                          command=square_root)
        elif text == "x²":
            btn = tk.Button(window, text=text, width=6, height=2,
                          font=("Arial", 14, "bold"), bg=colors["func"], fg="white",
                          activebackground="#732d91", bd=0,
                          command=square)
        elif text in ["/", "*", "-", "+", "%"]:
            btn = tk.Button(window, text=text, width=4, height=1,
                          font=("Arial", 22, "bold"), bg=colors["op"], fg="white",
                          activebackground="#d35400", bd=0,
                          command=lambda t=text: click(t))
        else:
            btn = tk.Button(window, text=text, width=6, height=2,
                          font=("Arial", 14, "bold"), bg=colors["num"], fg="white",
                          activebackground="#2c3e50", bd=0,
                          command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j, padx=4, pady=4)

window.mainloop()