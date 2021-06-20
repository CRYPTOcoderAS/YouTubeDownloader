import tkinter as tk
from pytube import YouTube      #pip install pytube3
def downloadVid():
    global E1
    string=E1.get()
    yt=YouTube(str(string))
    videos=yt.get_videos()
    s=1
    for v in videos:
        print(str(s)+'.'+str(v))
        s+=1
    n=int(input("Enter Your Choice"))
    vid=videos[n-1]
    destination=str(input("Enter Destination "))
    vid.download(destination)
    print(yt.filename+"\n has been downloaded")
root=tk.Tk()
w=tk.Label(root,text="Youtube Downloader")
w.pack()

E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)

button=tk.Button(root,text="DOWNLOAD",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()


