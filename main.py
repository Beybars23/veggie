from flaskapp import *
from flask import render_template
from flask import request, session, redirect, url_for
from werkzeug.utils import secure_filename
from models import User, db , Products
import crud


@app.route("/")
# @app.route("/<context>")
def home(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("home.html", context=None)


@app.route("/cart")
# @app.route("/<context>")
def cart(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("cart.html", context=None)


@app.route("/shop")
# @app.route("/<context>")
def shop(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("shop.html", context=None)


@app.route("/shop_detail")
# @app.route("/<context>")
def shop_detail(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("shop-detail.html", context=None)


@app.route("/checkout")
# @app.route("/<context>")
def checkout(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("checkout.html", context=None)


@app.route("/my_account")
# @app.route("/<context>")
def my_account(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("my-account.html", context=None)


@app.route("/wishlist")
# @app.route("/<context>")
def wishlist(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("wishlist.html", context=None)

@app.route("/contact_us")
# @app.route("/<context>")
def contact_us(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("contact-us.html", context=None)


@app.route("/about")
# @app.route("/<context>")
def about(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("about.html", context=None)


@app.route('/register', methods=["GET", "POST"])
def register(context=None):
    if request.method == "POST":
        login = request.form['email']
        fname = request.form['fname']
        sname = request.form['sname']
        pass1 = request.form['password']
        pass2 = request.form['password_conf']

        data = db.session.query(User).filter_by(login=request.form['email']).first()

        if data:
            return redirect(url_for("register", error="Already registered!"))
        elif pass1 != pass2:
            return redirect(url_for("register", error="Passwords do not match!"))
        else:
            crud.add_user(User(login=login,
                               user_fname=fname,
                               user_sname=sname,
                               password=pass1))

            return redirect(url_for("login", context="Successfully registered!"))
    return render_template("register.html", context=context)


@app.route("/login", methods=["GET", "POST"])
def login(context=None):
    if request.method == "POST":
        user = db.session.query(User).filter_by(login=request.form['email'],
                                                password=request.form['password']).first()
        if user :
            session['email'] = "admin@gmail.com"
            return redirect(url_for("admin"))
        elif user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['email'] = user.login
            return redirect(url_for("user_page", user_id=user.user_id))
        else:
            return render_template("login.html", context="Wrong credentials")

    return render_template("login.html", context=context)

@app.route("/admin_page")
# @app.route("/<context>")
def admin(context=None):
    data = {"Data": "Some data here to be sent as dict (JSON)"}
    return render_template("admin.html", context=None)



@app.route('/add_product', methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form['price']
        description = request.form['description']
        available = request.form['available']
        item = request.form['item']
        code = request.form['code']
        file = request.files['picture']
        data = db.session.query(Products).filter_by(name=request.form['name']).first()

        if data:
            return redirect(url_for("add_product", error="Already exists!"))
        else:
           crud.add_user(User(pName=name,
                           price=price,
                           description=description,
                           available=available,
                           item=item,
                           pCode=code,
                           picture=file
                           ))
           return redirect(url_for("admin"))
    return render_template("add-product.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)