#Librarys
import tkinter as tk
#from tkinter import ttk
from tkinter import * 
import requests
import PIL.ImageGrab
from PIL import ImageTk,Image
from tkinter import messagebox
import pyautogui
import time
import datetime
import cv2
import pytesseract
import os 
from os import path
#Librarys

############################################ Create directory ###################################################
#default folder C:\gui\projects\roulette\BVNoZero\
#where I store the images. C:\gui\projects\roulette\BVNoZero\images\
# Create directory
dirName = "images"

# Create target Directory if don't exist
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:
	print("Directory " , dirName ,  " exist ")

############################################ Create directory ###################################################

############################################ Main Window ########################################################
root=Tk()
#Title of the window
root.title("Tom's BetVoyager No ZERO (no flash) Roulette Bot GUI V2.4 made in Python")
#here I put a .ico file as a picture on the window top bar.
#root.iconbitmap(r"C:\gui\projects\roulette\BVNoZero\me.ico")
root.iconbitmap("me.ico")
root.resizable(width=False, height=False)
root.configure(background='#11390F')
root.attributes('-topmost', 'true')
root.geometry('610x270+0+0')
############################################ Main Window ########################################################

##############@@@@@@@@@ New Window display Images @@@@@@@@@#######################
#The point of this window was to capture the images from the roulette table.
#And display them on the screen as each one is captured.
#To also check to see if the image exists.
#!!! The Images are used o they can match what is on the screen.!!!
#Since I have already captured all the images that I need for the Roulette wheel.
#This window is now for display only.
def showscaptureimages(): #This is the showcap window. (Will add frames and labels etc later)
    showcap = Toplevel(root)
    #Title of the window
    showcap.title("Tom's BetVoyager No ZERO (no flash) Roulette Bot GUI V2.2 made in Python Image capture window display area")
    #here I put a .ico file as a picture on the window top bar.
    showcap.iconbitmap("me.ico")
    showcap.resizable(width=False, height=False)
    showcap.configure(background='#11390F')
    showcap.attributes('-topmost', 'true')
    showcap.geometry('834x358+645+80')
    print('clicked to open the showcap window')
    
    ############################################ showcap frames #################################################
    frameshowcap = Frame(showcap, bg='green', bd=5).place(x=6, y=6, width=822, height=348)#Main frame green background with dard green border
    frame1showcap = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
    frame1showcap.place(x=10, y=10, width=814, height=340) #frame using x y w h
    
    frame2showcap = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame for numbers use picture of labels
    frame2showcap.place(x=16, y=76, width=802, height=268) #frame using x y w h
    
    frameEntry = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#entry border
    frameEntry.place(x=16, y=39, width=152, height=28) #frame using x y w h

    frameEntry = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#entry border
    frameEntry.place(x=666, y=39, width=152, height=28) #frame using x y w h
    ############################################ showcap frames #################################################

    ############################################ showcap labels #################################################
    my_label = Label(showcap,text="Enter in the the screen numbers and button names from Roulette BetVoyager", height=1,width=73, bg='black', fg='white', font=('Verdana', 12, 'bold')).place(x=12, y=12)
    my_labelx = Label(showcap,text="X", height=1,width=1, bg='black', fg='white', font=('Verdana', 12, 'bold')).place(x=304, y=40)
    my_labely = Label(showcap,text="Y", height=1,width=1, bg='black', fg='white', font=('Verdana', 12, 'bold')).place(x=459, y=40)
    ############################################ showcap labels #################################################

############################################ commands Functions definitions showscaptureimages ##################
    def number(event):
        try:
            #Numbers only
            int(my_box.get())
            int(xpos.get())
            int(ypos.get())
            print(int(my_box.get()),' is a number')
            newnuminput = str(int(my_box.get()))
            newnuminputx = str(int(xpos.get()))
            newnuminputy = str(int(ypos.get()))

            screenshotimage(newnuminput+".png",newnuminputx,newnuminputy,60,60)

        except ValueError:
            print('That is not a number')

    def buttonname(event):
        try:
            int(xpos.get())
            int(ypos.get())
            response = entry.get()
            print(response,' name of button')
            newnameinputx = str(int(xpos.get()))
            newnameinputy = str(int(ypos.get()))

            screenshotimage(response+".png",newnameinputx,newnameinputy,60,60)

        except ValueError:
            print('x y not entered')

    def locate():
        #yellow area where the numbers appear
        #Chrome 1640 204 with bookmarks bar on.
        #Edge 1666 176
        #Firefox 1620 225 with bookmarks bar and menu on.
        #Now you can locate the number on the screen wih x,y,w,h
        locatenumonscreen(1615,227,100,100)

