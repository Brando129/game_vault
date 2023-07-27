from flask_app import app
from flask import render_template, redirect, request, session

# Get Routes
# Route for rendering the "Collection Summary" page.
@app.get('/collection_summary')
def render_collection_summary():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('collection_summary.html')