from dynaconf import FlaskDynaconf


def init_app(app):
    FlaskDynaconf(app)
