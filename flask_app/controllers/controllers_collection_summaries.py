from flask_app import app
from flask import render_template, redirect, session

# Route for rendering the "collection summary" page.
@app.route('/collection_summary')
def render_collection_summary_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('collection_summary.html')