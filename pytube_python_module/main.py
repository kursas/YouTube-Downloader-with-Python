from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download('D:/DUMENYS/DARIUS/Desktop')
print("Download completed!!")

#output
Enter the link of YouTube video you want to download:  https://www.youtube.com/watch?v=eEbi7wdZNV4
Title:  Пишу простую, но реальную программу. Python + Excel.
Number of views:  66118
Length of video:  1128
Rating of video:  None
Downloading...
Download completed!!

Process finished with exit code 0
