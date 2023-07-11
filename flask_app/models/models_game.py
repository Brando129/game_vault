from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash

# Database name
db = "retro_vault_schema"

# Class name
class Game:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        self.genere = data['genere']
        self.console = data['console']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new game.
    @classmethod
    def save_game(cls, data):
        print("Saving the game method...")
        query = """INSERT INTO games (title, release_date, genere, console, description)
                VALUES (%(title)s, %(release_date)s, %(genere)s, %(console)s, %(description)s);"""
        print("Saving game method was successful...")
        return connectToMySQL(db).query_db(query, data)
