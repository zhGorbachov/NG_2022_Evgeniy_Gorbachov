import requests
from bs4 import BeautifulSoup
import os
import shutil
import threading


headers = {
    'User-Agent': '...',
    'referer': 'https://...'}
listOfType = ["jpg", "jpeg", "png", "gif", "ico", "svg"]
name = "images"


def createFile():
    try:
        for file in os.scandir(name):
            os.remove(file)
        os.rmdir(name)
    except:
        pass
    os.mkdir(name)


def createZipFile():
    try:
        os.remove(name + ".zip")
    except:
        pass
    shutil.make_archive(name, "zip", name)


def manager():
    threads = []
    threads.append(threading.Thread(target=createZipFile()))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def parsingImages(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    images = soup.findAll("img")
    return images


def downloadImages(images):
    indexOfPicture = 1
    createFile()
    for image in images:
        imageUrl = image["src"]
        if imageUrl.split(".")[-1] in listOfType:
            readyImage = requests.get(imageUrl).content
            with open(name + "/picture_" + str(indexOfPicture) + "." + imageUrl.split(".")[-1], "wb+") as folder:
                folder.write(readyImage)
            print("Picture_" + str(indexOfPicture) + " was downloaded")
            indexOfPicture += 1
    print("Downloaded images: " + str(indexOfPicture - 1))
    manager()