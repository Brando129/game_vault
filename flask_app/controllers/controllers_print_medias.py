from flask_app import app
from flask import render_template, redirect, session

# Route for rendering the "print media" page.
@app.route('/print/media')
def render_print_media_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('print_media.html')