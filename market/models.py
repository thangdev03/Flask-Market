from market import db

# MODELS FOR DATABASE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True) 
    
    def __repr__(self):
        return f'User {self.username}'
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Define how Item will be showed in Terminal item.query.all()
    def __repr__(self):
        return f'Item {self.name}'