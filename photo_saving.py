import os
from PIL import Image
import shutil
from constants import *

class Service:
    def __init__(self):
        self.upload_folder = UPLOADED_PHOTO_SAVING_FOLDER_KEY

    def start_process(self):
        counter=1
        if os.path.exists(OUTPUT_FILES):
            shutil.rmtree(OUTPUT_FILES)
        os.makedirs(OUTPUT_FILES)

        for file in os.listdir(self.upload_folder):
            if file.endswith(('.jpg','.jpeg','.png')):
                #os.rename(os.path.join(self.upload_folder,file),os.path.join(OUTPUT_FILES,f"{counter}.jpeg"))
                im = Image.open(os.path.join(self.upload_folder, file))
                im = im.save(os.path.join(OUTPUT_FILES,f"{counter}.jpg"))
                counter+=1
        shutil.make_archive(CURRENT_TIMESTAMP, 'zip',OUTPUT_FILES)
        shutil.rmtree(self.upload_folder)
        shutil.rmtree(OUTPUT_FILES)
        return CURRENT_TIMESTAMP+".zip"
