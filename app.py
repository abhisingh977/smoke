from flask import Flask, render_template, request, redirect
from cloud_functions import upload_images
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return 'No file uploaded.', 400
        upload_images(uploaded_file)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=80)
