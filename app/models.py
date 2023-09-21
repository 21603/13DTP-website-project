from app.routes import db

# represent the many-to-many relationship between Meal and Ingredient
MealIngredient = db.Table(
    'MealIngredient',
    db.Column('mid', db.Integer, db.ForeignKey('Meal.id')),
    db.Column('iid', db.Integer, db.ForeignKey('Ingredient.id'))
)


class Base(db.Model):
    __tablename__ = "Base"

    # Columns for the Base table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.Text())
    image_url = db.Column(db.Text())

    # Establishing a relationship with the Meal table (one-to-many)
    meals = db.relationship('Meal', backref='base', lazy=True)

    def __repr__(self):
        return self.name


class Meal(db.Model):
    __tablename__ = "Meal"

    # Columns for the Meal table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.Text())
    price = db.Column(db.Text())
    image_url = db.Column(db.Text())

    # Foreign key relationship to the Base table
    base_id = db.Column(db.Integer, db.ForeignKey('Base.id'))

    # Establishing a relationship with the Ingredient table through the
    # MealIngredient association table (many-to-many)
    ingredients = db.relationship(
        'Ingredient',
        secondary=MealIngredient,
        backref='meals'
    )

    def __repr__(self):
        return f'{self.name.upper()} MEAL'


class Ingredient(db.Model):
    __tablename__ = "Ingredient"

    # Columns for the Ingredient table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return self.name