############################################ showcap Images##################################################
    def openimages():
        global img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12
        global img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24
        global img25,img26,img27,img28,img29,img30,img31,img32,img33,img34,img35,img36
        global img5c,img25c,img1D,img5D,img10D,img25D,img100D,imgCLR,imgREB,imgAUTO,imgSPIN,imgCUR
        
        if os.path.isfile("images\\1.png"):
            img1 = ImageTk.PhotoImage(Image.open("images\\1.png"))
            sclab01 = Label(frame2showcap, image=img1).grid(row=2,column=0, padx=1, pady=1)

        if os.path.isfile("images\\2.png"):
            img2 = ImageTk.PhotoImage(Image.open("images\\2.png"))
            sclab02 = Label(frame2showcap, image=img2).grid(row=1,column=0, padx=1, pady=1)

        if os.path.isfile("images\\3.png"):
            img3 = ImageTk.PhotoImage(Image.open("images\\3.png"))
            sclab03 = Label(frame2showcap, image=img3).grid(row=0,column=0, padx=1, pady=1)

        if os.path.isfile("images\\4.png"):
            img4 = ImageTk.PhotoImage(Image.open("images\\4.png"))
            sclab04 = Label(frame2showcap, image=img4).grid(row=2,column=1, padx=1, pady=1)

        if os.path.isfile("images\\5.png"):
            img5 = ImageTk.PhotoImage(Image.open("images\\5.png"))
            sclab05 = Label(frame2showcap, image=img5).grid(row=1,column=1, padx=1, pady=1)

        if os.path.isfile("images\\6.png"):
            img6 = ImageTk.PhotoImage(Image.open("images\\6.png"))
            sclab06 = Label(frame2showcap, image=img6).grid(row=0,column=1, padx=1, pady=1)

        if os.path.isfile("images\\7.png"):
            img7 = ImageTk.PhotoImage(Image.open("images\\7.png"))
            sclab07 = Label(frame2showcap, image=img7).grid(row=2,column=2, padx=1, pady=1)

        if os.path.isfile("images\\8.png"):
            img8 = ImageTk.PhotoImage(Image.open("images\\8.png"))
            sclab08 = Label(frame2showcap, image=img8).grid(row=1,column=2, padx=1, pady=1)

        if os.path.isfile("images\\9.png"):
            img9 = ImageTk.PhotoImage(Image.open("images\\9.png"))
            sclab09 = Label(frame2showcap, image=img9).grid(row=0,column=2, padx=1, pady=1)

        if os.path.isfile("images\\10.png"):
            img10 = ImageTk.PhotoImage(Image.open("images\\10.png"))
            sclab10 = Label(frame2showcap, image=img10).grid(row=2,column=3, padx=1, pady=1)

        if os.path.isfile("images\\11.png"):
            img11 = ImageTk.PhotoImage(Image.open("images\\11.png"))
            sclab11 = Label(frame2showcap, image=img11).grid(row=1,column=3, padx=1, pady=1)

        if os.path.isfile("images\\12.png"):
            img12 = ImageTk.PhotoImage(Image.open("images\\12.png"))
            sclab12 = Label(frame2showcap, image=img12).grid(row=0,column=3, padx=1, pady=1)

        if os.path.isfile("images\\13.png"):
            img13 = ImageTk.PhotoImage(Image.open("images\\13.png"))
            sclab13 = Label(frame2showcap, image=img13).grid(row=2,column=4, padx=1, pady=1)

        if os.path.isfile("images\\14.png"):        
            img14 = ImageTk.PhotoImage(Image.open("images\\14.png"))
            sclab14 = Label(frame2showcap, image=img14).grid(row=1,column=4, padx=1, pady=1)

        if os.path.isfile("images\\15.png"):
            img15 = ImageTk.PhotoImage(Image.open("images\\15.png"))        
            sclab15 = Label(frame2showcap, image=img15).grid(row=0,column=4, padx=1, pady=1)

        if os.path.isfile("images\\16.png"):
            img16 = ImageTk.PhotoImage(Image.open("images\\16.png"))
            sclab16 = Label(frame2showcap, image=img16).grid(row=2,column=5, padx=1, pady=1)

        if os.path.isfile("images\\17.png"):    
            img17 = ImageTk.PhotoImage(Image.open("images\\17.png"))
            sclab17 = Label(frame2showcap, image=img17).grid(row=1,column=5, padx=1, pady=1)

        if os.path.isfile("images\\18.png"):    
            img18 = ImageTk.PhotoImage(Image.open("images\\18.png"))        
            sclab18 = Label(frame2showcap, image=img18).grid(row=0,column=5, padx=1, pady=1)

        if os.path.isfile("images\\19.png"):
            img19 = ImageTk.PhotoImage(Image.open("images\\19.png"))
            sclab19 = Label(frame2showcap, image=img19).grid(row=2,column=6, padx=1, pady=1)

        if os.path.isfile("images\\20.png"):    
            img20 = ImageTk.PhotoImage(Image.open("images\\20.png"))
            sclab20 = Label(frame2showcap, image=img20).grid(row=1,column=6, padx=1, pady=1)

        if os.path.isfile("images\\21.png"):
            img21 = ImageTk.PhotoImage(Image.open("images\\21.png"))
            sclab21 = Label(frame2showcap, image=img21).grid(row=0,column=6, padx=1, pady=1)        

        if os.path.isfile("images\\22.png"):
            img22 = ImageTk.PhotoImage(Image.open("images\\22.png"))
            sclab22 = Label(frame2showcap, image=img22).grid(row=2,column=7, padx=1, pady=1)

        if os.path.isfile("images\\23.png"):
            img23 = ImageTk.PhotoImage(Image.open("images\\23.png"))
            sclab23 = Label(frame2showcap, image=img23).grid(row=1,column=7, padx=1, pady=1)

        if os.path.isfile("images\\24.png"):
            img24 = ImageTk.PhotoImage(Image.open("images\\24.png"))
            sclab24 = Label(frame2showcap, image=img24).grid(row=0,column=7, padx=1, pady=1)

        if os.path.isfile("images\\25.png"):
            img25 = ImageTk.PhotoImage(Image.open("images\\25.png"))
            sclab25 = Label(frame2showcap, image=img25).grid(row=2,column=8, padx=1, pady=1)

        if os.path.isfile("images\\26.png"):
            img26 = ImageTk.PhotoImage(Image.open("images\\26.png"))
            sclab26 = Label(frame2showcap, image=img26).grid(row=1,column=8, padx=1, pady=1)

        if os.path.isfile("images\\27.png"):
            img27 = ImageTk.PhotoImage(Image.open("images\\27.png"))
            sclab27 = Label(frame2showcap, image=img27).grid(row=0,column=8, padx=1, pady=1)

        if os.path.isfile("images\\28.png"):
            img28 = ImageTk.PhotoImage(Image.open("images\\28.png"))
            sclab28 = Label(frame2showcap, image=img28).grid(row=2,column=9, padx=1, pady=1)

        if os.path.isfile("images\\29.png"):
            img29 = ImageTk.PhotoImage(Image.open("images\\29.png"))
            sclab29 = Label(frame2showcap, image=img29).grid(row=1,column=9, padx=1, pady=1)

        if os.path.isfile("images\\30.png"):
            img30 = ImageTk.PhotoImage(Image.open("images\\30.png"))
            sclab30 = Label(frame2showcap, image=img30).grid(row=0,column=9, padx=1, pady=1)

        if os.path.isfile("images\\31.png"):
            img31 = ImageTk.PhotoImage(Image.open("images\\31.png"))
            sclab31 = Label(frame2showcap, image=img31).grid(row=2,column=10, padx=1, pady=1)

        if os.path.isfile("images\\32.png"):
            img32 = ImageTk.PhotoImage(Image.open("images\\32.png"))
            sclab32 = Label(frame2showcap, image=img32).grid(row=1,column=10, padx=1, pady=1)

        if os.path.isfile("images\\33.png"):
            img33 = ImageTk.PhotoImage(Image.open("images\\33.png"))
            sclab32 = Label(frame2showcap, image=img33).grid(row=0,column=10, padx=1, pady=1)

        if os.path.isfile("images\\34.png"):
            img34 = ImageTk.PhotoImage(Image.open("images\\34.png"))
            sclab34 = Label(frame2showcap, image=img34).grid(row=2,column=11, padx=1, pady=1)

        if os.path.isfile("images\\35.png"):
            img35 = ImageTk.PhotoImage(Image.open("images\\35.png"))
            sclab34 = Label(frame2showcap, image=img35).grid(row=1,column=11, padx=1, pady=1)

        if os.path.isfile("images\\36.png"):
            img36 = ImageTk.PhotoImage(Image.open("images\\36.png"))
            sclab36 = Label(frame2showcap, image=img36).grid(row=0,column=11, padx=1, pady=1)

        #x 428 y 810 ############### Chips ###########################
        # 523 25c 629 1D 725 5D 823 10D 918 25D 1020 1140 Clear 1271 Rebet 1400 Auto
        if os.path.isfile("images\\5c.png"):
            img5c = ImageTk.PhotoImage(Image.open("images\\5c.png"))
            sclab5c = Label(frame2showcap, image=img5c).grid(row=3,column=0, padx=1, pady=1)

        if os.path.isfile("images\\25c.png"):
            img25c = ImageTk.PhotoImage(Image.open("images\\25c.png"))
            sclab25c = Label(frame2showcap, image=img25c).grid(row=3,column=1, padx=1, pady=1)

        if os.path.isfile("images\\1D.png"):
            img1D = ImageTk.PhotoImage(Image.open("images\\1D.png"))
            sclab1D = Label(frame2showcap, image=img1D).grid(row=3,column=2, padx=1, pady=1)

        if os.path.isfile("images\\5D.png"):
            img5D = ImageTk.PhotoImage(Image.open("images\\5D.png"))
            sclab5D = Label(frame2showcap, image=img5D).grid(row=3,column=3, padx=1, pady=1)

        if os.path.isfile("images\\10D.png"):
            img10D = ImageTk.PhotoImage(Image.open("images\\10D.png"))
            sclab10D = Label(frame2showcap, image=img10D).grid(row=3,column=4, padx=1, pady=1)

        if os.path.isfile("images\\25D.png"):
            img25D = ImageTk.PhotoImage(Image.open("images\\25D.png"))
            sclab25D = Label(frame2showcap, image=img25D).grid(row=3,column=5, padx=1, pady=1)

        if os.path.isfile("images\\100D.png"):
            img100D = ImageTk.PhotoImage(Image.open("images\\100D.png"))
            sclab100D = Label(frame2showcap, image=img100D).grid(row=3,column=6, padx=1, pady=1)
        #x1625 y235 ############### Chips ###########################

        #x1625 y235 ############### Buttons #########################
        if os.path.isfile("images\\Clear.png"):
            imgCLR = ImageTk.PhotoImage(Image.open("images\\Clear.png"))
            sclabCLR = Label(frame2showcap, image=imgCLR).grid(row=3,column=7, padx=1, pady=1)

        if os.path.isfile("images\\Rebet.png"):
            imgREB = ImageTk.PhotoImage(Image.open("images\\Rebet.png"))
            sclabREB = Label(frame2showcap, image=imgREB).grid(row=3,column=8, padx=1, pady=1)

        if os.path.isfile("images\\Auto.png"):
            imgAUTO = ImageTk.PhotoImage(Image.open("images\\Auto.png"))
            sclabAUTO = Label(frame2showcap, image=imgAUTO).grid(row=3,column=9, padx=1, pady=1)

        if os.path.isfile("images\\Spin.png"):
            imgSPIN = ImageTk.PhotoImage(Image.open("images\\Spin.png"))
            sclabSPIN = Label(frame2showcap, image=imgSPIN).grid(row=3,column=10, padx=1, pady=1)
