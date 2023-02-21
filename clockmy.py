import time
from tkinter import*

root=Tk()
root.configure(background="black")

def start():
    text =time.strftime("%H : %M : %S %p\n%D")
    Label.config(text=text)
    Label.after(200,start)
Label = Label(root,font=("Algerian",100),fg="white",bg="black")
Label.grid(row=1, column=1)
print("Done")
start()
root.mainloop()   