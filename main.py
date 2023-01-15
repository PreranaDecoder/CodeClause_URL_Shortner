import pyshorteners
import pyperclip
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("URL SHORTENER")
# root.configure(bg='#51A') #49A
url = StringVar()
url_address = StringVar()
img=Image.open("bg.png")
bck_end=ImageTk.PhotoImage(img)
root.geometry("1000x550")
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)
lbl2=Label(root,text="CodeClause Project", font='Helvetica 16 bold',foreground="dark blue")
lbl2.pack(pady=50)


def urlshortener():
    urladdress = url.get()
    url_add = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_add)

def copyurl():
    url_add = url_address.get()
    pyperclip.copy(url_add)

Label(root, text="URL SHORTENER", font="calibri 20 bold").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root, text="Generate Short Url", command=urlshortener).pack(pady=7)
Entry(root, textvariable = url_address,foreground="blue").pack(pady=5)
Button(root, text="Copy",command=copyurl).pack()

root.mainloop()