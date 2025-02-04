from zipfile import ZipFile
import os


if os.path.exists("c:/PySetup"):

    if  os.path.exists("c:/PySetup/test"):
        with ZipFile("data.bin", "a") as myzip:
            myzip.extractall(path="C:/PySetup/test", members=None, pwd=None)

else:
    os.mkdir("c:/PySetup")
    os.mkdir("c:/PySetup/test")
    with ZipFile("data.bin", "a") as myzip:
        myzip.extractall(path="C:/PySetup/test", members=None, pwd=None)
