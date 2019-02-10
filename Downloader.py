import os
import math
import requests
import sys
class Downloader():
    def __init__(self,gui, url, path):
        self.url = url
        self.path = path
        self.gui = gui
    def download(self):
        try:
            r = requests.get(self.url, stream = True)
            contentSize = int(r.headers['Content-Length'])
            contentType = r.headers['Content-Type']
        except:
            self.gui.fileerror()
        
        chuckSize = 1024
        wrote = 0
        
        try:
            fileName = (r.headers['Content-Disposition'].split('='))[-1]
            fileName = fileName.split('\"')[1]
            fileName = fileName.split('.')[0]
            typefile = contentType.split('/')[1]
            fileName = fileName+"."+typefile
        except:
            fileName = (self.url.split('/'))[-1]
            fileName = fileName.split('.')[0]
            typefile = contentType.split('/')[1]
            fileName = fileName+"."+typefile
        with open(self.path+fileName,'wb') as f:
            for data in r.iter_content(chuckSize):
                wrote = wrote + len(data)
                f.write(data)
                f.flush()
                self.calprogress(wrote, contentSize)
            if contentSize != 0 and wrote != contentSize:
                os.remove(self.path+fileName)
                self.gui.finish()
            else:
                self.gui.finish()
    
    def calprogress(self, wrote, contentSize):
        percent  = round(wrote/contentSize*100)
        self.gui.updateprogress(percent)
