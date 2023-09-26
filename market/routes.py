from flask import render_template, redirect, url_for
from market import app, db
from market.models import Item, User
from market.forms import RegisterForm

# ROUTES TO PAGES
@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email_address.data,
            password_hash=form.password1.data            
        )
        # Need form.hidden_tag() in html register page to do this
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}: #If there are exist any errors
        for err_msg in form.errors.values():
            print(f'There was an error in creating an user: {err_msg}')

    return render_template('register.html', form=form)