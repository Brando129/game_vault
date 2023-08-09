from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import models_user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Get Route
# Route for rendering the "Edit User" page.
@app.get('/edit_user')
def render_edit_user_page():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        'id':session['user_id']
    }
    user = models_user.User.get_user_by_id(user_data)
    return render_template('edit_user.html', user=user)

# Post Route
@app.post('/update/user')
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_user.User.validate_edit_user(request.form):
        return redirect('/edit_user')
    data = {
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        # 'confirm_password': bcrypt.check_password_hash(request.form['password'], request.form['password']),
        'id': request.form['id']
    }
    models_user.User.update_user(data)
    return redirect('/homepage')