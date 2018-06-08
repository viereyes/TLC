from Tkinter import *
from PIL import ImageTk,Image
from subprocess import call
import subprocess as sub
import os
import sys



def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("TLC")

# ------------------FRAMES------------------------------
main = Frame(root)
voice = Frame(root)
voice.configure(background = 'black')
navigation = Frame(root)
navigation.configure(background = 'black')
mobile = Frame(root)
mobile.configure(background = 'black')
media = Frame(root)
media.grid()
media.configure(background = 'black')




for frame in (main, voice, navigation, mobile, media):
    frame.grid(row=0, column=0, sticky='news')

#----------------------IMAGES-----------------------------------------------

img = ImageTk.PhotoImage(Image.open("tlc.jpg")) 
voicepic=ImageTk.PhotoImage(Image.open("voice.jpg"))
navpic=ImageTk.PhotoImage(Image.open("nav.jpg"))
mobilepic=ImageTk.PhotoImage(Image.open("mobile.jpg"))
mediapic=ImageTk.PhotoImage(Image.open("media.jpg"))
headervoice=ImageTk.PhotoImage(Image.open("headervoice.jpg"))
headermobile=ImageTk.PhotoImage(Image.open("headermobile.jpg"))
headernav=ImageTk.PhotoImage(Image.open("headernav.jpg"))
headermedia=ImageTk.PhotoImage(Image.open("headermedia.jpg"))
home=ImageTk.PhotoImage(Image.open("home.jpg"))
backgroundpic=ImageTk.PhotoImage(Image.open("backgroundpic.jpg"))
nextb=ImageTk.PhotoImage(Image.open("next.jpg"))
prevb=ImageTk.PhotoImage(Image.open("prev.jpg"))
content=ImageTk.PhotoImage(Image.open("content.jpg"))
tune=ImageTk.PhotoImage(Image.open("tuning.jpg"))
tune1=ImageTk.PhotoImage(Image.open("tune1.jpg"))
tune2=ImageTk.PhotoImage(Image.open("tune2.jpg"))
tune3=ImageTk.PhotoImage(Image.open("tune3.jpg"))
tune4=ImageTk.PhotoImage(Image.open("tune4.jpg"))
tune5=ImageTk.PhotoImage(Image.open("tune5.jpg"))
map=ImageTk.PhotoImage(Image.open("map.jpg"))
# -----------------IMAGES FOR VOICE RECOGNITION FRAMES---------------------
headlights=ImageTk.PhotoImage(Image.open("headlights.jpg"))
engine=ImageTk.PhotoImage(Image.open("engine.jpg"))
radio=ImageTk.PhotoImage(Image.open("radio.jpg"))
doorlock=ImageTk.PhotoImage(Image.open("doorlock.jpg"))
aircon=ImageTk.PhotoImage(Image.open("aircon.jpg"))


#---------------------------BUTTONS--------------------------------------------------------

# MAIN PAGE BUTTONS---------------------------------------------------------------------------------

Label(main,image = img, height=65, width=705).grid()
voicebutton = Button(main, image = voicepic, bg = 'black', command=lambda:raise_frame(voice)).grid(row = 2,column=0,sticky =W)
navbutton = Button(main, image = navpic, bg = 'black', command=lambda:raise_frame(navigation)).grid(row = 2, column = 0,sticky=E)
mobilebutton = Button(main, image = mobilepic, bg = 'black', command=lambda:raise_frame(mobile)).grid(row = 3, column = 0,sticky =W)
mediabutton = Button(main, image = mediapic, bg = 'black', command=lambda:raise_frame(media)).grid(row = 3, column = 0,sticky =E)

