from pytube import YouTube

link = input("Enter the link of the video: ")
yt = YouTube(link)
print("Title: ", yt.title)
video = yt.streams.get_highest_resolution()
print(video)
video.download("./Viedos")
print('Done')

