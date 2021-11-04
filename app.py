import os
from flask import Flask, render_template, request, redirect, send_file, flash
from s3_functions import upload_file, show_image
from werkzeug.utils import secure_filename
#from flask_mobility import Mobility

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
BUCKET = "smokeclassify"
ALLOWED_EXTENSIONS = { 'tif' 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']

        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_file(f"uploads/{f.filename}", BUCKET)
            return redirect("/")


@app.route("/pics")
def list():
    contents = show_image(BUCKET)
    return render_template('collection.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
