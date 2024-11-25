from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///add.db'  # виправлено назву і пробіл
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Pizza {self.name}>'


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/addpizza')
def add_pizza():
    return render_template('addpizza.html')


@app.route('/aboutUs')
def aboutUs():
    return render_template('about.html')


@app.route('/check')
def check():
    return render_template('orderplaced.html')


@app.route('/added')
def added():
    return render_template('added.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/menu")
def pizza_menu():
    menu_items = [
        {"name": "Мишачий Класик", "description": "Сир, томати, базилік", "price": 150},
        {"name": "Пепероні від Тома", "description": "пепероні, шинка, ковбаски, соус барбекю", "price": 180},
        {"name": "Джеррі в Сирі", "description": "Моцарела, горгонзола, пармезан, чеддер", "price": 200},
        {"name": "Сирний Джеррі", "description": "моцарела, чеддер, пармезан, рікотта, любов", "price": 250},
        {"name": "Томовий Барбекю", "description": "курка, бекон, соус барбекю, червоний лук", "price": 300},
    ]

    return render_template("menu.html", menu_items=menu_items)


@app.errorhandler(404)
def page_not_found(error):
    return "Упс, такої сторінки немає", 404


if __name__ == "__main__":
    app.run(debug=True)
