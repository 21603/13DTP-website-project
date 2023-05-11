#https://flask.palletsprojects.com/en/2.3.x/quickstart/


#imports
import sqlite3
from flask import Flask,g,render_template



#initialization
app = Flask(__name__)

DATABASE = 'Japanese food.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#routes
@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM Base"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)





# run the app
if __name__ == "__main__":
    app.run(debug=True)



