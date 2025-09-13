from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
bcrypt=Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config['SECRET_KEY']='84b5b43b51f8392da2c57356'
db=SQLAlchemy(app)
loginManager=LoginManager(app)
loginManager.login_message_category="info"
loginManager.login_view="login"
@app.cli.command("init-db")
def init_db():
    db.create_all()

from Market import routes,models,form