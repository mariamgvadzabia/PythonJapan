from flask import render_template, redirect, url_for
from forms import RegisterFrom
from models import User
from ext import app, db, client
from forms import ProductForm
from models import Product
from flask import render_template, redirect, url_for
from forms import RegisterFrom, ProductForm, LoginForm, AskForm
from flask_login import login_user, logout_user, login_required, current_user
import os

profiles = []


@app.route("/")
def main():
    return render_template("main.html", role="admin")

@app.route("/explore")
def explore():
    products = Product.query.all()
    tokyo_item = None
    for product in products:
        if product.name == "Tokyo":
            tokyo_item = product
            break

    if tokyo_item:
        products.remove(tokyo_item)
        products.insert(0, tokyo_item)
    return render_template("explore.html",  products=products, role="admin")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/seemore")
def seemore():
    return render_template("seemore.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterFrom()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            birthday=str(form.birthday.data)
        )
        db.session.add(new_user)
        db.session.commit()
    return render_template("register.html", form=form)

@app.route("/create", methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            category=form.category.data,
            subtitle = form.subtitle.data
        )
        image= form.img.data
        img_location = os.path.join(app.root_path, "static", "images", image.filename)
        image.save(img_location)
        new_product.img=image.filename

        db.session.add(new_product)
        db.session.commit()
        return redirect("/explore")
    print(form.errors)
    return render_template("create.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('explore'))



@app.route('/ask', methods=['GET', 'POST'])
def ai_page():
    form = AskForm()
    answer = None

    if form.validate_on_submit():
        question = form.question.data

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                    "role": "user",
                    "content": question,
                    }
                ],

                model="llama-3.3-70b-versatile",

            )
            answer = chat_completion.choices[0].message.content

        except Exception as e:
            answer = f"შეცდომა: {str(e)}"

    return render_template('ask_ai.html', form=form, answer=answer)