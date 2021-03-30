from twit_app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    followers = db.Column(db.Integer)
    children = db.relationship("tweet", backref="user")

    def __repr__(self):
        return f"User {self.id}"
