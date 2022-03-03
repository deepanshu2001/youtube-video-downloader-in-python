# youtube video downloader
from pytube import YouTube

link=input("Enter the link of the video")
ys=YouTube(link)

print("TITLE:",ys.title)
print("Number of views:",ys.views)
print("Description of the video:",ys.description)

yt=ys.streams.get_highest_resolution()
yt.download('C:\\Users\\deepanshu\\Desktop')