############################################ showcap Images##################################################
############################################ commands Functions definitions showscaptureimages ##################
    def onclick(event):
        print("Nothing")
    openimages()    
    
    #state=DISABLED
    ############################################ showcap Entry ##################################################
    if os.path.isfile("images\\100D.png"):
        my_box = Entry(showcap, width=12, font=('Verdana', 13, 'bold'),state=DISABLED)#Numbers only
        my_box.place(x=18, y=40)
        
        xpos = Entry(showcap, width=4, font=('Verdana', 13, 'bold'),state=DISABLED)#Numbers only
        xpos.place(x=320, y=40)
        
        ypos = Entry(showcap, width=4, font=('Verdana', 13, 'bold'),state=DISABLED)#Numbers only
        ypos.place(x=476, y=40)

        entry = Entry(showcap, width=12, font=('Verdana', 13, 'bold'),state=DISABLED)#names
        entry.place(x=668, y=40)
    else:
        my_box = Entry(showcap, width=12, font=('Verdana', 13, 'bold'))#Numbers only
        my_box.bind('<Return>',number)
        my_box.place(x=18, y=40)

        xpos = Entry(showcap, width=4, font=('Verdana', 13, 'bold'))#Numbers only
        #xpos.bind("<Return>",xpos())
        xpos.place(x=320, y=40)

        ypos = Entry(showcap, width=4, font=('Verdana', 13, 'bold'))#Numbers only
        #ypos.bind("<Return>",ypos)
        ypos.place(x=476, y=40)

        entry = Entry(showcap, width=12, font=('Verdana', 13, 'bold'))#names
        ypos.bind("<Return>",buttonname)
        entry.place(x=668, y=40)
    #my_box.pack(pady=10)
    ############################################ showcap Entry ##################################################

    #state=DISABLED
    ############################################ showcap Buttons ################################################
    if os.path.isfile("images\\100D.png"):
        num_button = Button(showcap, text="Enter Number", height=1,width=13, bg='green', fg='white', font=('Verdana', 10, 'bold'),state=DISABLED,command=btnClickFunction).place(x=172, y=39)
        name_button = Button(showcap, text="Button Name", height=1,width=13, bg='green', fg='white', font=('Verdana', 10, 'bold'),state=DISABLED,command=btnClickFunction).place(x=532, y=39)
        find_button = Button(showcap, text="Find", height=1,width=7, bg='green', fg='white', font=('Verdana', 10, 'bold'),command=locate).place(x=380, y=39)
    else:
        num_button = Button(showcap, text="Enter Number", height=1,width=13, bg='green', fg='white', font=('Verdana', 10, 'bold'),command=number).place(x=172, y=39)
        name_button = Button(showcap, text="Button Name", height=1,width=13, bg='green', fg='white', font=('Verdana', 10, 'bold'),command=buttonname).place(x=534, y=39)
        find_button = Button(showcap, text="Find", height=1,width=7, bg='green', fg='white', font=('Verdana', 10, 'bold'),command=locate).place(x=380, y=39)
    ############################################ showcap Buttons ################################################
############################################ commands Functions definitions showscaptureimages ##################
##############@@@@@@@@@ New Window display Images @@@@@@@@@#######################

############################################ frames #############################################################
class frames():
    #Here I design the layout of the GUI (Graphic User Interface). Well... I got it to look good.
    frame = Frame(root, bg='green', bd=5)#Main frame green background with dard green border
    frame.place(x=6, y=6, width=598, height=260) #frame using x y w h

    frame1 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border for numbers
    frame1.place(x=10, y=10, width=590, height=210) #frame using x y w h

    frame2 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame for numbers use picture of labels
    frame2.place(x=16, y=18, width=484, height=112) #frame using x y w h

    frame12N = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#1st 12, 2nd 12, 3rd 12
    frame12N.place(x=16, y=128, width=484, height=28) #frame using x y w h

    frameEven = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#even odd etc
    frameEven.place(x=16, y=154, width=484, height=28) #frame using x y w h

    frameColumns = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#columns
    frameColumns.place(x=498, y=18, width=58, height=112) #frame using x y w h

    frameNL = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#Incoming numbers list frame border.
    frameNL.place(x=554, y=10, width=47, height=210) #frame using x y w h

    framemessages = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#bottom frame with stats.
    framemessages.place(x=10, y=224, width=590, height=36) #frame using x y w h

    frametall = Frame(root, bg='green', bd=5)#Main frame green background with dard green border
    frametall.place(x=6, y=270, width=598, height=586) #frame using x y w h

    frametall2 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border for numbers
    frametall2.place(x=10, y=275, width=590, height=576) #frame using x y w h

    framewide = Frame(root, bg='green', bd=5)#Main frame green background with dard green border
    framewide.place(x=610, y=6, width=895, height=260) #frame using x y w h

    framewide2 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border for numbers
    framewide2.place(x=616, y=10, width=884, height=251) #frame using x y w h
############################################ frames #############################################################

############################################ labels #############################################################
class labels():
    # This is the section of code which creates the a label
    # This section of labels is for the Roulette Table Squares with Numbers.
    lab01=Label(frames.frame2, text='1', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=0, padx=1, pady=1)
    lab02=Label(frames.frame2, text='2', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=0, padx=1, pady=1)
    lab03=Label(frames.frame2, text='3', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=0, padx=1, pady=1)

    lab04=Label(frames.frame2, text='4', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=1, padx=1, pady=1)
    lab05=Label(frames.frame2, text='5', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=1, padx=1, pady=1)
    lab06=Label(frames.frame2, text='6', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=1, padx=1, pady=1)

    lab07=Label(frames.frame2, text='7', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=2, padx=1, pady=1)
    lab08=Label(frames.frame2, text='8', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=2, padx=1, pady=1)
    lab09=Label(frames.frame2, text='9', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=2, padx=1, pady=1)

    lab10=Label(frames.frame2, text='10', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=3, padx=1, pady=1)
    lab11=Label(frames.frame2, text='11', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=3, padx=1, pady=1)
    lab12=Label(frames.frame2, text='12', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=3, padx=1, pady=1)

    lab13=Label(frames.frame2, text='13', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=4, padx=1, pady=1)
    lab14=Label(frames.frame2, text='14', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=4, padx=1, pady=1)
    lab15=Label(frames.frame2, text='15', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=4, padx=1, pady=1)

    lab16=Label(frames.frame2, text='16', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=5, padx=1, pady=1)
    lab17=Label(frames.frame2, text='17', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=5, padx=1, pady=1)
    lab18=Label(frames.frame2, text='18', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=5, padx=1, pady=1)

    lab19=Label(frames.frame2, text='19', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=6, padx=1, pady=1)
    lab20=Label(frames.frame2, text='20', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=6, padx=1, pady=1)
    lab21=Label(frames.frame2, text='21', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=6, padx=1, pady=1)

    lab22=Label(frames.frame2, text='22', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=7, padx=1, pady=1)
    lab23=Label(frames.frame2, text='23', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=7, padx=1, pady=1)
    lab24=Label(frames.frame2, text='24', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=7, padx=1, pady=1)

    lab25=Label(frames.frame2, text='25', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=8, padx=1, pady=1)
    lab26=Label(frames.frame2, text='26', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=8, padx=1, pady=1)
    lab27=Label(frames.frame2, text='27', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=8, padx=1, pady=1)

    lab28=Label(frames.frame2, text='28', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=9, padx=1, pady=1)
    lab29=Label(frames.frame2, text='29', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=9, padx=1, pady=1)
    lab30=Label(frames.frame2, text='30', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=9, padx=1, pady=1)

    lab31=Label(frames.frame2, text='31', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=10, padx=1, pady=1)
    lab32=Label(frames.frame2, text='32', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=10, padx=1, pady=1)
    lab33=Label(frames.frame2, text='33', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=10, padx=1, pady=1)

    lab34=Label(frames.frame2, text='34', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=2,column=11, padx=1, pady=1)
    lab35=Label(frames.frame2, text='35', height=2,width=4, bg='black', fg='white', font=('Verdana', 9, 'bold')).grid(row=1,column=11, padx=1, pady=1)
    lab36=Label(frames.frame2, text='36', height=2,width=4, bg='red', fg='white', font=('Verdana', 9, 'bold')).grid(row=0,column=11, padx=1, pady=1)

