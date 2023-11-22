import os
import tkinter as tk
from tkinter import filedialog, font
from jsonHandler import JsonHandler 



jHandler = None

window = tk.Tk()
# window.columnconfigure([0, 1], minsize=50)
window.rowconfigure([0,1,2], minsize=10)
window.config(bg="black")


def load():
    current_file = filedialog.askdirectory(title="Choose a Directory", initialdir="./")
    if os.path.exists(current_file + "/config.json") == True:
        folder_name = os.path.basename(current_file)
        load_text.set(folder_name)
        jHandler = JsonHandler(folder_name)
        print(jHandler.getData("playset"))
    else:
        print("Not there")




label_width = 50
label_height = 20
init_font_size = 14

label_font = font.Font(size=init_font_size)

label = tk.Label(window, text="Test",width=label_width,height=label_height,bg="blue", font=label_font, borderwidth=2)
label.grid(row=0, column=0, rowspan=2, sticky="nsew")

load_text = tk.StringVar()
load_button = tk.Button(textvariable=load_text, width=20, font=label_font,
                        height=1, bg='#21781A', fg='#781A52', command=load).grid(row=0, column=1)
load_text.set("Load Playset")

but2 = tk.Button(text="Save", width=20, height=5, bg="green").grid(row=1, column=1)










window.mainloop()