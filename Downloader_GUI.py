import tkinter as tk
from os import path
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from Downloader import Downloader 
import threading
import sys
class Downloader_GUI():
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.win = tk.Tk()
        self.progressVar = tk.IntVar()
        self.progressVar.set(0)
        self.win.title("DownloadManager")
        self.win.resizable(False,False)
        self.create_widgets()
        self.download()
        self.win.mainloop()
        
    def download(self):
        self.downloader = Downloader(self, self.url, self.path)
        self.thread = threading.Thread(target = self.downloader.download)
        self.thread.start()

    def create_widgets(self):
        mighty = ttk.LabelFrame(self.win, text = 'Downloader')
        mighty.grid(column = 0, row = 0, padx = 8, pady = 4)

        frameData = ttk.Frame(mighty)
        frameData.grid(column = 0, row = 0)
        self.urlLabel = ttk.Label(frameData, text = 'URL : ')
        self.urlLabel.grid(column = 0, row = 0, pady = 5)

        self.urlShow = ttk.Label(frameData,width=50, text = self.url)
        self.urlShow.grid(column =  1 , row = 0, pady = 5)

        self.pathLabel = ttk.Label(frameData, text = 'Path : ')
        self.pathLabel.grid(column = 0, row = 1, pady = 5)

        self.pathShow = ttk.Label(frameData,width=50, text = self.path)
        self.pathShow.grid(column =  1 , row = 1, pady = 5)

        frameProgress = ttk.Frame(mighty)
        frameProgress.grid(column = 0,row = 1)
        self.progressBar=ttk.Progressbar(frameProgress,orient='horizontal',length=320,mode='determinate', variable = self.progressVar)
        self.progressBar.grid(column = 0 , row = 0)

        self.progressPercent = ttk.Label(frameProgress, text =  "0 / 100 %")
        self.progressPercent.grid(column = 1, row = 0, padx = 2)

    def updateprogress(self,newProgress):
        self.progressVar.set(newProgress)
        self.progressPercent.configure(text=  str(newProgress)+" / 100 %")
    
    def finish(self):
        self.thread._delete()
        self.win.quit()
        self.win.destroy()
        exit()
        sys.exit()

    def fileerror(self):
        messagebox.showerror("Error", "File Error")
        self.finish()
    def nodiskspace(self):
        messagebox.showerror("Error", "File is too big")
        self.finish()