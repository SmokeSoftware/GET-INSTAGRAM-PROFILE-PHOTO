import tkinter as tk
from tkinter import*
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import urllib
from PIL import Image

APP = tk.Tk()
APP.title("GET-İNSTA-PHOTO")
APP.minsize(350,150)
APP.maxsize(350,150)


def GET_PHOTO():
    profile_url = str(APP_GET_DATA.get())
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile_image = soup.find("meta", property="og:image")["content"]
    urllib.request.urlretrieve(profile_image, "profile_image.png")
    MSG = Tk()
    MSG.withdraw()
    messagebox.showinfo("İNFORMATİON","THE İMAGE WAS SUCCESFULLY SAVED!")
    return 0


APP_İNFO = tk.Label(APP,text = "ENTER\n\n İNSTAGRAM\n\n LİNK:",fg = "cyan",bg = "black",font = "Arial 13")
APP_İNFO.place(width = 100,height = 100,x = 0,y = 0)

APP_GET_DATA = tk.Entry(APP,fg = "blue",bg = "white",font = "Arial 25")
APP_GET_DATA.place(width = 250,height = 100,x = 100,y = 0)

APP_BUTTON = tk.Button(APP,text = "DOWNLOAD PROFİLE PHOTO",fg = "lime",bg = "black",activeforeground = "black",activebackground = "lime",font = "Arial 17",command = GET_PHOTO)
APP_BUTTON.place(width = 350,height = 50,x = 0,y = 100)



APP.mainloop()