####################### landed num color change ##################
#Here I change the color of the number it landed on.
def landednumcolorchange(newnum,bgcol,rown,coln):
    #Label(frame2, text='36', height=2,width=4, bg='edc64f', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=11, padx=1, pady=1)
    Label(frames.frame2, text=newnum, height=2,width=4, bg=bgcol, fg='white', font=('Verdana', 9, 'bold')).grid(row=rown,column=coln, padx=1, pady=1)
####################### landed num color change ##################

####################### blanklabel_message #######################
def blanklabel_message(message):
    Label(frames.framemessages, text=message, height=1,width=46, bg='black', fg='white', font=('Verdana', 9, 'bold')).place(x=6, y=6)
####################### blanklabel_message #######################

#Label(framemessages, text='Stats go here... or I show what is going on...').place(x=6, y=2)
#blanklabel where I send all the resuls to.
blanklabel_message('Make sure BetVoyager Casino Roulette screen is on')

############################################ stats labels #################################################
class statslabels():
    labS01 = Label(frames.frametall2,text=" 1", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=0, padx=1, pady=1)
    labS01R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=1, padx=1, pady=1)
    labS02 = Label(frames.frametall2,text=" 2", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=0, padx=1, pady=1)
    labS02R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=1, padx=1, pady=1)
    labS03 = Label(frames.frametall2,text=" 3", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=0, padx=1, pady=1)
    labS03R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=1, padx=1, pady=1)
    labS04 = Label(frames.frametall2,text=" 4", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=0, padx=1, pady=1)
    labS04R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=1, padx=1, pady=1)
    labS05 = Label(frames.frametall2,text=" 5", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=0, padx=1, pady=1)
    labS05R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=1, padx=1, pady=1)
    labS06 = Label(frames.frametall2,text=" 6", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=0, padx=1, pady=1)
    labS06R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=1, padx=1, pady=1)
    labS07 = Label(frames.frametall2,text=" 7", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=0, padx=1, pady=1)
    labS07R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=1, padx=1, pady=1)
    labS08 = Label(frames.frametall2,text=" 8", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=0, padx=1, pady=1)
    labS08R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=1, padx=1, pady=1)
    labS09 = Label(frames.frametall2,text=" 9", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=0, padx=1, pady=1)
    labS09R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=1, padx=1, pady=1)
    labS10 = Label(frames.frametall2,text="10", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=0, padx=1, pady=1)
    labS10R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=1, padx=1, pady=1)
    labS11 = Label(frames.frametall2,text="11", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=0, padx=1, pady=1)
    labS11R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=1, padx=1, pady=1)
    labS12 = Label(frames.frametall2,text="12", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=0, padx=1, pady=1)
    labS12R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=1, padx=1, pady=1)

    labS13 = Label(frames.frametall2,text="13", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=2, padx=1, pady=1)
    labS13R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=3, padx=1, pady=1)
    labS14 = Label(frames.frametall2,text="14", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=2, padx=1, pady=1)
    labS14R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=3, padx=1, pady=1)
    labS15 = Label(frames.frametall2,text="15", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=2, padx=1, pady=1)
    labS15R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=3, padx=1, pady=1)
    labS16 = Label(frames.frametall2,text="16", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=2, padx=1, pady=1)
    labS16R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=3, padx=1, pady=1)
    labS17 = Label(frames.frametall2,text="18", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=2, padx=1, pady=1)
    labS17R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=3, padx=1, pady=1)
    labS18 = Label(frames.frametall2,text="18", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=2, padx=1, pady=1)
    labS18R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=3, padx=1, pady=1)
    labS19 = Label(frames.frametall2,text="19", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=2, padx=1, pady=1)
    labS19R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=3, padx=1, pady=1)
    labS20 = Label(frames.frametall2,text="20", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=2, padx=1, pady=1)
    labS20R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=3, padx=1, pady=1)
    labS21 = Label(frames.frametall2,text="21", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=2, padx=1, pady=1)
    labS21R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=3, padx=1, pady=1)
    labS22 = Label(frames.frametall2,text="22", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=2, padx=1, pady=1)
    labS22R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=3, padx=1, pady=1)
    labS23 = Label(frames.frametall2,text="23", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=2, padx=1, pady=1)
    labS23R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=3, padx=1, pady=1)
    labS24 = Label(frames.frametall2,text="24", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=2, padx=1, pady=1)
    labS24R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=3, padx=1, pady=1)

    labS25 = Label(frames.frametall2,text="25", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=4, padx=1, pady=1)
    labS25R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=0,column=5, padx=1, pady=1)
    labS26 = Label(frames.frametall2,text="26", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=4, padx=1, pady=1)
    labS26R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=1,column=5, padx=1, pady=1)
    labS27 = Label(frames.frametall2,text="27", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=4, padx=1, pady=1)
    labS27R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=2,column=5, padx=1, pady=1)
    labS28 = Label(frames.frametall2,text="28", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=4, padx=1, pady=1)
    labS28R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=3,column=5, padx=1, pady=1)
    labS29 = Label(frames.frametall2,text="29", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=4, padx=1, pady=1)
    labS29R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=4,column=5, padx=1, pady=1)
    labS30 = Label(frames.frametall2,text="30", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=4, padx=1, pady=1)
    labS30R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=5,column=5, padx=1, pady=1)
    labS31 = Label(frames.frametall2,text="31", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=4, padx=1, pady=1)
    labS31R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=6,column=5, padx=1, pady=1)
    labS32 = Label(frames.frametall2,text="32", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=4, padx=1, pady=1)
    labS32R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=7,column=5, padx=1, pady=1)
    labS33 = Label(frames.frametall2,text="33", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=4, padx=1, pady=1)
    labS33R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=8,column=5, padx=1, pady=1)
    labS34 = Label(frames.frametall2,text="34", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=4, padx=1, pady=1)
    labS34R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=9,column=5, padx=1, pady=1)
    labS35 = Label(frames.frametall2,text="35", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=4, padx=1, pady=1)
    labS35R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=10,column=5, padx=1, pady=1)
    labS36 = Label(frames.frametall2,text="36", height=1,width=2, bg='black', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=4, padx=1, pady=1)
    labS36R = Label(frames.frametall2,text="  ", height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=11,column=5, padx=1, pady=1)

    #Here I change the label/s with updated data from the spin count.
    def changelabel(num,rn,cln):
        Label(frames.frametall2,text=num, height=1,width=3, bg='#11390F', fg='white', font=('Verdana', 12, 'bold')).grid(row=rn,column=cln, padx=1, pady=1)
############################################ stats labels #################################################
############################################ labels #############################################################

