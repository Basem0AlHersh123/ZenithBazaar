from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
db=SQLAlchemy(app)
@app.route("/market")
def market():
    Items=item.query.all()
    return render_template("market_page.html",Items=Items)

class item(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(50),nullable=False, unique=True)
    price=db.Column(db.Integer,nullable=False, unique=True)
    barcode=db.Column(db.String(12),nullable=False, unique=True)
    description=db.Column(db.String(1024),nullable=False, unique=True)
@app.route("/")
def home():
    return render_template("market_page.html")
    
if __name__=="__main__":
    app.run(debug=True,port=5000)