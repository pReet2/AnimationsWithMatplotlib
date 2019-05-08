from tkinter import *
window = Tk()
window.title('Grand Canyon')

canvas = Canvas(window, width = 700, height = 500)
canvas.pack()
my_image=PhotoImage(file='C:\\Users\\Preeti Gupta\\Desktop\\pyPrograms\\myImage.gif')
canvas.create_image(0,0,anchor = NW,image= my_image)
