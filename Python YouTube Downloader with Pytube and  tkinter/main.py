#ques:where can you find the download?
#answ:In the same folder where you have python where you have code

from tkinter import *
from pytube import YouTube

#Create Display Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

#Create Field to Enter Link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#Create Function to Start Downloading
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()

#output
Process finished with exit code 0
