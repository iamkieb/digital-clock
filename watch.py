from time import strftime
from tkinter import Label, Tk

# Window Config for clock
window = Tk()
window.title("")
window.geometry("190x80")
window.configure(bg = "#5F6672")
window.resizable(False, False)

# label config
clock_label = Label(window, bg="#5F6672", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.place(x = 30, y = 20)

def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, updating_label)

updating_label()
window.mainloop()