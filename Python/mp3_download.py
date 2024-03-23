from pytube import YouTube
import os

def mp3_downloader():
    yt = YouTube(
        str(input("Enter URL: \n>>")))
    
    video = yt.streams.filter(only_audio=True).first()

    print("Enter Download Directory: ")
    destination = str(input(">> ")) or '.'

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    mp3_downloader()