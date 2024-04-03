
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

with open("config.json", "r") as f:
    params = json.load(f)["params"]





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]

db = SQLAlchemy(app)



class Posts(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), primary_key=False)
    slug = db.Column(db.String(50), primary_key=False)
    author = db.Column(db.String(50), primary_key=False)
    date = db.Column(db.String(50), primary_key=False)
    readtime = db.Column(db.Integer, primary_key=False)
    content = db.Column(db.String(3000), primary_key=False)
    image = db.Column(db.String(50), primary_key=False)




@app.route('/')
def home():
    posts  = Posts.query.filter_by().all()
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")


@app.route('/blogpost/<string:slug>', methods=["GET"])
def blogpost(slug):
    posts = Posts.query.filter_by().all()
    posts = posts[0:3]
    post = Posts.query.filter_by(slug=slug).first()
    return render_template("blogpost.html", post=post, posts=posts)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    
    return render_template('search.html', query=query)






app.run(debug=True)
