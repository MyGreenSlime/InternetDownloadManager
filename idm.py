import os
import math
import requests
import threading
downloadList = []
def GetInput():
    newUrl = input("Url for download :")
    path = input("Path to save file :")
    newDict = {}
    newDict['url'] = newUrl
    newDict['path'] = path
    return newDict

def Dowloader(url, path):
    r = requests.get(url, stream=True)
    print(r.headers)
    contentSize = int(r.headers['Content-Length'])
    contentType = r.headers['Content-Type']
    chuckSize = 1024
    wrote = 0
    try:
        fileName = (r.headers['Content-Disposition'].split('\"'))[1]
    except:
        fileName = (url.split('/'))[-1]
    with open(path+fileName,'wb') as f:
        for data in r.iter_content(chuckSize):
            wrote = wrote  + len(data)
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        if contentSize != 0 and wrote != contentSize:
            print("ERROR")
def DownloadMan():
    global downloadList
    if(len(downloadList) != 0):
        for newInput in downloadList:
            thread = threading.Thread(target = Dowloader, args=(newInput['url'], newInput['path']))
            thread.start()
            thread.daemon
        downloadList = []

if __name__ == "__main__":
    while True:
        downloadList.append(GetInput())
        DownloadMan()
        
