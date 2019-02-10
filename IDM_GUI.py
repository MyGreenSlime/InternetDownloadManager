from Downloader_GUI import Downloader_GUI 
import tkinter as tk
from os import path
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
import sys
import multiprocessing
class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("DownloadManager")
        self.win.resizable(False,False)
        self.create_widgets()
        
    def create_widgets(self):
        
        tabControl =ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = 'main')
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = 'dowload list')
        tabControl.pack(expand = '1', fill = 'both')

        mighty = ttk.LabelFrame(tab1, text = 'Main')
        mighty.grid(column = 0, row = 0, padx = 8, pady = 4)

        urlLabel = ttk.Label(mighty, text = 'URL : ')
        urlLabel.grid(column = 0, row = 0, pady = 5)

        self.url = tk.StringVar()
        urlInput = ttk.Entry(mighty,width=50, textvariable=self.url)
        urlInput.grid(column =  1 , row = 0, pady = 5)

        pathLabel = ttk.Label(mighty, text = 'Path : ')
        pathLabel.grid(column = 0, row = 1, pady = 5)

        pathFrame = ttk.Frame(mighty)
        pathFrame.grid(column = 1, row = 1, pady = 5)

        self.path = tk.StringVar()
        pathInput = ttk.Entry(pathFrame,width = 35, textvariable=self.path, state='readonly')
        pathInput.grid(column =  0 , row = 0, pady = 5)
        pathButt = ttk.Button(pathFrame, text = " path to save", width = 13, command = self.getPathSave)
        pathButt.grid(column = 1, row = 0 )

        dowloandButt = ttk.Button(mighty, text = 'download', command = self.callDownloader)
        dowloandButt.grid(column = 1, row = 2)

    def getPathSave(self):
        self.path.set(fd.askdirectory())
    def callDownloader(self):
        url = self.url.get()
        path = self.path.get()
        if url == '' or path == '':
            messagebox.showwarning("Warning", "Please fill the URL or Save address")
        else:
            url = self.url.get()
            path = self.path.get()+"/"
            p = multiprocessing.Process(target= Downloader_GUI , args = (url, path))
            p.start()
def main():
    idm = Window()
    idm.win.mainloop()

if __name__ == "__main__":
    main()