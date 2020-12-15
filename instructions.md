Instructions for
Tom's BetVoyager No ZERO (no flash) Roulette Bot GUI V2.2 made in Python

You will need to install the Python Librarys yourself...

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

(A work in progress)

At the moment. I am still learning how to code in Python.
And put the focus on this Roulette script.
The Python script does not bet as yet.
All the script does is it looks for a yellow area.
If if finds it. It places a bet and spins.
Puts the number on the screen.

The Images window.
I created to take the pictures of the numbers.
Using x y coords. (Screen position of the where the numbers appear)

You will need to have BetVoyager casino open in FireFox. (With the Menu Bar and the Bookmarks bar ON)
https://betvoyager.com/

BetVoyager casino screen.

[![main.png](https://1.bp.blogspot.com/-M4tYXUrHqC4/X9g95XxEcGI/AAAAAAAAEaM/S1X2N3FX-3k-ws2_R0LDaL6bY7Xl-krbACLcBGAsYHQ/s320/bv-main.jpg)](https://1.bp.blogspot.com/-M4tYXUrHqC4/X9g95XxEcGI/AAAAAAAAEaM/S1X2N3FX-3k-ws2_R0LDaL6bY7Xl-krbACLcBGAsYHQ/s320/bv-main.jpg)

BetVoyager No Zero Roulette.

[![bv-rol-no-zero.png](https://1.bp.blogspot.com/-PToSMdNgS8A/X9g96QE2C6I/AAAAAAAAEaY/fmYB2IJQngsh4M0JweSG5bDW8PaXedktgCLcBGAsYHQ/s320/bv-rol-no-zero.jpg)](https://1.bp.blogspot.com/-PToSMdNgS8A/X9g96QE2C6I/AAAAAAAAEaY/fmYB2IJQngsh4M0JweSG5bDW8PaXedktgCLcBGAsYHQ/s320/bv-rol-no-zero.jpg)

What the Python GUI(Graphic User Interface) looks like.

[![bv-bot-main.png](https://1.bp.blogspot.com/-zpKGXV0avGQ/X9g94yvG77I/AAAAAAAAEaI/302u_aL5XMI5zMIVxVq4nJ0c_31QMlzxgCLcBGAsYHQ/s320/bv-bot-main.jpg)](https://1.bp.blogspot.com/-zpKGXV0avGQ/X9g94yvG77I/AAAAAAAAEaI/302u_aL5XMI5zMIVxVq4nJ0c_31QMlzxgCLcBGAsYHQ/s320/bv-bot-main.jpg)

What the Python GUI(Graphic User Interface) looks like. 
Images Window: (Where I can see the images I saved.)

[![bv-bot-images.png](https://1.bp.blogspot.com/-SuziDomjk_I/X9g94PAYKbI/AAAAAAAAEZ8/NGLzNuNHHYMXVuq43sx6fZpjHH4nYJBDwCLcBGAsYHQ/s320/bv-bot-images.jpg)](https://1.bp.blogspot.com/-SuziDomjk_I/X9g94PAYKbI/AAAAAAAAEZ8/NGLzNuNHHYMXVuq43sx6fZpjHH4nYJBDwCLcBGAsYHQ/s320/bv-bot-images.jpg)

Images Window:
This where you capture the numbers from the casino and save them to the folder.

[![v-bot-images-enter.png](https://1.bp.blogspot.com/-wZ3JoMQdiMk/X9g94fEooVI/AAAAAAAAEaE/vrIytNjOa5Y1zqrLgXVnt6FO9i6mDdQVQCLcBGAsYHQ/s836/bv-bot-images-enter.jpg)](https://1.bp.blogspot.com/-wZ3JoMQdiMk/X9g94fEooVI/AAAAAAAAEaE/vrIytNjOa5Y1zqrLgXVnt6FO9i6mDdQVQCLcBGAsYHQ/s836/bv-bot-images-enter.jpg)

[![bv-bot-main.png](https://1.bp.blogspot.com/-BEWbHQAxDSk/X9g94AdaIaI/AAAAAAAAEaA/mNGWvixORM4He5TdsO3hyy_x70VlwqHrQCLcBGAsYHQ/s1920/bv-bot-images-enter-coords.jpg)](https://1.bp.blogspot.com/-BEWbHQAxDSk/X9g94AdaIaI/AAAAAAAAEaA/mNGWvixORM4He5TdsO3hyy_x70VlwqHrQCLcBGAsYHQ/s1920/bv-bot-images-enter-coords.jpg)
