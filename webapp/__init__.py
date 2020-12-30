import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# # from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_bootstrap import Bootstrap



# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
# app.config['SECRET_KEY']= 'sdkhjfbgvasd21345adqad'
bootstrap = Bootstrap(app)


# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)


# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

from webapp.Seller import routes
