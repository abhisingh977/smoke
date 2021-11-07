from ImageManager import ImageManager

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
        uploaded_data(uploaded_file.filename)


def uploaded_data(data):
    '''
    Upload the images metadata from frontend to the google cloud firestore
    '''
    dbc.document(data).set({'id': '0'})
