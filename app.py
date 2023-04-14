from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from constants import *
from photo_saving import Service
import os
import shutil

app = Flask(__name__)
app.secret_key= APP_SECRET_KEY

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/save_photos', methods=['GET', 'POST'])
def save_photos():
    if request.method == 'POST':
        try:
            files = request.files.getlist("files")
            folder = UPLOADED_PHOTO_SAVING_FOLDER_KEY

            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)
            for file in files:
                file.save(os.path.join(folder,file.filename))
            
            output_file = Service().start_process()
            flash("File uploaded!!","success")
            flash("Files Converted Successfully!!","success")
            return send_file(output_file,as_attachment=True)

        except Exception as e:
            flash(f'Something went wrong: {e}', 'danger')
            return redirect(url_for('home'))
        
if __name__=="__main__":
    app.run()