#__________________*******************_______________________
# ----------------VOICE RECOGNITION FRAME--------------------
titlevoice = Label(voice, image = headervoice, height=80, width=705)
titlevoice.grid(rowspan = 2,columnspan = 5)
Button(voice, image = home, height=28, width=28, bg = 'black', command=lambda:raise_frame(main)).grid(row=0, column=0, sticky = NW)
# -------------VOICE RECOGNITION BUTTONS---------------------
b1 = Button(voice, image = headlights, bg = 'black', width = 400, height = 40, command=lambda:raise_frame(main)).grid(row = 2, column = 1)
b2 = Button(voice, image = engine, bg = 'black', width = 400, height = 40, command=lambda:raise_frame(main)).grid(row = 3, column = 1)
b3 = Button(voice, image = radio, bg = 'black', width = 400, height = 40, command=lambda:raise_frame(main)).grid(row = 4, column = 1)
b4 = Button(voice, image = doorlock, bg = 'black', width = 400, height = 40, command=lambda:raise_frame(main)).grid(row = 5, column = 1)
b5 = Button(voice, image = aircon, bg = 'black', width = 400, height = 40, command=lambda:raise_frame(main)).grid(row = 6, column = 1)
# ------------VOICE RECOGNITION LABEL------------------------
Label(voice,text='To control these car devices,', font =("Helvetica", 10), fg = 'white', bg = 'black', width = 30, height = 2).grid(row=3,column=2);
Label(voice,text=' just speak \"TLC,<command>,<device>\"', font =("Helvetica", 10), fg = 'white', bg = 'black', width = 30, height = 2).grid(row=4,column=2);
Label(voice,text='Example: \"TLC,  turn on the engine\"', font =("Helvetica", 10), fg = 'white', bg = 'black', width = 30, height = 2).grid(row=5,column=2);
# --------------END OF VOICE RECOGNITION---------------
#_______________________*******________________________


#_______________**************_____________________
#-----------------------NAVIGATIOIN FRAME------------------------------
titlenav = Label(navigation, image = headernav, height=80, width=705).grid(row = 0, column =0, columnspan = 5)
Button(navigation, image = home, height=28, width=28, bg = 'black', command=lambda:raise_frame(main)).grid(row=0, column=0, sticky = NW)
navmap = Label(navigation, image = map, height=400, width=700, bg = 'black').grid(row = 1, column= 0, columnspan = 5)
#----------------------END OF NAVIGATION FRAME----------------------------
#_______________**************_____________________

#_______________**************_____________________
#-----------------------MOBILE PHONE FRAME------------------------------
titlemobile = Label(mobile, image = headermobile, height=80, width=705).grid(row = 0, column =0, columnspan = 5)
Button(mobile, image = home, height=28, width=28, bg = 'black', command=lambda:raise_frame(main)).grid(row=0, column=0, sticky = NW)

#------------------------END OF MOBILE PHONE--------------------------------
#_______________**************_____________________

#_______________**************_____________________
#-----------------------MEDIA FRAME------------------------------

titlemedia = Label(media, image = headermedia, height=80, width=705).grid(row = 0, column =0, columnspan = 5)
Button(media, image = home, height=28, width=28, bg = 'black', command=lambda:raise_frame(main)).grid(row=0, column=0, sticky = NW)

radiostation = Label(media, text = '99.6 MHz', font =("Helvetica", 30), fg = 'white', bg = 'black', height=2, width=7).grid(row= 1, column = 0, columnspan= 5)
Button(media, image = prevb, height=30, width=45, bg = 'black', command=lambda:raise_frame(main)).grid(row=2, column=1)
Label(media,text='Previous Station', font =("Helvetica", 9), fg = 'white', bg = 'black', width = 12, height = 3).grid(row=3,column=1)
Button(media, image = nextb, height=30, width=45, bg = 'black', command=lambda:raise_frame(main)).grid(row=2, column=2, sticky = W)
Label(media,text='Next Station', font =("Helvetica", 10), fg = 'white', bg = 'black', width = 8, height = 3).grid(row=3,column=2, sticky = W)
Button(media, image = tune, height=35, width=35, bg = 'black', command=lambda:raise_frame(main)).grid(row=2, column=3)
Label(media,text='Set/Tune Channels', font =("Helvetica", 9), fg = 'white', bg = 'black', width = 15, height = 3).grid(row=3,column=3)


Button(media, image = tune1, height=18, width=60, bg = 'black', command=lambda:raise_frame(main)).grid(row=7, column=0,pady=50)
Button(media, image = tune2, height=18, width=60, bg = 'black', command=lambda:raise_frame(main)).grid(row=7, column=1,pady=50)
Button(media, image = tune3, height=18, width=60, bg = 'black', command=lambda:raise_frame(main)).grid(row=7, column=2,pady=50)
Button(media, image = tune4, height=18, width=60, bg = 'black', command=lambda:raise_frame(main)).grid(row=7, column=3,pady=50)
Button(media, image = tune5, height=18, width=60, bg = 'black', command=lambda:raise_frame(main)).grid(row=7, column=4,pady=50)

#------------------------END OF MEDIA--------------------------------




#-------end
raise_frame(main)
root.mainloop()