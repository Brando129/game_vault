from flask_app.config.mysqlconnection import connectToMySQL


# Database name
db = "game_vault_schema"

# Class name
class Game:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.background_image = data['background_image']
        self.playtime = data['playtime']
        self.released = data['released']
        self.rating = data['rating']
        self.esrb_rating = data['esrb_rating']
        self.genre = data['genre']
        self.platform = data['platform']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # Classmethod for saving a new game.
    @classmethod
    def save_game(cls, data):
        print("Saving the game method...")
        query = """INSERT INTO games (name, background_image, playtime, released, rating, esrb_rating, genre,
                platform, description, user_id)
                VALUES (%(name)s, %(background_image)s, %(playtime)s, %(released)s, %(rating)s, %(esrb_rating)s,
                %(genre)s, %(platform)s, %(description)s, %(user_id)s);"""
        print(query)
        print("Saving game method was successful...")
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the games.
    @classmethod
    def get_all_games(cls):
        print("Getting all the games method...")
        query = "SELECT * FROM games;"
        results = connectToMySQL(db).query_db(query)
        collected_games = []
        for row in results:
            collected_games.append(cls(row))
        print("Getting all the games method was successful...")
        return collected_games

    # Classmethod for getting games by a user_id.
    @classmethod
    def get_games_by_user_id(cls, data):
        print("Getting the game by id method...")
        query = "SELECT * FROM games WHERE user_id = %(user_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print("Getting game by id method was successful...")
        return cls(results[0])


    # Classmethod for deleting a game.
    @classmethod
    def destroy_game(cls, data):
        print("Delete game method...")
        query = "DELETE FROM games WHERE id = %(id)s AND user_id = %(user_id)s;"
        print("Game delete method was successful...")
        return connectToMySQL(db).query_db(query, data)



