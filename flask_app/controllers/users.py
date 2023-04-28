from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.post import Post 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hub_login")
def hub_login():
    return render_template('login.html') 

@app.route("/hub_register")
def hub_register():
    return render_template('register.html') 

@app.route("/register", methods=["POST"]) 
def register():
    if not User.validate_register(request.form):
        return redirect("/hub_register")
    
    data = { 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']) 
    }

    id = User.save(data) 

    session['user_id'] = id 

    return redirect("/home")

@app.route("/login", methods=["POST"])
def login(): 
    user = User.get_by_email(request.form)

    if not user: 
        flash("Invalid Email", "login")
        return redirect("/hub_login")
    if not bcrypt.check_password_hash(user.password, request.form['password']): 
        flash("Invalid Password", "login")
        return redirect("/hub_login")
    session["user_id"] = user.id 
    return redirect("/home")

@app.route("/home")
def home(): 
    if 'user_id' not in session: 
        return redirect("/logout")
    data = { 
        "id": session['user_id']
    }
    return render_template('home.html', user=User.get_by_id(data), posts=Post.get_all())

@app.route("/gallery")
def gallery(): 
    if 'user_id' not in session: 
        return redirect("/logout")
    data = { 
        "id": session['user_id']
    }
    return render_template('gallery.html')

@app.route("/support")
def support():
    session.clear()
    return redirect("/") 

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/") 