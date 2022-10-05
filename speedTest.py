from email import message
import math
from struct import pack
import tkinter as tk
from tkinter import messagebox
from turtle import speed
from PIL import Image, ImageTk
import pyspeedtest

root = tk.Tk()
root.geometry("320x450")
root.resizable(0,0)
root.title("Internet Download Speed")
root.iconbitmap("smeter.ico")

#Creating Functions

st=pyspeedtest.SpeedTest("www.google.com")
def SpeedTest():
    speed = str(math.floor(st.download()/1000 ))+ "Kb/s"
    messagebox.showinfo("The speed is ",speed)

#Logo
logo = Image.open("robot.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()

new_label = tk.Label(root, text = "Test Download Speed", font=("Areal",18,"bold"), fg="green")
new_label.pack(padx=20 ,pady=20)

#creating Buttons
button1 = tk.Button(root, text="Check", command=SpeedTest, font=("Areal",18,"bold"))
button1.pack(padx=20, pady=10)

button2 = tk.Button(root, text="Exit", command=root.destroy, font=("Areal",18,"bold"))
button2.pack(padx=10, pady=10)

#createing Label
new_label2 = tk.Label(root, text="Thanks!",  font=("Areal",25,"bold"),bg="black",fg="white")
new_label2.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()