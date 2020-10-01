from extensions import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    comments = db.Column(db.Text())

    def __init__(self, username, email, comments):
        self.username = username
        self.email = email
        self.comments = comments
