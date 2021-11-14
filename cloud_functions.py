from ImageManager import ImageManager
import urllib
from PIL import Image
from io import BytesIO
import requests
import numpy
ALLOWED_EXTENSIONS = {'tif', 'png', 'jpg', 'jpeg', 'gif'}
ImageManager = ImageManager()
bucket = ImageManager.bucket()
dbc = ImageManager.db()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_images(uploaded_file):
    if uploaded_file and allowed_file(uploaded_file.filename):
        blob = bucket.blob(uploaded_file.filename)
        blob.upload_from_string(
            uploaded_file.read(),
            content_type=uploaded_file.content_type
        )
        blob.make_public()
        prediction = predict(blob.public_url, uploaded_file.filename)
        uploaded_data(uploaded_file.filename)
        return prediction, blob.public_url

def uploaded_data(data):
    '''
    Upload the images metadata from frontend to the google cloud firestore
    '''
    dbc.document(data).set({'id': '0'})


def predict(url, filename):

    try: 
        urllib.URLopener().retrieve(url, filename)
    except:
        urllib.request.urlretrieve(url, filename)

    image = Image.fromarray(numpy.uint8(Image.open(filename)))
    image2bytes = BytesIO()
    image.save(image2bytes, format="PNG")
    image2bytes.seek(0)
    image_as_bytes = image2bytes.read()

# Send the HTTP POST request to TorchServe

    req = requests.post("http://35.230.109.206:8080/predictions/smoke", data=image_as_bytes)
    if req.status_code == 200:
        res = req.json()
        res = pre(res)
        return res
    else:
        print("error")

def pre(value):
    if value == 0:
        return "Not Smoking"
    else:
        return "Smoking"