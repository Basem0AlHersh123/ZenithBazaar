from Market import db, loginManager
from Market import bcrypt, app
from flask_login import UserMixin
loginManager.init_app(app)
loginManager.login_view ='login'# name of the function you want to direct the user to 
@loginManager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))
class User(db.Model,UserMixin):
    __tablename__='User'
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    email=db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash=db.Column(db.String(length=60),nullable=False)
    budget=db.Column(db.Integer(),nullable=False,default=1000)
    item=db.relationship('Item',backref='owned_user',lazy=True)
    @property
    def prettier_bugdet(self):
        final_pattern=[]
        while self.budget>0:
            for _ in range(3):
                final_pattern.insert(0,str(self.budget%10))
                self.budget//=10
                if self.budget==0:
                    return "".join(final_pattern)
            final_pattern.insert(0,",")
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self,plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(pw_hash=self.password_hash,password= attempted_password)
    def can_purchase(self, item):
        return self.budget>=item.price
    def can_sell(self, item):
        return item in self.item
class Item(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner=db.Column(db.Integer(),db.ForeignKey('User.id'))
    def __repr__(self):
        return f'Item {self.name}'
    def buy(self,user):
        self.owner=user.id
        user.budget -= self.price
        db.session.commit()
    def sell(self,user):
        self.owner = None
        user.budget += self.price
        db.session.commit()