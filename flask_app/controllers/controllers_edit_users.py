from flask_app import app
from flask import render_template, redirect, session
from flask_app.models import models_user

# Get Route
# Route for rendering the "Edit User" page.
@app.get('/edit_user')
def render_edit_user_page():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    edit = models_user.User.get_user_by_id(data)
    return render_template('edit_user.html', edit=edit)