from . import db

class dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ownerFullName = db.Column(db.Text, nullable=False)
    ownerAdress = db.Column(db.Text, nullable=False)
    ownerMobileNumber = db.Column(db.String(20), nullable=False)
    ownerMobileEmail = db.Column(db.String(120), nullable=False)
    dogName = db.Column(db.Text, nullable=False)
    dogAge = db.Column(db.Integer, nullable=False)
    dogColor = db.Column(db.Text, nullable=False)
    dogSize = db.Column(db.Text, nullable=False)
    dogWeight = db.Column(db.Float, nullable=False)
    dogTemper = db.Column(db.Text, nullable=False)

    def repr(self):
        return f"<dog {self.username}>"