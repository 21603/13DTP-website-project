import sys
import os

# Add parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "Japanese food.db")
db.init_app(app)

import app.models as models

# basic route
@app.route('/')
def root():
    return render_template('home.html', page_title='HOME')

# about route
@app.route('/about')
def about():
    return render_template('about.html', page_title='ABOUT')

# Page to display all Japanese food and link to each individual one
@app.route('/all_Japanese_food')
def all_Japanese_food():
    Japanese_food = models.Meal.query.all()
    return render_template("all_Japanese_food.html", Japanese_food=Japanese_food)

# Display the details of one Japanese food including its toppings
@app.route('/Japanese_food/<int:id>')
def Japanese_food(id):
    # Get the Japanese food, but throw a 404 if the id doesn't exist
    Japanese_food = models.Meal.query.filter_by(id=id).first_or_404()
    print(Japanese_food, Japanese_food.base)  # DEBUG
    return render_template('Japanese_food.html', Japanese_food=Japanese_food)

@app.route('/base/<int:id>')
def base(id):
    Japanese_food = models.Meal.query.filter_by(base_id=id).all()
    return render_template("base.html", Japanese_food=Japanese_food)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)