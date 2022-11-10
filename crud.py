from models import User, Products, db


def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()


def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()


def get_all_users()->db.Query:
    return User.query.all()
def add_product(product:Products)->None:
    db.session.add(product)
    db.session.commit()