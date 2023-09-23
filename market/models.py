from market import db

# MODELS FOR DATABASE
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)

    # Define how Item will be showed in Terminal item.query.all()
    def __repr__(self):
        return f'Item {self.name}'