############################################ listbox ############################################################
# This is the section of code which creates a listbox
listBoxOne=Listbox(frames.frameNL, bg='black', fg='red', relief=SUNKEN, borderwidth=1, highlightthickness=0, font=('Verdana', 9, 'bold'), width=2, height=13)
#listBoxOne.insert(1, "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")#red numbers
listBoxOne.place(x=2, y=2)

listBoxTwo=Listbox(frames.frameNL, bg='black', fg='white', relief=SUNKEN, borderwidth=1, highlightthickness=0, font=('Verdana', 9, 'bold'), width=2, height=13)
#listBoxTwo.insert(1, "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")#black number
#listBoxTwo.insert(0, " ")#black number
listBoxTwo.place(x=22, y=2)
####################### Listbox insert number ####################
def listBoxInsert(red,black):
    print(red,black)
    listBoxOne.insert(0, red) #red
    listBoxTwo.insert(0, black) #Black
####################### Listbox insert number ####################
############################################ listbox ############################################################

############################################ Entry ##############################################################
frameEntry = Frame(frames.frame1, bg='#31859B', highlightbackground="black", highlightthickness=2).place(x=246, y=174, width=64, height=25)#entry border
spinamount = Entry(frames.frame1, width=6, font=('Verdana', 10, 'bold')).place(x=248, y=176)#names
############################################ Entry ##############################################################

############################################ commands Functions definitions (def) ###############################
# this is the function called when the button is clicked
def btnClickFunction(): #defualt command (just prints 'clicked in the output') use this def for testing.
    print('clicked')

####################### screenshot image and save it to folder ###################
def screenshotimage(imagename,sx,sy,sh,sw):
    #pyautogui.screenshot('images\yellowarea.png',region = (1624,237,60,60))
    pyautogui.screenshot("images\\"+imagename,region = (sx,sy,sh,sw))
####################### screenshot image and save it to folder ###################

class variables():
    #Chips X and Y table positions.
    #Perhaps I could put these positions into an array?
    #So all you need to do. Is figure out where on the screen the chips are.
    #I used http://efigureout.com/free-utility-to-locate-mouse-cursor-position/
    chipY = 845
    chip5cX = 470    
    chip25cX = 567
    chip1DX = 668
    chip5DX = 770
    chip10DX = 864
    chip25DX = 963
    chip100DX = 1061

    #Bet X and Y table positions.
    #Perhaps I could put these positions into an array?
    #Single number positions X Y
    #1,4,7,10,13,16,19,22,25,28,31,34 Row 1
    #2,5,8,11,14,17,20,23,26,29,32,35 Row 2
    #3,6,9,12,15,18,21,24,27,30,33,36 Row 3
    TPosRow1Y = 560
    TPosRow2Y = 483
    TPosRow3Y = 411

    TPos1X = 657 #1,2,3
    TPos2X = 735 #4,5,6
    TPos3X = 812 #7,8,9
    TPos4X = 892 #10,11,12
    TPos5X = 965 #13,14,15
    TPos6X = 1043 #16,17,18
    TPos7X = 1120 #19,20,21
    TPos8X = 1198 #22,23,24
    TPos9X = 1271 #25,26,27
    TPos10X = 1348 #28,29,30
    TPos11X = 1423 #31,32,33
    TPos12X = 1500 #34,35,36

####################### Main Roulette Procedures Spin, bet, etc ##########################
##############@@@@@@@@@ Chip positions @@@@@@@@@##################################
#This clicks on the chip amount that you want to use to bet with. (num)
def clickchips(num):
    if num == 1:
        #pyautogui.click(470, 845)# Click the mouse. 5c chip
        pyautogui.click(variables.chip5cX, variables.chipY)# Click the mouse. 5c chip
    elif num == 2:
        pyautogui.click(variables.chip25cX, variables.chipY)# Click the mouse. 25c chip  
    elif num == 3:
        pyautogui.click(variables.chip1DX, variables.chipY)# Click the mouse. $1 chip
    elif num == 4:
        pyautogui.click(variables.chip5DX, variables.chipY)# Click the mouse. $5 chip
    elif num == 5:
        pyautogui.click(variables.chip10DX, variables.chipY)# Click the mouse. $10 chip
    elif num == 6:
        pyautogui.click(variables.chip25DX, variables.chipY)# Click the mouse. $25 chip 
    elif num == 7:
        pyautogui.click(variables.chip100DX, variables.chipY)# Click the mouse. $100 chip 
##############@@@@@@@@@ Chip positions @@@@@@@@@##################################

def spinme():
    for i in range(15):
        print("Spin num "+str(i))
        imgREB = pyautogui.locateOnScreen("images\\RebetS.png", region = (1110,800,560,160) ,confidence=0.9) # Rebet
        if imgREB is not None:
            pyautogui.click(1300, 845,)# Rebet
            pyautogui.click(1585, 823)# Click the mouse. Spin button
            #mousereturnto(530, 230)
            time.sleep(3)
            locatenumonscreen(1615,227,100,100)
            numberfoundonscreen()
            insertnumberintobox()
            root.update_idletasks()
            if i == 28:
                continue
                
                #break
            i += 1
        else:
            time.sleep(1)

        mousereturnto(530, 230)

##############@@@@@@@@@ Rebet @@@@@@@@@###########################################
def rebet():
    imgREB = pyautogui.locateOnScreen("images\\RebetS.png", region = (1110,800,560,160) ,confidence=0.9) # Rebet
    if imgREB is not None:
        pyautogui.click(1300, 845,)# Rebet
        pyautogui.click(1585, 823)# Click the mouse. Spin button
        time.sleep(3)
##############@@@@@@@@@ Rebet @@@@@@@@@###########################################

