import cv2 
import numpy as np
import tkinter as tk
from tkinter import filedialog









#PENCIL SKETCH

def img2sketch_main(filepath):
        #reading image:
        input_image = cv2.imread(str(filepath))
        #for gray scale:
        f_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('image',f_image)
        #inverse image
        imgnot=cv2.bitwise_not(f_image)
        #cv2.imshow('image',imgnot)
        # Getting the kernel to be used in Top-Hat
        kernel = np.ones((8,8),np.uint8)
        # Applying the Top-Hat operation
        tophat_img = cv2.morphologyEx(imgnot, cv2.MORPH_TOPHAT,kernel)
        img_not = cv2.bitwise_not(tophat_img)
        cv2.imshow('img_not',img_not)

        image = tk.PhotoImage(image=img_not)
        button.config(image=image)
        button.image = image
        #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
        #cv2.imshow('backtobgr',backtobgr)
        #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
        cv2.waitKey(0)



def img2sketch():
    img2sketch_main(filepath)





#SEPIA
    
def img3sketch_main(filepath):
        #reading image:
        input_image = cv2.imread(str(filepath))

        
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia_img = cv2.transform(input_image, kernel)
        cv2.imshow('sepia_img',sepia_img)
       

        image = tk.PhotoImage(image=sepia_img)
        button.config(image=image)
        button.image = image
        #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
        #cv2.imshow('backtobgr',backtobgr)
        #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
        cv2.waitKey(0)

def img3sketch():
    img3sketch_main(filepath)




    
#BANDW
    
def img4sketch_main(filepath):
        #reading image:
        input_image = cv2.imread(str(filepath))
        gray_img = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('gray_img',gray_img)

        image = tk.PhotoImage(image=gray_img)
        button.config(image=image)
        button.image = image
        #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
        #cv2.imshow('backtobgr',backtobgr)
        #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
        cv2.waitKey(0)


def img4sketch():
    img4sketch_main(filepath)




#CROP

def img5sketch_main(filepath):
        #reading image:
        input_image = cv2.imread(str(filepath))
        x, y, w, h = 50, 50, 200, 200
        cropped_img = input_image[y:y+h, x:x+w]

        cv2.imshow('cropped_img', cropped_img)

        image = tk.PhotoImage(image=cropped_img)
        button.config(image=image)
        button.image = image
        #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
        #cv2.imshow('backtobgr',backtobgr)
        #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
        cv2.waitKey(0)

def img5sketch():
    img5sketch_main(filepath)






#SHARPEN

def img6sketch_main(filepath):
    #reading image:
    input_image = cv2.imread(str(filepath))    
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_img = cv2.filter2D(input_image, -1, kernel)

    cv2.imshow('sharpened_img', sharpened_img)
 
    image = tk.PhotoImage(image=sharpened_img)
    button.config(image=image)
    button.image = image
    #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
    #cv2.imshow('backtobgr',backtobgr)
    #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
    cv2.waitKey(0)


def img6sketch():
    img6sketch_main(filepath)




#CONTRAST
    
def contrast_main(filepath):
    # Load image
    img = cv2.imread(str(filepath))

    # Define the contrast value
    alpha = -1.5  # for increasing the contrast
    beta = 50    # for adjusting the contrast

    # Apply the contrast adjustment
    contrast_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Display the contrast image
    
    #cv2.imshow('img',img)
    cv2.imshow('contrast image',contrast_img)
    image = tk.PhotoImage(image=contrast_img)
    button.config(image=image)
    button.image = image
    cv2.waitKey(0)

def contrast():
    contrast_main(filepath)




#X-RAY

def xray_main(filepath):
    img = cv2.imread(filepath)

    # Invert the image
    inverted_img = cv2.bitwise_not(img)

    # Display the inverted image
    
    
    cv2.imshow('inverted img',inverted_img)
    image = tk.PhotoImage(image=inverted_img)
    button.config(image=image)
    button.image = image
    #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
    #cv2.imshow('backtobgr',backtobgr)
    #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
    cv2.waitKey(0)



    

def xray():
    xray_main(filepath)




    

#BRIGHTEN
    
def brighten_main(filepath):
    # Load image
        img = cv2.imread(filepath)

    # Define the brightness value
        alpha = 1.5 # for increasing the brightness
        beta = 50   # for adjusting the brightness

    # Apply the brightness adjustment
        bright_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Display the bright image
        cv2.imshow('bright img',bright_img)
        image = tk.PhotoImage(image=brighten_img)
        button.config(image=image)
        button.image = image
    #backtobgr = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
    #cv2.imshow('backtobgr',backtobgr)
    #hsv=cv2.cvtColor(backtobgr,cv.COLOR_BGR2HSV)
        cv2.waitKey(0)
   

def brighten():
        brighten_main(filepath)










root = tk.Tk()
    
def open():

    def add_image():
        global filepath
    # Open a file dialog to select an image file
        filepath = filedialog.askopenfilename()
    
    # Create the image object
        image = tk.PhotoImage(file=filepath)
    #cv2.imshow('image',filepath)
    # Resize the image to fit the button while preserving the aspect ratio
        image = image.subsample(2, 2)
     
    # Update the image of the button
        button.config(image=image)
        button.image = image
        return filepath
    #print(filepath)

   
        

     
    
    #MAINFRAME,BUTTONS


    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("200x200")
   
    
    new_window.config(bg='cadetblue')
    # Create the button
    button = tk.Button(new_window, text="ADD IMAGE",bg = 'black', fg = 'white', command=add_image)
    button.pack(side = 'left')

    # Create a frame to hold the smaller buttons
    frame = tk.Frame(new_window)

    # Create the smaller buttons and add them to the frame
    button1 = tk.Button(frame, text="BLACK AND WHITE", width=55, height=4, bg = 'black', fg = 'white', command = img4sketch)
    button2 = tk.Button(frame, text="PENCIL SKETCH", width=55, height=4, fg = 'black', bg = 'gainsboro',command=img2sketch)
    button3 = tk.Button(frame, text="SEPIA", width=55, height=4, bg = 'black', fg = 'white', command=img3sketch)
    button4 = tk.Button(frame, text="CROP", width=55, height=4, fg = 'black', bg = 'gainsboro',command=img5sketch)
    button5 = tk.Button(frame, text="SHARPEN", width=55, height=4, bg = 'black', fg = 'white', command=img6sketch)
    button6 = tk.Button(frame, text="CONTRAST", width=55, height=4, fg = 'black', bg = 'gainsboro',command=contrast)
    button7 = tk.Button(frame, text="XRAY", width=55, height=4, bg = 'black', fg = 'white',command=xray)
    button8 = tk.Button(frame, text="BRIGHTEN", width=55, height=4, fg = 'black', bg = 'gainsboro',command=brighten)

    button1.pack(side="top")
    button2.pack(side="top")
    button3.pack(side="top")
    button4.pack(side="top")
    button5.pack(side="top")
    button6.pack(side="top")
    button7.pack(side="top")
    button8.pack(side="top")

    # Place the frame with the smaller buttons on the right side of the window
    frame.pack(side="right")







#root.mainloop()

root.config(bg='cadetblue')
photo_editor_button = tk.Button(root,width=40, height=4, text="PHOTO EDITOR",font = ('arial',30),bg = 'black',fg='white')
photo_editor_button.place(relx=0.5, rely=0.5, anchor='center')

go_button = tk.Button(root, text="GO", width = 20, height = 2,bg= 'black', fg = 'white', command=open)
go_button.place(relx=1, rely=1, anchor='se')

root.mainloop()
