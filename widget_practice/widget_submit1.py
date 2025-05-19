from tkinter import * 
window = Tk()

photo = PhotoImage(file="C:\\Users\\LG\\Downloads\\dog.gif") #\\로 \표시
label1 = Label(window, image=photo)
label2 = Label(window, image=photo)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()