'''organise(path) organises all files in path into directories defined in the directories list.
Add a / (linux, unix) or double backslash(Windows) to the end of the path'''

import os
import shutil

#Defining the file types
directories = ["image", "document", "video", "audio", "musescore", "fonts",
"software", "code"]
image = ["jpg", "png", "jpeg"]
document = ["pdf", "docx", "csv"]
video = ["mp4"]
audio = ["wav", "mp3"]
musescore = ["mscz"]
fonts = ["tff", "otf","ttf"]
software = ["zip", "exe", "sh","conf"]
code = ["c", "py", "html"]

#File class. type and directory name must be equal.
class File(object):
    def __init__(self, location, extension = "", type = ""):
        self.location = location
        self.extension = location.rpartition('.')[-1]
        if self.extension in image:
            self.type = "image"
        elif self.extension in document:
            self.type = "document"
        elif self.extension in video:
            self.type = "video"
        elif self.extension in audio:
            self.type = "audio"
        elif self.extension in musescore:
            self.type = "musescore"
        elif self.extension in fonts:
            self.type = "fonts"
        elif self.extension in software:
            self.type = "software"
        elif self.extension in code:
            self.type = "code"
        else:
            self.type ="null"

def organize(path):
    print("WARNING:")
    print("Files with same name will be replaced while moving.")
    print("No changes to folders not in directories list(see code)")
    print("[y/n]", end = " ")
    n = input()
    if n =='y':
        files = os.listdir(path)

        for directory in directories:
            try:
                os.mkdir(path + directory) 
            except:
                pass
            
        for f in files:
            file = File(path + f)
            if file.type != 'null':
                shutil.move(file.location, path+file.type)
            del file