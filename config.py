import os

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ["MICROBLOG_WTF_SECRET_KEY"]

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# database settings
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ["MICROBLOG_EMAIL_USERNAME"]
MAIL_PASSWORD = os.environ["MICROBLOG_EMAIL_PASSWORD"]

# administrator list
ADMINS = ['besermenji.vladimir@gmail.com']
