from flask_app import app
from flask_app.controllers import controllers_users, controllers_games, controllers_collection_summaries
from flask_app.controllers import controllers_consoles, controllers_peripherals, controllers_print_medias




if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)