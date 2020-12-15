NOTE: Though I named this file howitworks.py it is NOT a .py script.

NOTE: All X Y coords are for FireFox With Menu and Bookmars bar open.
You will need to change the X and Y values if you have issues with the script working.

The Python Script is very well laid out.
And has notes for my own benefit.

What the Python Script does.

1. Creates a folder if there isn't one.
dirName = "images"

# Create target Directory if don't exist
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:
	print("Directory " , dirName ,  " exist ")

The def showscaptureimages(): is a window that shows the captured images.
And it also is used to capture the images to save to the folder.
You need to give the images names.
"images\\1.png" etc... (all 36 numbers)
And you need to save the roulette button images.
"images\\Clear.png" etc...
And the chip images.
"images\\100D.png" etc...

The best part of the script so far.
This section locates the image on the screen.
I tried to use OpenCV and tesseract.
To do OCR (Optical Character Recogniton.)
But could not get it to work.

So I found 
pyautogui.locateOnScreen
pyautogui.locateCenterOnScreen
To work
It locates the image you have saved.
And looks for it on the screen.

def locate():
#yellow area where the numbers appear
#Chrome 1640 204 with bookmarks bar on.
#Edge 1666 176
#Firefox 1620 225 with bookmarks bar and menu on.
#Now you can locate the number on the screen wih x,y,w,h
locatenumonscreen(1615,227,100,100)

Num04 = pyautogui.locateOnScreen("images\\4.png", region = (regx,regy,regw,regh) ,confidence=0.9) #black
Num05 = pyautogui.locateCenterOnScreen("images\\5.png", grayscale=True, region = (regx,regy,regw,regh),confidence=0.9) #red

I also found out that grayscale=True seemed to make the image recognition work better.
However, even with this. I was still only getting about 90% of the images to locate on the screen.
So I had to change some of the saved images.
And also use 
pix = pyautogui.pixel(1663, 266)
And
pix26 = pyautogui.pixelMatchesColor(1663, 266, (17, 16, 4))#28
To see if the pixel in that area would match.

The rest of the script deals with the table and color operations.
def numberfoundonscreen():  
    if Num01 is not None:
        print('Number 1 Red is found on the screen')
        blanklabel_message('Located Number 1 Red on the screen')
        landednumcolorchange('1','#edc64f',2,0)

def numberfoundonscreenreturncolor():   
    if Num01 is not None:
        landednumcolorchange('1','red',2,0)

def insertnumberintobox():
    if Num01 is not None:
        listBoxInsert(" 1","  ")#Red
        
      
