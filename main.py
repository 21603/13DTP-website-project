from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)


# can't do this import until we have 'app' in place
# sometimes can use from models import pizzas but not with M2M
# Linters will scream about this - there are codes to stop that
import models


# basic route
@app.route('/')
def root():
  return render_template('home.html', page_title='HOME')


# about route
@app.route('/about')  # note the leading slash, it’s important
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
  Japanese_food = models.JapaneseFood.query.filter_by(id=id).first_or_404()
  return render_template('Japanese_food.html', Japanese_food=Japanese_food)


@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html")


if __name__ == "__main__":
  app.run(debug=True)