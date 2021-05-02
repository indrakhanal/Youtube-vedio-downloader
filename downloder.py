import tkinter as ttk
from tkinter import *
from pytube import YouTube
from pytube.cli import on_progress
from tkinter import messagebox as ms
from tkinter.ttk import *
import time


class YouTubeDownloder(Tk):
    def __init__(self):
        super(YouTubeDownloder, self).__init__()
        self.title('YouTube Video Downloader')
        self.minsize(500, 500)
        self.form_()
        self.bytes = 0
        self.maxbytes = 0

    def form_(self):
        self.label_frame = LabelFrame(self, text='Enter Video URL for Download')
        self.label_frame.grid(column=0, row=0)
        # font = ("monaco", 16, 'bold')

        label = Label(self.label_frame, text='Enter URL', font=("monaco", 16))
        label.grid(column=1, row=0, padx=12, pady=8)

        self.url = Entry(self.label_frame, width=80)
        self.url.grid(column=1, row=1)

        label2 = Label(self.label_frame, text='', font=("monaco", 16))
        label2.grid(column=1, row=2, padx=12, pady=8)

        button1 = ttk.Button(self.label_frame, text='Download Now', width=15, command=self.downloader)
        button1.grid(column=1, row=3)

        button2 = ttk.Button(self.label_frame, text='view detail', width=15, command=self.view_progress)
        button2.grid(column=1, row=5)

        label3 = Label(self.label_frame, text='', font=("monaco", 16))
        label3.grid(column=1, row=4, padx=12, pady=8)

    def downloader(self):
        try:
            link = self.url.get()
            # Label(self, text='video starts downloading !!').grid(column=0, row=3)
            if len(link) != 0:
                self.video = YouTube(link)

                self.stream = self.video.streams.get_highest_resolution()
                self.stream.download()

                self.maxbytes = self.stream.filesize
                Label(self.label_frame, text='video download successfully !!').grid(column=1, row=4)
            else:
                ms.showerror('Error!', 'url Should be Filled out')
        except:
            ms.showerror('Error!!', 'No internet or invalid Url')

    def view_progress(self):
        try:
            if self.maxbytes != 0:
                self.label_frame1 = LabelFrame(self, text='Downloaded Media Information')
                self.label_frame1.grid(column=0, row=1)

                self.progress = Progressbar(self.label_frame1, orient=HORIZONTAL, length=200, mode='determinate')
                self.progress.grid(column=0, row=8)

                self.progress["value"] = 0
                self.progress["maximum"] = self.maxbytes
                self.read_bytes()

                title = self.video.title
                captions = self.video.captions
                Label(self.label_frame1, text=f'Video Title: {title}').grid(column=0, row=5)
                Label(self.label_frame1, text=f'Total Size: {int(self.maxbytes / (1024 * 1024))}MB ').grid(column=0, row=6)
                Label(self.label_frame1, text=f'Captions: {captions} ').grid(column=0, row=7)

            else:
                ms.showerror('Error!!', 'video not downloaded yet')
        except:
            ms.showwarning('Error!!', 'video not downloaded yet')

    def read_bytes(self):
        self.bytes += 5000000
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(1000, self.read_bytes)
            print(self.progress["value"])


y_tub = YouTubeDownloder()
y_tub.mainloop()



