from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.post import Post 
from flask_app.models.user import User

@app.route('/new/post')
def new_post():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id": session["user_id"]
    }
    return render_template('post.html', user=User.get_by_id(data))

@app.route('/create/post',methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "employer": request.form["employer"],
        "program_type": request.form["program_type"],
        "start_date": request.form["start_date"],
        "comment": request.form["comment"], 
        "user_id": session["user_id"]
    }
    Post.save(data)
    return redirect('/home')

@app.route('/edit/post/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html",edit=Post.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/post',methods=['POST'])
def update_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "employer": request.form["employer"],
        "program_type": request.form["program_type"],
        "start_date": request.form["start_date"],
        "comment": request.form["comment"], 
        "user_id": session["user_id"]
    }
    Post.update(data)
    return redirect('/home')

@app.route('/destroy/post/<int:id>')
def destroy_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Post.destroy(data)
    return redirect('/home')