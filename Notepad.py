from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext, ttk, font
import os

Notepad = Tk()
Notepad.geometry("600x480+350+40")
Notepad.title("Notepad")
photo = PhotoImage(file="Notepad.png")
Notepad.iconphoto(False, photo)


def font_change():
    fonts_win = Toplevel()
    fonts_win.title("Fonts Settings")
    fonts_win.resizable(False, False)

    def font_size_choose(e):
        value = font_size.get()
        my_font.config(size=value)

    def font_family_choose(e):
        value = font_family.get()
        my_font.config(family=value)

    def font_style_choose(e):
        value = font_style.get()

        if value == "Bold":
            my_font.config(weight="bold")
        if value == "Regular":
            my_font.config(weight="normal", slant="roman", underline=0, overstrike=0)
        if value == "Italic":
            my_font.config(slant="italic")
        if value == "Bold/Italic":
            my_font.config(weight="bold", slant="italic")
        if value == "Underline":
            my_font.config(underline=1)
        if value == "Strike":
            my_font.config(overstrike=1)

    font_size_label = ttk.Label(fonts_win, text="Font Size", font=("Helvetica", 15))
    font_size_label.grid(row=1, column=1, padx=5, pady=5)

    values = [[a] for a in range(2, 101, 2)]

    font_size = ttk.Combobox(fonts_win, values=values, width=30)
    font_size.bind("<<ComboboxSelected>>", font_size_choose)
    font_size.grid(row=1, column=2, padx=5, pady=5)

    font_family_label = ttk.Label(fonts_win, text="Font Family", font=("Helvetica", 15))
    font_family_label.grid(row=2, column=1, padx=5, pady=5)

    fonts = list(font.families())
    fonts.sort()

    font_family = ttk.Combobox(fonts_win, values=fonts, width=30)
    font_family.bind("<<ComboboxSelected>>", font_family_choose)
    font_family.grid(row=2, column=2, padx=5, pady=5)

    font_style_label = ttk.Label(fonts_win, text="Font Style", font=("Helvetica", 15))
    font_style_label.grid(row=3, column=1, padx=5, pady=5)

    font_styles = ["Regular", "Bold", "Italic", "Bold/Italic", "Underline", "Strike"]

    font_style = ttk.Combobox(fonts_win, values=font_styles, width=30)
    font_style.bind("<<ComboboxSelected>>", font_style_choose)
    font_style.grid(row=3, column=2, padx=5, pady=5)


def newFile():
    global file
    Notepad.title("Untitled - Notepad")
    file = None
    txt.delete(1.0, END)


def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        Notepad.title(os.path.basename(file) + " - Notepad")
        txt.delete(1.0, END)
        f = open(file, "r")
        txt.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(txt.get(1.0, END))
            f.close()

            Notepad.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # save a file
        f = open(file, "w")
        f.write(txt.get(1.0, END))
        f.close()


def cut():
    txt.event_generate("<<Cut>>")


def copy():
    txt.event_generate("<<Copy>>")


def paste():
    txt.event_generate("<<Paste>>")


def exit():
    Notepad.destroy()


def Light():
    txt.config(bg="light grey", fg="black")


def Dark():
    txt.config(bg="#505050", fg="#000000")


def about():
    messagebox.showinfo("About Notepad", "Notepad, made by zaid123khalid")


file = None

Menubar = Menu(Notepad)
Notepad.config(menu=Menubar)

filemenu = Menu(Menubar, tearoff=0)
editmenu = Menu(Menubar, tearoff=0)
thememenu = Menu(Menubar, tearoff=0)
Aboutmenu = Menu(Menubar, tearoff=0)

Menubar.add_cascade(label="File", menu=filemenu)
Menubar.add_cascade(label="Edit", menu=editmenu)
Menubar.add_cascade(label="Theme", menu=thememenu)
Menubar.add_cascade(label="About", menu=Aboutmenu)

my_font = font.Font(family="Helvetica", size="10", weight="normal", slant="roman", underline=0, overstrike=0)

txt = scrolledtext.ScrolledText(Notepad, font=my_font, bg="light grey", fg="black")
txt.pack(expand=True, fill=BOTH)

filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
editmenu.add_command(label="Font", command=font_change)

thememenu.add_command(label="Light", command=Light)
thememenu.add_command(label="Dark", command=Dark)

Aboutmenu.add_command(label="About Notepad", command=about)

Notepad.mainloop()
