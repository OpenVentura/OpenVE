# OpenTE -v1.0
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import sys

window = tk.Tk()
window.title("OpenTE")
window.geometry("600x500")
window.attributes('-fullscreen', True)
bar = tk.Menu(window)

def_font = font.Font(family="Consolas", size=12)
def_barfont = ("Helvetica Neue", 11, "bold italic")

def_foreground = "#00ff00"
def_background = "#000000"
def_ActiveForeground = "#ffffff"
def_ActiveBackground = "#555555"
def_barbg = "#434343"
def_barfg = "#ffffff"

def new_file():
    te.delete(1.0, tk.END)

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text = te.get("1.0", "end-1c")
            file.write(text)
            
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            te.delete("1.0", "end")
            te.insert("1.0", text)

def wf_quit():
    if messagebox.askokcancel("Confirmation", "Are you sure you want to exit OpenTE? (Will NOT save your file)"):
        window.destroy()
        sys.exit()

def wf_iconify():
    window.iconify()

te = tk.Text(window, wrap="word", font=def_font, foreground=def_foreground, background=def_background, insertbackground=def_foreground)
te.pack(fill="both", expand=True)
te.insert(tk.END, "Welcome to OpenTE v1.0\n\n")

file_bar = tk.Menu(bar, tearoff=0, font=def_barfont, background=def_barbg, foreground=def_barfg, activeforeground=def_ActiveForeground, activebackground=def_ActiveBackground)
file_bar.add_command(label="New", command=new_file)
file_bar.add_command(label="Open", command=open_file)
file_bar.add_command(label="Save As", command=save_file_as)
te_bar = tk.Menu(bar, tearoff=0, font=def_barfont, background=def_barbg, foreground=def_barfg, activeforeground=def_ActiveForeground, activebackground=def_ActiveBackground)
te_bar.add_command(label="Send to Taskbar", command=wf_iconify)
te_bar.add_command(label="Save and Exit", command=wf_quit)

bar.add_cascade(label="OpenTE", menu=te_bar)
bar.add_cascade(label="File", menu=file_bar)

window.config(menu=bar)
window.mainloop()
