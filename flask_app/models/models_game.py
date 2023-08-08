from flask_app.config.mysqlconnection import connectToMySQL
import random

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
        # print("Saving the game method...")
        query = """INSERT INTO games (name, background_image, playtime, released, rating, esrb_rating, genre,
                platform, description, user_id)
                VALUES (%(name)s, %(background_image)s, %(playtime)s, %(released)s, %(rating)s, %(esrb_rating)s,
                %(genre)s, %(platform)s, %(description)s, %(user_id)s);"""
        # print(query)
        # print("Saving game method was successful...")
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_users_collected_games(cls, data):
        query = """SELECT * FROM games WHERE user_id = %(user_id)s"""
        results = connectToMySQL(db).query_db(query, data)
        collected_games = []
        # count = 0
        for game in results:
            # print(game)
            collected_games.append(cls(game))
            # count += 1
        # print(f"You have {count} collected games!")
        print(f'{len(collected_games)} collected games')
        return collected_games

    # Classmethod for deleting a game.
    @classmethod
    def destroy_game(cls, data):
        # print("Delete game method...")
        query = "DELETE FROM games WHERE id = %(id)s AND user_id = %(user_id)s;"
        # print("Game delete method was successful...")
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for displaying a random game fact
    @classmethod
    def random_game_facts(cls):
        facts = []
        gamecube = ["The Nintendo Gamecube came out September 14th, 2001."]
        facts.append(gamecube)
        kombat = ["Mortal Kombat made it's first appearance in 1992."]
        facts.append(kombat)
        skyrim = ["The dragon Paarthurnax in The Elder Scrolls V: Skyrim is voiced by the same man who voices Nintendo’s Mario."]
        facts.append(skyrim)
        gears = ["Gears of War 2 was featured in AMC’s The Walking Dead."]
        facts.append(gears)
        dead = ["Left 4 Dead 2 was so popular that an expansion was released 11 years after the original launch date."]
        facts.append(dead)
        rockstar = ["Rockstar Games hired real-life gang members to voice background characters in Grand Theft Auto V."]
        facts.append(rockstar)
        god = ["God of War (2018) plays out like a movie that’s been shot in one single take, with no cuts or loading screens."]
        facts.append(god)
        dk = ["Donkey Kong 64‘s DK Rap started as a joke between the game designers."]
        facts.append(dk)
        halo = ["In the first 24 hours of its release, more than a million people logged into Xbox Live to play Halo 3."]
        facts.append(halo)
        witcher = ["The author of The Witcher novels tried to sue the developers of The Witcher 3 for more royalty payments."]
        facts.append(witcher)
        first_event = ["The first gaming event in the US to be held at a national level was the Red Annihilation multiplayer Quake event in 1997."]
        facts.append(first_event)
        persia = ["Assassin’s Creed was initially meant to be a spin-off of Prince of Persia."]
        facts.append(persia)
        snoop = ["Snoop Dogg created an exclusive track for Need For Speed: Underground 2."]
        facts.append(snoop)
        dog_meat = ["Dogmeat, the canine companion in Fallout 3, was modeled off the dog in Mad Max 2."]
        facts.append(dog_meat)
        party = ["Nintendo’s American branch was forced to offer gloves to everyone who bought a copy of Mario Party."]
        facts.append(party)
        ultimate = ["At its release, Super Smash Bros. Ultimate was the largest crossover game in history."]
        facts.append(ultimate)
        pinkerton = ["The Pinkerton Detective Agency tried to sue Rockstar Games after the release of Red Dead Redemption 2."]
        facts.append(pinkerton)
        kart = ["The handbook for Super Mario Kart actually recommended players cheat and look at each other’s screens to get an advantage!"]
        facts.append(kart)
        hawk = ["Tony Hawk’s Pro Skater 2 was the first in the series to have a playable Marvel character."]
        facts.append(hawk)
        tomb = ["If you play Rise of the Tomb Raider on February 14, a special message pops up."]
        facts.append(tomb)
        conker = ["Conker’s Bad Fur Day was originally meant to be another boring PG-rated 3D platformer."]
        facts.append(conker)
        broke_vegas = ["The developers of Fallout: New Vegas missed out on a huge bonus from Bethesda because the game’s ratings were high enough."]
        facts.append(broke_vegas)
        tlou = ["The Last of Us began development as a reboot of Naughty Dog’s Jak and Daxter series."]
        facts.append(tlou)
        ocarina = ["The Legend of Zelda: Ocarina of Time has been the highest-ranking game since its release in 1998."]
        facts.append(ocarina)
        streaks = ["Call of Duty 4: Modern Warfare was the first Call of Duty to feature killstreaks."]
        facts.append(streaks)
        re = ['The woman who voices Resident Evil 4‘s Ashley Graham also did voice work for SpongeBob SquarePants.']
        facts.append(re)
        san_andreas = ["Grand Theft Auto: San Andreas is the best-selling PlayStation 2 game of all time."]
        facts.append(san_andreas)
        return random.choice(facts)