####################### Locate numbers from saved folder #########################
def locatenumonscreen(regx,regy,regw,regh):
    global Num01,Num02,Num03,Num04,Num05,Num06,Num07,Num08,Num09
    global Num10,Num11,Num12,Num13,Num14,Num15,Num16,Num17,Num18,Num19
    global Num20,Num21,Num22,Num23,Num24,Num25,Num26,Num27,Num28,Num29
    global Num30,Num31,Num32,Num33,Num34,Num35,Num36

    Num01 = pyautogui.locateOnScreen("images\\1.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num02 = pyautogui.locateOnScreen("images\\2.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num03 = pyautogui.locateOnScreen("images\\3.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num04 = pyautogui.locateOnScreen("images\\4.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num05 = pyautogui.locateCenterOnScreen("images\\5.png", grayscale=True, region = (regx,regy,regw,regh),confidence=0.9) #red
    Num06 = pyautogui.locateCenterOnScreen("images\\6.png", grayscale=True, region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num07 = pyautogui.locateOnScreen("images\\7.png", grayscale=True, region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num08 = pyautogui.locateOnScreen("images\\8.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black        
    Num09 = pyautogui.locateOnScreen("images\\9.png", region = (regx,regy,regw,regh),confidence=0.9) #red
    Num10 = pyautogui.locateOnScreen("images\\10.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num11 = pyautogui.locateOnScreen("images\\11.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num12 = pyautogui.locateOnScreen("images\\12.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num13 = pyautogui.locateOnScreen("images\\13.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num14 = pyautogui.locateOnScreen("images\\14.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red 
    Num15 = pyautogui.locateOnScreen("images\\15.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black   
    Num16 = pyautogui.locateCenterOnScreen("images\\16RB.png", region = (regx,regy,regw,regh)) #red 
    Num17 = pyautogui.locateOnScreen("images\\17.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num18 = pyautogui.locateCenterOnScreen("images\\18T.png", grayscale=True, region = (regx,regy,regw,regh),confidence=0.9) #red
    Num19 = pyautogui.locateCenterOnScreen("images\\19.png", grayscale=True, region = (regx,regy,regw,regh),confidence=0.9) #red
    
    Num20 = pyautogui.locateCenterOnScreen("images\\20H.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    if Num20 is not None:
        pix = pyautogui.pixel(1663, 266)
        #print(pix)
        
        pix26 = pyautogui.pixelMatchesColor(1663, 266, (17, 16, 4))#28
        pix26b = pyautogui.pixelMatchesColor(1663, 266, (148, 127, 49))#28
        pix28 = pyautogui.pixelMatchesColor(1663, 266, (80, 71, 21))#28
        pix29 = pyautogui.pixelMatchesColor(1663, 266, (0, 0, 0))#29        
        
        if pix26 is True:
            #print('yes')
            Num26 = pyautogui.pixelMatchesColor(1663, 266, (17, 16, 4))
            Num20 = None

        if pix26b is True:
            #print('yes')
            Num26 = pyautogui.pixelMatchesColor(1663, 266, (148, 127, 49))
            Num20 = None

        if pix28 is True:
            #print('yes')
            Num28 = pyautogui.pixelMatchesColor(1663, 266, (80, 71, 21))
            Num20 = None

        if pix29 is True:
            #print('yes')
            Num29 = pyautogui.pixelMatchesColor(1663, 266, (0, 0, 0))
            Num20 = None        

    Num21 = pyautogui.locateOnScreen("images\\21.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num22 = pyautogui.locateOnScreen("images\\22.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num23 = pyautogui.locateOnScreen("images\\23.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num24 = pyautogui.locateOnScreen("images\\24.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black   
    Num25 = pyautogui.locateCenterOnScreen("images\\25.png", grayscale=True, region = (regx,regy,regw,regh) ,confidence=0.9) #red   
    Num26 = pyautogui.locateCenterOnScreen("images\\26R.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num27 = pyautogui.locateOnScreen("images\\27.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    
    Num28 = pyautogui.locateCenterOnScreen("images\\28R.png", region = (regx,regy,regw,regh),confidence=0.9) #black

    Num29 = pyautogui.locateCenterOnScreen("images\\29L.png", grayscale=True, region = (regx,regy,regw,regh) ,confidence=0.9) #black
    if Num20 is None:
        pix = pyautogui.pixel(1663, 266)
        #print(pix)
        pix29 = pyautogui.pixelMatchesColor(1663, 266, (0, 0, 0))#29
        if pix29 is True:
            #print('yes')
            Num29 = pyautogui.pixelMatchesColor(1663, 266, (0, 0, 0))

    Num30 = pyautogui.locateCenterOnScreen("images\\30R.png", region = (regx,regy,regw,regh),confidence=0.9) #red
    Num31 = pyautogui.locateOnScreen("images\\31.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num32 = pyautogui.locateOnScreen("images\\32.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num33 = pyautogui.locateOnScreen("images\\33.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num34 = pyautogui.locateOnScreen("images\\34.png", region = (regx,regy,regw,regh) ,confidence=0.9) #red
    Num35 = pyautogui.locateOnScreen("images\\35.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
    Num36 = pyautogui.locateCenterOnScreen("images\\36RB.png", grayscale=True,region = (regx,regy,regw,regh) ,confidence=0.9) #red  
####################### Locate numbers from saved folder #########################

##############@@@@@@@@@ Locate number on screen @@@@@@@@@#########################
def numberfoundonscreen():  
    if Num01 is not None:
        print('Number 1 Red is found on the screen')
        blanklabel_message('Located Number 1 Red on the screen')
        landednumcolorchange('1','#edc64f',2,0)
    elif Num02 is not None:
        print('Located Number 2 Black on the screen')
        blanklabel_message('Located Number 2 Black on the screen')
        landednumcolorchange('2','#edc64f',1,0)
    elif Num03 is not None:
        print('Located Number 3 Red on the screen')
        blanklabel_message('Located Number 3 Red  on the screen')
        landednumcolorchange('3','#edc64f',0,0)

    elif Num04 is not None:
        print('Located Number 4 Black on the screen')
        blanklabel_message('Located Number 4 Black on the screen')
        landednumcolorchange('4','#edc64f',2,1)
    #elif Num05 is not None:
    elif Num05 is not None:
        print('Located Number 5 Red on the screen')
        blanklabel_message('Located Number 5 Red  on the screen')
        landednumcolorchange('5','#edc64f',1,1)
    elif Num06 is not None:
        print('Located Number 6 Black on the screen')
        blanklabel_message('Located Number 6 Black on the screen')
        landednumcolorchange('6','#edc64f',0,1)

    elif Num07 is not None:
        print('Located Number 7 Red on the screen')
        blanklabel_message('Located Number 7 Red on the screen')
        landednumcolorchange('7','#edc64f',2,2)
    elif Num08 is not None:
        print('Located Number 8 Black on the screen')
        blanklabel_message('Located Number 8 Black on the screen')
        landednumcolorchange('8','#edc64f',1,2)
    elif Num09 is not None:
        print('Located Number 9 Red on the screen')
        blanklabel_message('Located Number 9 Red on the screen')
        landednumcolorchange('9','#edc64f',0,2)

    elif Num10 is not None:
        print('Located Number 10 Black on the screen')
        blanklabel_message('Located Number 10 Black on the screen')
        landednumcolorchange('10','#edc64f',2,3)
    elif Num11 is not None:
        print('Located Number 11 Black on the screen')
        blanklabel_message('Located Number 11 Black on the screen')
        landednumcolorchange('11','#edc64f',1,3)
    elif Num12 is not None:
        print('Located Number 12 Red on the screen')
        blanklabel_message('Located Number 12 Red on the screen')
        landednumcolorchange('12','#edc64f',0,3)

    elif Num13 is not None:
        print('Located Number 13 Black on the screen')
        blanklabel_message('Located Number 13 Black on the screen')
        landednumcolorchange('13','#edc64f',2,4)
    elif Num14 is not None:
        print('Located Number 14 Red on the screen')
        blanklabel_message('Located Number 14 Red on the screen')
        landednumcolorchange('14','#edc64f',1,4)
    elif Num15 is not None:
        print('Located Number 15 Black on the screen')
        blanklabel_message('Located Number 15 Black on the screen')
        landednumcolorchange('15','#edc64f',0,4)

    elif Num16 is not None:
        print('Located Number 16 Red on the screen')
        blanklabel_message('Located Number 16 Red on the screen')
        landednumcolorchange('16','#edc64f',2,5)
    elif Num17 is not None:
        print('Located Number 17 Black on the screen')
        blanklabel_message('Located Number 17 Black on the screen')
        landednumcolorchange('17','#edc64f',1,5)
    elif Num18 is not None:
        print('Located Number 18 Red on the screen')
        blanklabel_message('Located Number 18 Red on the screen')
        landednumcolorchange('18','#edc64f',0,5)

    elif Num19 is not None:
        print('Located Number 19 Red on the screen')
        blanklabel_message('Located Number 19 Red on the screen')
        landednumcolorchange('19','#edc64f',2,6)
    elif Num20 is not None:
        print('Located Number 20 Black on the screen')
        blanklabel_message('Located Number 20 Black on the screen')
        landednumcolorchange('20','#edc64f',1,6)
        #pix = pyautogui.pixel(1663, 266)
        #print(pix)
    elif Num21 is not None:
        print('Located Number 21 Red on the screen')
        blanklabel_message('Located Number 21 Red on the screen')
        landednumcolorchange('21','#edc64f',0,6)

    elif Num22 is not None:
        print('Located Number 22 Black on the screen')
        blanklabel_message('Located Number 22 Black on the screen')
        landednumcolorchange('22','#edc64f',2,7)
    elif Num23 is not None:
        print('Located Number 23 Red on the screen')
        blanklabel_message('Located Number 23 Red on the screen')
        landednumcolorchange('23','#edc64f',1,7)
    elif Num24 is not None:
        print('Located Number 24 Black on the screen')
        blanklabel_message('Located Number 24 Black on the screen')
        landednumcolorchange('24','#edc64f',0,7)

    elif Num25 is not None:
        print('Located Number 25 Red on the screen')
        blanklabel_message('Located Number 25 Red on the screen')
        landednumcolorchange('25','#edc64f',2,8)
    elif Num26 is not None:
        print('Located Number 26 Black on the screen')
        blanklabel_message('Located Number 26 Black on the screen')
        landednumcolorchange('26','#edc64f',1,8)
    elif Num27 is not None:
        print('Located Number 27 Red on the screen')
        blanklabel_message('Located Number 27 Red on the screen')
        landednumcolorchange('27','#edc64f',0,8)

    elif Num28 is not None:
        print('Located Number 28 Black on the screen')
        blanklabel_message('Located Number 28 Black on the screen')
        landednumcolorchange('28','#edc64f',2,9)
    #elif Num28 is True:
        #print('Located Number 28 Black on the screen')
        #blanklabel_message('Located Number 28 Black on the screen')
        #landednumcolorchange('28','#edc64f',2,9)
    elif Num29 is not None:
        print('Located Number 29 Black on the screen')
        blanklabel_message('Located Number 29 Black on the screen')
        landednumcolorchange('29','#edc64f',1,9)
    elif Num30 is not None:
        print('Located Number 30 Red on the screen')
        blanklabel_message('Located Number 30 Red on the screen')
        landednumcolorchange('30','#edc64f',0,9)

    elif Num31 is not None:
        print('Located Number 31 Black on the screen')
        blanklabel_message('Located Number 31 Black on the screen')
        landednumcolorchange('31','#edc64f',2,10)
    elif Num32 is not None:
        print('Located Number 32 Red on the screen')
        blanklabel_message('Located Number 32 Red on the screen')
        landednumcolorchange('32','#edc64f',1,10)
    elif Num33 is not None:
        print('Located Number 33 Black on the screen')
        blanklabel_message('Located Number 33 Black on the screen')
        landednumcolorchange('33','#edc64f',0,10)

    elif Num34 is not None:
        print('Located Number 34 Red on the screen')
        blanklabel_message('Located Number 34 Red on the screen')
        landednumcolorchange('34','#edc64f',2,11)
    elif Num35 is not None:
        print('Located Number 35 Black on the screen')
        blanklabel_message('Located Number 35 Black on the screen')
        landednumcolorchange('35','#edc64f',1,11)
    elif Num36 is not None:
        print('Located Number 36 Red on the screen')
        blanklabel_message('Located Number 36 Red on the screen')
        landednumcolorchange('36','#edc64f',0,11)
    else:
        print('Number Not Located or did not match')
        blanklabel_message('Number Not Located or did not match')
##############@@@@@@@@@ Locate number on screen @@@@@@@@@#########################

##############@@@@@@@@@ Return Label number to original color @@@@@@@@@###########
def numberfoundonscreenreturncolor():   
    if Num01 is not None:
        landednumcolorchange('1','red',2,0)
    elif Num02 is not None:
        landednumcolorchange('2','black',1,0)
    elif Num03 is not None:
        landednumcolorchange('3','red',0,0)

    elif Num04 is not None:
        landednumcolorchange('4','black',2,1)
    elif Num05 is True:
        landednumcolorchange('5','red',1,1)
    elif Num06 is not None:
        landednumcolorchange('6','black',0,1)

    elif Num07 is not None:
        landednumcolorchange('7','red',2,2)
    elif Num08 is not None:
        landednumcolorchange('8','black',1,2)
    elif Num09 is not None:
        landednumcolorchange('9','red',0,2)

    elif Num10 is not None:
        landednumcolorchange('10','red',2,3)
    elif Num11 is not None:
        landednumcolorchange('11','black',1,3)
    elif Num12 is not None:
        landednumcolorchange('12','red',0,3)

    elif Num13 is not None:
        landednumcolorchange('13','black',2,4)
    elif Num14 is not None:
        landednumcolorchange('14','red',1,4)
    elif Num15 is not None:
        landednumcolorchange('15','black',0,4)

    elif Num16 is not None:
        landednumcolorchange('16','red',2,5)
    elif Num17 is not None:
        landednumcolorchange('17','black',1,5)
    elif Num18 is not None:
        landednumcolorchange('18','red',0,5)

    elif Num19 is not None:
        landednumcolorchange('19','red',2,6)
    elif Num20 is not None:
        landednumcolorchange('20','black',1,6)
    elif Num21 is not None:
        landednumcolorchange('21','red',0,6)

    elif Num22 is not None:
        landednumcolorchange('22','black',2,7)
    elif Num23 is not None:
        landednumcolorchange('23','red',1,7)
    elif Num24 is not None:
        landednumcolorchange('24','black',0,7)

    elif Num25 is not None:
        landednumcolorchange('25','red',2,8)
    elif Num26 is not None:
        landednumcolorchange('26','black',1,8)
    elif Num27 is not None:
        landednumcolorchange('27','red',0,8)

    elif Num28 is not None:
        landednumcolorchange('28','black',2,9)
    elif Num29 is True:
        landednumcolorchange('29','black',1,9)
    elif Num30 is not None:
        landednumcolorchange('30','red',0,9)

    elif Num31 is not None:
        landednumcolorchange('31','black',2,10)
    elif Num32 is not None:
        landednumcolorchange('32','red',1,10)
    elif Num33 is not None:
        landednumcolorchange('33','black',0,10)

    elif Num34 is not None:
        landednumcolorchange('34','red',2,11)
    elif Num35 is not None:
        landednumcolorchange('35','black',1,11)
    elif Num36 is not None:
        landednumcolorchange('36','red',0,11)
    else:
        print('Number Not Located or did not match')
        blanklabel_message('Number Not Located or did not matchh')
##############@@@@@@@@@ Return Label number to original color @@@@@@@@@###########

####################### x y freespin table positions (def) #######################
#This places the chip ($1) onto the Roulette table in free spin bet positions.
def freespin():
    #I will add in the variable positions here at some stage.
    pyautogui.click(700, 528)# Click the mouse. 1-2-4-5 corner bet
    pyautogui.click(854, 528)# Click the mouse. 7-8-10-11 corner bet
    pyautogui.click(1003, 528)# Click the mouse. 13-14-16-17 corner bet
    pyautogui.click(1154, 528)# Click the mouse. 19-20-22-23 corner bet
    pyautogui.click(1309, 528)# Click the mouse. 25-26-28-29 corner bet
    pyautogui.click(1458, 528)# Click the mouse. 31-32-34-35 corner bet
    pyautogui.click(1564, 411, clicks=3)# Click the mouse. top 2to1 bet

    pyautogui.click(1585, 823)# Click the mouse. Spin button
####################### x y freespin table positions (def) #######################
####################### Main Roulette Procedures Spin, bet, etc ##########################

##############@@@@@@@@@ Insert number into box @@@@@@@@@##########################
def insertnumberintobox():
    if Num01 is not None:
        listBoxInsert(" 1","  ")#Red
    elif Num02 is not None:
        listBoxInsert("  "," 2")#Black
    elif Num03 is not None:
        listBoxInsert(" 3","  ")#Red
    elif Num04 is not None:
        listBoxInsert("  "," 4")#Black
    elif Num05 is True:
        listBoxInsert(" 5","  ")#Red
    elif Num06 is not None:
        listBoxInsert("  "," 6")#Black
    elif Num07 is not None:
        listBoxInsert(" 7","  ")#Red
    elif Num08 is not None:
        listBoxInsert("  "," 8")#Black
    elif Num09 is not None:
        listBoxInsert(" 9","  ")#Red
    elif Num10 is not None:
        listBoxInsert("  ","10")#Black
    elif Num11 is not None:
        listBoxInsert("  ","11")#Black
    elif Num12 is not None:
        listBoxInsert("12","  ")#Red
    elif Num13 is not None:
        listBoxInsert("  ","13")#Black
    elif Num14 is not None:
        listBoxInsert("14","  ")#Red
    elif Num15 is not None:
        listBoxInsert("  ","15")#Black
    elif Num16 is not None:
        listBoxInsert("16","  ")#Red
    elif Num17 is not None:
        listBoxInsert("  ","17")#Black
    elif Num18 is not None:
        listBoxInsert("18","  ")#Red
    elif Num19 is not None:
        listBoxInsert("19","  ")#Red
    elif Num20 is not None:
        listBoxInsert("  ","20")#Black
    elif Num21 is not None:
        listBoxInsert("21","  ")#Red
    elif Num22 is not None:
        listBoxInsert("  ","22")#Black
    elif Num23 is not None:
        listBoxInsert("23","  ")#Red
    elif Num24 is not None:
        listBoxInsert("  ","24")#Black
    elif Num25 is not None:
        listBoxInsert("25","  ")#Red
    elif Num26 is not None:
        listBoxInsert("  ","26")#Black
    elif Num27 is not None:
        listBoxInsert("27","  ")#Red
    elif Num28 is not None:
        listBoxInsert("  ","28")#Black
    elif Num29 is True:
        listBoxInsert("  ","29")#Black
    elif Num30 is not None:
        listBoxInsert("30","  ")#Red
    elif Num31 is not None:
        listBoxInsert("  ","31")#Black
    elif Num32 is not None:
        listBoxInsert("32","  ")#Red
    elif Num33 is not None:
        listBoxInsert("  ","33")#Black
    elif Num34 is not None:
        listBoxInsert("34","  ")#Red
    elif Num35 is not None:
        listBoxInsert("  ","35")#Black
    elif Num36 is not None:
        listBoxInsert("36","  ")#Red
    else:
        print('Number Not Located or did not match')
        blanklabel_message('Number Not Located or did not matchh')
##############@@@@@@@@@ Insert number into box @@@@@@@@@##########################

##############@@@@@@@@@ Return Mouse to a position @@@@@@@@@######################
def mousereturnto(mx,my):
    pyautogui.moveTo(mx, my) # Move the mouse to XY coordinates. 
##############@@@@@@@@@ Return Mouse to a position @@@@@@@@@######################

##############@@@@@@@@@ Expand window to show stats @@@@@@@@@#####################
def largewin():
    root.geometry('610x862+0+0')
    butstatsB = Button(frames.framemessages, text='StatsB', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=normalwin).place(x=537, y=4)

def normalwin():
    root.geometry('610x270+0+0')
    butstatsB = Button(frames.framemessages, text='StatsB', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=largewin).place(x=537, y=4)

def widewin():
    root.geometry('1510x270+0+0')
    butstatsR = Button(frames.framemessages, text='StatsR', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=widenorm).place(x=389, y=4)

def widenorm():
    root.geometry('610x270+0+0')
    butstatsR = Button(frames.framemessages, text='StatsR', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=widewin).place(x=389, y=4)
##############@@@@@@@@@ Expand window to show stats @@@@@@@@@#####################

##############@@@@@@@@@ Locate yellowarea on the screen @@@@@@@@@#################
miss = 0
spin = 0
maxmiss = 0

def yellowareaonscreen():
    #First I chekc to see if the yellow blank area is on the screen before I spin.
    global img,miss,spin,maxmiss
    yellowarea = pyautogui.locateOnScreen("images\\yellowarea.png", region = (1615,227,100,100) ,confidence=0.9) #yellowarea
    if yellowarea is not None:
        print('located yellow area on the screen')
        blanklabel_message("located yellow area on the screen")
        clickchips(1)
        freespin()
        mousereturnto(530, 230)
        time.sleep(3)
        screenshotimage('Num.png',1626,235,60,60)
        img = ImageTk.PhotoImage(Image.open("images\\Num.png"))
        imgtaken = Label(root, image=img, height=48,width=50,).place(x=500, y=130)

        locatenumonscreen(1615,227,100,100)
        numberfoundonscreen()
        insertnumberintobox()
    else:
        locatenumonscreen(1615,227,100,100)
        numberfoundonscreenreturncolor()

        rebet()
        screenshotimage('Num.png',1626,235,60,60)
        img = ImageTk.PhotoImage(Image.open("images\\Num.png"))
        imgtaken = Label(root, image=img, height=48,width=50,).place(x=500, y=130)

        locatenumonscreen(1615,227,100,100)
        numberfoundonscreen()
        insertnumberintobox()

        spin += 1
        miss += 1
        print("Spin num "+str(spin))

        misscount()

        mousereturnto(530, 230)
        #pyautogui.click(530, 230, clicks=2)# Click the mouse. top 2to1 bet
##############@@@@@@@@@ Locate yellowarea on the screen @@@@@@@@@#################
############################################ commands Functions definitions (def) ###############################

############################################ Buttons ############################################################
class buttons():
    # this is the function called when the button is clicked
    butstatsR = Button(frames.framemessages, text='StatsR', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=widewin).place(x=389, y=4)
    butRNG = Button(frames.framemessages, text='RNG', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=441, y=4)
    #Now to make the screen caputre image GUI.
    butcapimg = Button(frames.framemessages, text='Images', width=6, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=showscaptureimages).place(x=477, y=4)
    butstatsB = Button(frames.framemessages, text='StatsB', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=largewin).place(x=537, y=4)

    if os.path.isfile("images\\100D.png"):
        print ("File 100.png exist")    
        Button(frames.frame1, text='SPIN', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=yellowareaonscreen).place(x=488, y=174)
    else:
        print ("File 100.png does not exist")
        Button(frames.frame1, text='SPIN', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), state=DISABLED,command=btnClickFunction).place(x=488, y=174)

    Button(frames.frame12N, text='1st 12', height=1,width=19, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=0, y=0)
    Button(frames.frame12N, text='2nd 12', height=1,width=18, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=163, y=0)
    Button(frames.frame12N, text='3rd 12', height=1,width=19, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=319, y=0)

    Button(frames.frameEven, text='1-18', height=1,width=9, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=0, y=0)
    Button(frames.frameEven, text='EVEN', height=1,width=9, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=80, y=0)
    Button(frames.frameEven, text='RED', height=1,width=9, bg='red', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=162, y=0)
    Button(frames.frameEven, text='BLACK', height=1,width=9, bg='black', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=238, y=0)
    Button(frames.frameEven, text='ODD', height=1,width=9, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=318, y=0)
    Button(frames.frameEven, text='19-36', height=1,width=9, bg='green', fg='white', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=399, y=0)

    Button(frames.frameColumns, text='2to1', height=2,width=6, bg='green', fg='white', font=('Verdana', 8, 'bold'), command=btnClickFunction).place(x=0, y=0)
    Button(frames.frameColumns, text='2to1', height=2,width=6, bg='green', fg='white', font=('Verdana', 8, 'bold'), command=btnClickFunction).place(x=0, y=37)
    Button(frames.frameColumns, text='2to1', height=2,width=6, bg='green', fg='white', font=('Verdana', 8, 'bold'), command=btnClickFunction).place(x=0, y=73)

    Button(frames.frame1, text='AUTO', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=spinme).place(x=438, y=174)
    Button(frames.frame1, text='REBET', width=6, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=380, y=174)
    Button(frames.frame1, text='CLEAR', width=6, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=322, y=174)

    Button(frames.frame1, text='100', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=206, y=174)
    Button(frames.frame1, text='25', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=172, y=174)
    Button(frames.frame1, text='10', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=139, y=174)
    Button(frames.frame1, text=' 5 ', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=106, y=174)
    Button(frames.frame1, text=' 1 ', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=72, y=174)
    Button(frames.frame1, text='25c', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=38, y=174)
    Button(frames.frame1, text='5c', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'), command=btnClickFunction).place(x=4, y=174)
############################################ Buttons ############################################################

root.mainloop()
