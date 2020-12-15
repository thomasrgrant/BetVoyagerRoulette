Here are some of the issues with the script.
1. Loops and input.
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
        
The loop works.
However, while it loops. It does not update the window.
insertnumberintobox()

Issue with some of the numbers.
Even with 
pyautogui.locateOnScreen
and
pyautogui.locateCenterOnScreen
I still get one or two numbers that it has issues with finding on the screen.
The Numbers it has issues with.
Num 5, 26, 28, 29 and possibly a few more.
Num05 = pyautogui.locateCenterOnScreen("images\\5.png", grayscale=True, region = (regx,regy,regw,regh),confidence=0.9) #red
For the most part.
Its fairly accurate.
Seems to work better with just the spin function.
The loop gives it some issues with numbers.
