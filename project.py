import math
import numpy as np
import cv2
import tkinter.filedialog
import tkinter as tkinter
import PIL.ImageTk, PIL.Image

def show_image (canvas, file_name):
    image = cv2.imread(file_name)
    a, b, _ = image.shape
    if(a > b):
        c = 800*b//a
        image = cv2.resize(image, (c, 800))
        canvas.mask_list = get_masks(image)
        canvas.select_mask = np.zeros((800,c), dtype=np.uint8)
    elif (a < b):
        c = 800*a//b
        image = cv2.resize(image, (800,c))
        canvas.mask_list = get_masks(image)
        canvas.select_mask = np.zeros((c,800), dtype=np.uint8)
    else:
        image = cv2.resize(image, (800, 800))
        canvas.mask_list = get_masks(image)
        canvas.select_mask = np.zeros((800,800), dtype=np.uint8)
    image=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
    canvas.config(image=image)
    canvas.image=image
    canvas.origin_image = image
    canvas.display = image
    canvas.has_image = True

def get_file(canvas, file_menu):
    canvas.file_name = tkinter.filedialog.askopenfilename(title = 'select image', filetypes= (('jpg files', '*.jpg'),('png files', '*.png'),('jpeg files', '*.jpeg')))
    file_menu.add_command(label = 'view custom picture', command= lambda: show_image(canvas, canvas.file_name))

def clear_image(canvas):
    image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(np.zeros((800, 800, 3), dtype=np.uint8)))
    canvas.config(image=image)
    canvas.image=image
    canvas.origin_image = image
    canvas.display = image
    canvas.has_image = False

def get_masks(image):
    pass

def select(canvas, menu):
    pass

def deselect(canvas, menu):
    pass

# def reset_image(canvas, menu):
    # canvas.image = canvas.origin_image
#     menu['Reset image'].entryconfig()

def main():
    window = tkinter.Tk()
    window.title('')
    menu = tkinter.Menu(window)
    file_menu = tkinter.Menu(menu, tearoff=0)
    image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(np.zeros((800, 800, 3), dtype=np.uint8)))
    canvas = tkinter.Label(window, image=image)
    canvas.image = image
    canvas.display = image
    canvas.origin_image = image
    canvas.mask_list = []
    canvas.select_mask = image
    canvas.has_image = False
    canvas.bind('<Button-1>', select(canvas, menu))
    canvas.bind('<Button-3', deselect(canvas, menu))
    canvas.pack(fill="both", expand="yes")
    file_menu.add_command(label = 'Clear image', command = lambda: clear_image(canvas))
    file_menu.add_command(label = 'Room 1', command= lambda: show_image(canvas, 'room1.jpg'))#cv2.resize(cv2.imread('room1.jpg'), (800, 800))))
    file_menu.add_command(label = 'Room 2', command= lambda: show_image(canvas, 'room2.jpeg'))
    file_menu.add_command(label = 'Room 3', command= lambda: show_image(canvas, 'room3.jpg'))
    file_menu.add_command(label = 'Room 4', command= lambda: show_image(canvas, 'room4.jpg'))
    file_menu.add_command(label = 'choose new file', command= lambda: get_file(canvas, file_menu))
    menu.add_cascade(label='choose a new image', menu=file_menu)
    menu.add_command(label='Exit', command=window.destroy)
    window.config(menu=menu)
    window.mainloop()
    

if __name__ == "__main__":
    # execute only if run as a script
    main()