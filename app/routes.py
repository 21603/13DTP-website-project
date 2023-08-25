from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "Japanese food.db")
db.init_app(app)

import app.models as models

# ... Your existing routes and view functions ...

def update_image_urls():
    # Get all the bases from the database
    bases = models.Base.query.all()
    
    # Update the image URLs for each base
    for base in bases:
        base.image_url = "new_image_url"  # Update this with the actual new image URL
    
    # Commit the changes to the database
    db.session.commit()


@app.route('/')
def root():
    # Run the update_image_urls() function before retrieving the bases
    update_image_urls()
    
    bases = models.Base.query.all()  # Retrieve all bases from the database
    return render_template('home.html', page_title='HOME', bases=bases)

#about route
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
    # Get the Japanese food, but throw a 404 error if the id doesn't exist
    Japanese_food = models.Meal.query.get(id)
    if not Japanese_food:
        abort(404)  # Return a 404 error if the meal with the given id doesn't exist

    return render_template('Japanese_food.html', Japanese_food=Japanese_food)

# Route to display meals of a specific base
@app.route('/base/<int:base_id>')
def base(base_id):
    base = models.Base.query.get(base_id)
    if not base:
        abort(404)  # Return a 404 error if the base with the given id doesn't exist

    meals_of_base = base.meals  # Accessing meals associated with the base

    return render_template("base.html", base=base, meals_of_base=meals_of_base)

@app.route('/base/1')
def rice_base():
    rice_base = models.Base.query.get(1)
    return render_template('base.html', base=rice_base)

@app.route('/base/2')
def noodle_base():
    noodle_base = models.Base.query.get(2)
    return render_template('base.html', base=noodle_base)

@app.route('/base/3')
def deep_fried_food_base():
    deep_fried_food_base = models.Base.query.get(3)
    return render_template('base.html', base=deep_fried_food_base)

@app.route('/base/4')
def seafood_base():
    seafood_base = models.Base.query.get(4)
    return render_template('base.html', base=seafood_base)

@app.route('/base/5')
def wagashi_base():
    wagashi_base = models.Base.query.get(5)
    return render_template('base.html', base=wagashi_base)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)
