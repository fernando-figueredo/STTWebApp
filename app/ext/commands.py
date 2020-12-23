import click
from app.ext.database import db
from app.tables import User


def create_db():
    """Creates sqlite database"""
    db.create_all()

def populate_db():
    """populate db with simple data"""
    i=User("luiz.flf","1234","Fernando Luiz de Figueredo","Estagiário", False)
    db.session.add(i)
    db.session.commit()
    return User.query.all()

def drop_db():
    """Cleans sqlite database"""
    db.drop_all()

def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    @click.option('--name', '-n')
    @click.option('--cargo', '-c')
    @click.option('--missao', '-m')
    def addUser_db(username,password,name,cargo,missao):
        """Adds a new user to the database"""
        if missao == '1':
            m = True
        else:
            m = False

        i=User(username,password,name,cargo,m)
        db.session.add(i)
        db.session.commit()
        return User.query.all()
