from pytube import YouTube
from pytube import Playlist

option=int(input("Press 1 for Video download, Press 2 for complete Playlist Download?"))
if option == 1:
    file_obj=open("DownloadVideo.txt","r")
    video_list=file_obj.readlines()

    path=input("Enter the path where you want to save the files:")

    for i in video_list:
        yt=YouTube(i.strip())
        try:
            dw=yt.streams.first()
            dw.download(path)
            print("Downloaded",i)
        except:
            import traceback
            traceback.print_exc()
            print("Download Failed for",i)
        finally:
            file_obj.close()

else:
    file_obj=open("DownloadPlaylist.txt","r")
    video_list=file_obj.readlines()

    path=input("Enter the path where you want to save the files:")

    for i in video_list:
        pt=Playlist(i.strip())
        try:
            pt.download_all(path)
            print("Downloadeded all videos from playlist ",i)
        except:
            import traceback
            traceback.print_exc()
            print("Downloads failed for playlist",i)
        finally:
            file_obj.close()
print("Task Completed. Have a good day :) ")
