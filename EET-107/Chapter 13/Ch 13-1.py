# Sean Kelley
# ch13-1
# 26 July 2021

from tkinter import *

root = Tk()
root.title('Feet and Inches Converter')

# label at top of program
label = Label(root, text='Feet and Inches Converter')
label.grid(row=1, column=1, columnspan=4)

# label for feet entry
feet_label = Label(root, text='Feet:')
feet_label.grid(row=2, column=1)

# label fot inches entry
inches_label = Label(root, text='Inches:')
inches_label.grid(row=2, column=3)


feets = Entry(root, width=5, borderwidth=5)
feets.grid(row=2, column=2)

inches = Entry(root, width=5, borderwidth=5)
inches.grid(row=2, column=4)


def converter():
    feet = int(feets.get())
    inch = int(inches.get())
    final = (feet * 12) + inch
    label['text'] = f'Inches: {final}'


label = Label(root, text='Inches: 0')
label.grid(row=3, column=2, columnspan=2)

convert = Button(root, text='Convert', command=lambda:converter())
convert.grid(row=4, column=2)

quit = Button(root, text='Exit', command=lambda:root.quit())
quit.grid(row=4, column=3)
root.mainloop()
