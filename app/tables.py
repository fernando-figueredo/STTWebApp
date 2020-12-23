from app.ext.auth import lm
from app.ext.database import db


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    cargo = db.Column(db.String)
    missao = db.Column(db.Boolean)

    # Metodos do Flask Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, cargo, missao):
        self.username = username
        self.password = password
        self.name = name
        self.cargo = cargo
        self.missao = missao

    def __repr__(self):
        return "<Usuário %r>" % self.password


class AccessLevel(db.Model):
    __tablename__ = "AccessLevel"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), unique=True)
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, level, user_id):
        self.level = level
        self.user_id = user_id

    def __repr__(self):
        return "<Nível de Acesso %r>" % self.level
