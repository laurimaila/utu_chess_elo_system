import player
import game
import json

# Methods for saving and loading the json data

def save_players(players, filename = "players_database.json"):
	"""
	Method for saving players list to database.
	
    Parameters
    ----------
	players : list of Player instances
	"""
	# Make a list of Player dictionaries
	playerstable = [vars(p) for p in players]
	json_format = json.dumps(playerstable, indent = 4)
	with open(filename, "w") as db:
		db.write(json_format)

# Update games database
# Read old json, extend list to new data and dump all to json
def save_new_games(new_games, filename = "games_database.json"):
	"""
	Method for saving NEW games to games database.
	
    Parameters
    ----------
    first_games : list of Game instances
	"""
	# Read old json
	with open(filename, "r") as db:
		old_json = db.read()
	game_dictionaries = json.loads(old_json)

	# List of new game dictionaries to new json data
	newgamestable = [vars(g) for g in new_games]
	# Extend old data to new games
	game_dictionaries.extend(newgamestable)
	updated_json  = json.dumps(game_dictionaries, indent = 4)

	# Write the updated json
	with open(filename, "w") as db:
		db.write(updated_json)

def load_players():
	"""
	Method for loading whole players list from database.
	
    Returns
	-------
	players : list of Player instances
	"""
	with open("players_database.json", "r") as db:
		json_format = db.read()
	player_dictionaries = json.loads(json_format)
	players = []
	for j in player_dictionaries:
		players.append(player.Player(**j))
	return players

def load_games(filename = "games_database.json"):
	"""
	Method for loading whole games list from database.
	
    Returns
	-------
	games : list of Game instances
	"""
	with open(filename, "r") as db:
		json_format = db.read()
	game_dictionaries = json.loads(json_format)
	games = []
	for j in game_dictionaries:
		games.append(game.Game(**j))
	return games