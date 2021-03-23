from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(800))
    rooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(30))
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

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support 