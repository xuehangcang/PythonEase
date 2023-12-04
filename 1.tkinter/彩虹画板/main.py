import tkinter as tk
from tkinter import colorchooser, messagebox
from PIL import Image

root = tk.Tk()
root.title("彩虹画板：Tkinter绘图应用")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

current_color = 'black'


def paint(event):
    """画图"""
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)


canvas.bind('<B1-Motion>', paint)


def change_color():
    """改变画笔颜色"""
    global current_color
    color = colorchooser.askcolor()
    if color[1]:
        current_color = color[1]


color_button = tk.Button(root, text="选择颜色", command=change_color)
color_button.pack()


def save_drawing():
    """保存画作"""
    canvas.postscript(file="canvas.eps", colormode='color')
    try:
        img = Image.open('canvas.eps')
        img.save('output.png', 'png')
        messagebox.showinfo("保存成功", "您的画作已保存为drawing.png")
    except Exception as e:
        messagebox.showerror("保存失败", str(e))


def clear_canvas():
    """清除画布"""
    canvas.delete("all")


save_button = tk.Button(root, text="保存作品", command=save_drawing)
clear_button = tk.Button(root, text="清除画板", command=clear_canvas)

save_button.pack()
clear_button.pack()

root.mainloop()
