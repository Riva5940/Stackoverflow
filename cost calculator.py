from tkinter import *
import random  # 處理隨機生成


win = Tk()

win.title("")
win.geometry("+800+400")

Length = Label(text="Length ")
Length.grid(row=0, column=0)

Diameter = Label(text="Diameter ")
Diameter.grid(row=1, column=0)

Length_entry: Entry = Entry(bg="#323232")
Length_entry.grid(row=0, column=1)

Diameter_entry = Entry(bg="#323232")
Diameter_entry.grid(row=1, column=1)

cost_show = Label(text="cost")
cost_show.grid(row=4, column=0)

cost_show = Label(text="")
cost_show.grid(row=4, column=1)

cost_L = int


def calculate():
    Length_value = int(float(Length_entry.get())

    if( Length_value <=250):
     cost_L=1
    elif( 250< Length_value <=300):
     cost_L=2
    elif( 300< Length_value <=350):
     cost_L=3
    elif( 350< Length_value <=450):
     cost_L=4
    elif( 450< Length_value):
     cost_L=5
print(str(Length_value))
y = str(cost_L)
cost_show.config(text=y)


Calculate_btn=Button(text="Calculate",command=calculate())
Calculate_btn.grid(row=3, column=1)



win.mainloop()
