import tkinter as tk
from tkinter import messagebox
import math

# Biến bộ nhớ tạm thời
memory = 0

# Hàm xử lý các phím bấm
def press_key(key):
    global memory
    current_text = entry.get()
    
    try:
        if key == "=":
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "C":
            entry.delete(0, tk.END)
        elif key == "DEL":
            entry.delete(len(current_text) - 1, tk.END)
        elif key == "√":
            result = math.sqrt(float(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "^2":
            result = float(current_text) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "%":
            result = float(current_text) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "+/-":
            if current_text:
                if current_text[0] == "-":
                    entry.delete(0)
                else:
                    entry.insert(0, "-")
        elif key == "MC":
            memory = 0
        elif key == "MR":
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(memory))
        elif key == "M+":
            memory += float(current_text)
        elif key == "M-":
            memory -= float(current_text)
        else:
            entry.insert(tk.END, key)
    except Exception:
        messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")

# Tạo cửa sổ chính của ứng dụng
app = tk.Tk()
app.title("Calculator")
app.geometry("360x550")
app.configure(bg="#222831")

# Khung nhập liệu
entry = tk.Entry(app, width=18, font=('Arial', 24), borderwidth=0, relief="solid", justify="right", bg="#222831", fg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=4, pady=(20, 10), padx=10, sticky="nsew")

# Các nút bấm
buttons = [
    ('MC', '#D9534F'), ('MR', '#D9534F'), ('M+', '#FFC107'), ('M-', '#FFC107'),
    ('C', '#D9534F'), ('DEL', '#D9534F'), ('%', '#FFC107'), ('√', '#FFC107'),
    ('7', '#393E46'), ('8', '#393E46'), ('9', '#393E46'), ('/', '#FFC107'),
    ('4', '#393E46'), ('5', '#393E46'), ('6', '#393E46'), ('*', '#FFC107'),
    ('1', '#393E46'), ('2', '#393E46'), ('3', '#393E46'), ('-', '#FFC107'),
    ('+/-', '#393E46'), ('0', '#393E46'), ('.', '#393E46'), ('+', '#FFC107'),
    ('^2', '#1E90FF'), ('=', '#1E90FF')
]

# Tạo và sắp xếp các nút trong lưới
row = 1
col = 0
for (text, color) in buttons:
    action = lambda x=text: press_key(x)
    tk.Button(app, text=text, width=6, height=2, command=action, bg=color, fg="white", font=('Arial', 16), borderwidth=0).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Thiết lập kích thước đồng đều cho tất cả các hàng và cột
for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for j in range(4):
    app.grid_columnconfigure(j, weight=1)

app.mainloop()
