from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(800))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Numeric(9,2))
    ptype = db.Column(db.String(30))
    location = db.Column(db.String(100))
    photo = db.Column(db.String(255))


    def __init__(self, title, description, rooms, bathrooms, price, ptype, location, photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.ptype = ptype
        self.location = location
        self.photo = photo
