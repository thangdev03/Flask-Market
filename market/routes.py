from flask import render_template
from market import app
from market.models import Item

# ROUTES TO PAGES
@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

