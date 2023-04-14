import os
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
                os.rename(os.path.join(self.upload_folder,file),os.path.join(OUTPUT_FILES,f"{counter}.jpeg"))
                counter+=1
        shutil.make_archive(OUTPUT_FILES, 'zip',OUTPUT_FILES)
        return OUTPUT_FILES+".zip"
