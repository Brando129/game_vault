from flask_app import app
from flask import render_template, redirect, session

# Route for rendering the "peripherals" page.
@app.route('/peripherals')
def render_peripherals_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('peripherals.html')