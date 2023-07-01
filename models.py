from main import db

JapaneseFoodIngredient = db.Table('MealIngredient',
    db.Column('mid', db.Integer, db.ForeignKey('Meal.id')),
    db.Column('iid', db.Integer, db.ForeignKey('Ingredient.id'))
)


class Meal(db.Model):
  __tablename__ = "Meal"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  price = db.Column(db.Text())
  image_url = db.Column(db.Text())
  base = db.Column(db.Integer, db.ForeignKey('Base.id'))

  Ingredients = db.relationship('Ingredient', secondary=JapaneseFoodIngredient, backref='Meals')

  def __repr__(self):
    return f'{self.name.upper()} MEAL' 


class Ingredient(db.Model):
  __tablename__ = "Ingredient"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())

  def __repr__(self):
    return self.name