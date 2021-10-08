#For this exercise I use a library called "Pytube" that bring us the possibility to download videos:

# importing pytube
from pytube import YouTube

# here's where the video is going to be saved
SAVE_PATH = "/Users/mariorobles/Desktop" #you can customize the path

#just a welcome
print("Hi! welcome to the python youtube video downloader! ヽ(・∀・)ﾉ")

# link of the video 
link=input("Please paste the link of the video you want to download!ᕕ( ᐛ )ᕗ : \n")
yt = YouTube(link)



#Just feedback for the user
print("Downloading! (¬‿¬ ")

#here the object is created using YouTube
video = yt.streams.get_highest_resolution()


# downloading the video
video.download(SAVE_PATH)

print('Your video was downladed! ヾ(☆▽☆)')