from pytube import YouTube

def download_video(link, format='mp4'):
    youtube = YouTube(link)
    video = youtube.streams.filter(file_extension=format).first()
    video.download()
    print(f'The video has been successfully downloaded in {format} format.')

link = input("Enter the YouTube video URL: ")
download_video(link)
