from tkinter import *
from tkinter import filedialog, messagebox
import backend
import webbrowser
#194703-21871a60-f09c-4678-97b9-2db2b7322acf
# Required in order to add data files to Windows executable
import sys, os
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)


def btn_clicked():
    token = token_entry.get()
    URL = URL_entry.get()

    if not token:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter Token")

    elif not URL:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter URL")

    elif not output_path:
        messagebox.showerror(title="invalid path",
                             message="Enter a valid output path")

    else:
        backend.generate_code(token,URL, output_path)

def select_path(event):
    global output_path

    # window.withdraw()
    output_path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, output_path)
    # window.deiconify()


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)

    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)

    return label




window = Tk()
window.title("Proxlight Designer")
window.iconbitmap("Icon.ico")
window.geometry("862x519")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    374.0, 295.5,
    image=background_img)

canvas.create_text(
    220.0, 78.5,
    text = "Proxlight",
    fill = "#ffffff",
    font = ("Bite Chocolate", int(30.0)))

canvas.create_text(
    607.0, 78.5,
    text = "Enter Details Here",
    fill = "#515486",
    font = ("Roboto-Bold", int(15.0)))

canvas.create_text(
    210.0, 150,
    text = "Designer",
    fill = "#ffffff",
    font = ("Roboto-Italic", int(24.0)))

canvas.create_text(
    210.0, 280.0,
    text = "Create Some Thing Beautiful !",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(13.0)))



path_entry_img = PhotoImage(file = f"img_textBox0.png")
path_entry_bg = canvas.create_image(
    638.0, 345.0,
    image = path_entry_img)

path_entry =  Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)
path_entry.place(
        x = 538.0, y = 326,
        width = 200.0,
        height = 36)


path_entry.bind("<1>", select_path)

URL_entry_img = PhotoImage(file = f"img_textBox1.png")
URL_entry_bg = canvas.create_image(
    638.0, 248.0,
    image = URL_entry_img)

URL_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

URL_entry.place(
    x = 538.0, y = 229,
    width = 200.0,
    height = 36)

token_entry_img = PhotoImage(file = f"img_textBox2.png")
token_entry_bg = canvas.create_image(
    638.0, 153.0,
    image = path_entry_img)

token_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

token_entry.place(
    x = 538.0, y = 134,
    width = 200.0,
    height = 36)
token_entry.focus()

canvas.create_text(
    560.5, 117.0,
    text = "Token ID",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

canvas.create_text(
    560.5, 210.0,
    text = "File URL",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

canvas.create_text(
    560.5, 310.0,
    text = "Export To",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")

b0.place(
    x = 572, y = 401,
    width = 152,
    height = 51)

window.resizable(False, False)
window.mainloop()
