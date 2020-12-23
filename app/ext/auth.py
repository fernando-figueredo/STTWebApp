from flask_login import LoginManager


lm=LoginManager()

def init_app(app):
    lm.init_app(app)
