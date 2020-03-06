import math
import numpy as np
import cv2
import tkinter as tkinter
import PIL.ImageTk, PIL.Image

def show_image_2(canvas, filename):
    canvas.create_image(0, 0, image=PIL.ImageTk.PhotoImage(file=filename), anchor=tkinter.NW)

def show_image (canvas, file_name):
    image = cv2.resize(cv2.imread(file_name), (800, 800))
    image=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
    canvas.config(image=image)
    canvas.image=image
    # canvas.create_image(0, 0, , anchor=tkinter.NW)
    # img = False
    
    # image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
    # canvas.create_image(0, 0, image=image, anchor=tkinter.NW) 

def main():
    window = tkinter.Tk()
    window.title('')
    menu = tkinter.Menu(window)
    file_menu = tkinter.Menu(menu, tearoff=0)
    # canvas = tkinter.Canvas(window, width = 800, height = 800)
    # canvas.pack()
    image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(np.zeros((800, 800, 3), dtype=np.uint8)))
    canvas = tkinter.Label(window, image=image)
    canvas.image = image
    canvas.pack(fill="both", expand="yes")
    file_menu.add_command(label = 'Room 1', command= lambda: show_image(canvas, 'room1.jpg'))#cv2.resize(cv2.imread('room1.jpg'), (800, 800))))
    file_menu.add_command(label = 'Room 2', command= lambda: show_image(canvas, 'room2.jpeg'))
    file_menu.add_command(label = 'Room 3', command= lambda: show_image(canvas, 'room3.jpg'))
    file_menu.add_command(label = 'Room 4', command= lambda: show_image(canvas, 'room4.jpg'))
    menu.add_cascade(label='choose a new image', menu=file_menu)
    menu.add_command(label='Exit', command=window.destroy)
    window.config(menu=menu)

    # load_pic_button = tkinter.Button(window, text="Load image", width = 15)
    # load_pic_button.pack()
    # exit_button = tkinter.Button(window, text="Exit", width = 15, command=window.destroy)
    # exit_button.pack()
    window.mainloop()
    

if __name__ == "__main__":
    # execute only if run as a script
    main()