from flaskapp import app, db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)  # integer primary key will be autoincremented by default
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_sname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_fname!r})"


class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)  # integer primary key will be autoincremented by default
    pName = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(100), nullable=False)
    pCode = db.Column(db.String(20), nullable=False)
    picture = db.Column(db.String(100), nullable=False)
