import tkinter as tk
import math
from datetime import datetime

root = tk.Tk()
root.title("Сағат")
root.geometry("400x400")

c = tk.Canvas(root, width=400, height=400, bg='white')
c.pack()

cx, cy, r = 200, 200, 150

def draw_static_elements():
    # Шеңбер
    c.create_oval(cx - r, cy - r, cx + r, cy + r, width=4, outline='black')
    
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        # Сандар
        x_num = cx + (r - 30) * math.cos(angle)
        y_num = cy + (r - 30) * math.sin(angle)
        c.create_text(x_num, y_num, text=str(i), font=('Arial', 20, 'bold'), fill='black')
        
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        x1 = cx + (r - 10) * math.cos(angle)
        y1 = cy + (r - 10) * math.sin(angle)
        x2 = cx + r * math.cos(angle)
        y2 = cy + r * math.sin(angle)
        c.create_line(x1, y1, x2, y2, width=1)

draw_static_elements()

hands = []

def update_clock():
    global hands
    for h in hands:
        c.delete(h)
    hands = []
    
    now = datetime.now()
    s = now.second
    m = now.minute + s / 60
    h = (now.hour % 12) + m / 60
    
    
    hands.append(c.create_line(cx, cy, cx + 60*math.cos(math.radians(h*30-90)), cy + 60*math.sin(math.radians(h*30-90)), width=6, fill='black')) 
    hands.append(c.create_line(cx, cy, cx + 100*math.cos(math.radians(m*6-90)), cy + 100*math.sin(math.radians(m*6-90)), width=4, fill='black'))
    hands.append(c.create_line(cx, cy, cx + 120*math.cos(math.radians(s*6-90)), cy + 120*math.sin(math.radians(s*6-90)), width=2, fill='red'))
    
    c.create_oval(cx-5, cy-5, cx+5, cy+5, fill='black')
    
    root.after(1000, update_clock)

update_clock()
root.mainloop()