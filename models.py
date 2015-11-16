import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pokemon@localhost/pokemasters'
db = SQLAlchemy(app)

class Move(db.Model):
	__tablename__ = 'ALL_MOVES'
	MOVE_ID = db.Column(db.Integer, primary_key=True)
	MOVE_NAME = db.Column(db.VARCHAR(50))
	MOVE_TYPE = db.Column(db.VARCHAR(50))
	MOVE_CATEGORY = db.Column(db.VARCHAR(50))
	MOVE_POWER = db.Column(db.Integer)
	MOVE_ACCURACY = db.Column(db.Integer)
	MOVE_PP = db.Column(db.Integer)
	MOVE_DESCRIPTION = db.Column(db.BLOB)
	
	def __init__(self, name, type, category, power, accuracy, pp, description):
		self.MOVE_NAME = name
		self.MOVE_TYPE = type
		self.MOVE_CATEGORY = category
		self.MOVE_POWER = power
		self.MOVE_ACCURACY = accuracy
		self.MOVE_PP = pp
		self.MOVE_DESCRIPTION = description
		
	@property
	def serialize(self):
		return {
            'name' : self.MOVE_NAME,
            'type' : self.MOVE_TYPE,
            'category' : self.MOVE_CATEGORY,
            'power' : self.MOVE_POWER,
            'accuracy' : self.MOVE_ACCURACY,
            'pp' : self.MOVE_PP,
            'description' : self.MOVE_DESCRIPTION}
		
	@staticmethod
	def get_all():
		return Move.query.all()
		
	@staticmethod
	def get(move):
		return Move.query.filter_by(MOVE_NAME=move).first()

	@staticmethod
	def get_id(id):
		return Move.query.filter_by(MOVE_ID=id).first()
		

	
class Pokemon(db.Model):
	__tablename__ = "ALL_POKEMON"
	POKEMON_ID = db.Column(db.Integer, primary_key=True)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_HP = db.Column(db.Integer)
	POKEMON_ATK = db.Column(db.Integer)
	POKEMON_DEF = db.Column(db.Integer)
	POKEMON_SPATK = db.Column(db.Integer)
	POKEMON_SPDEF = db.Column(db.Integer)
	POKEMON_SPD = db.Column(db.Integer)
	POKEMON_HEIGHT = db.Column(db.Integer)
	POKEMON_WEIGHT = db.Column(db.Integer)
	POKEMON_IMG = db.Column(db.VARCHAR(256))
	
	
	def __init__(self, name, hp, attack, defense, spAttack, spDefense, speed, height, weight, img):
		self.POKEMON_NAME = name
		self.POKEMON_HP = hp
		self.POKEMON_ATK = attack
		self.POKEMON_DEF = defense
		self.POKEMON_SPATK = spAttack
		self.POKEMON_SPDEF = spDefense
		self.POKEMON_SPD = speed
		self.POKEMON_HEIGHT = height
		self.POKEMON_WEIGHT = weight
		self.POKEMON_IMG = img
		
	def __repr__(self):
		return '<name {}>'.format(self.name)
	
	@property
	def serialize(self):
		dtest = {
			'name' : self.POKEMON_NAME,
			'hp' : self.POKEMON_HP, 
			'atk' : self.POKEMON_ATK, 
			'def' : self.POKEMON_DEF, 
			'spa' : self.POKEMON_SPATK, 
			'spd' : self.POKEMON_SPDEF, 
			'spe' : self.POKEMON_SPD,
			'moves' : test()}
		print(dtest)
		return dtest
	
	def test(self):
		return {{'name' : 'Tackle', 'learn_type' : 'level' }}
	
	@staticmethod
	def get_all():
		return Pokemon.query.all()
		
	@staticmethod
	def get(name):
		return Pokemon.query.filter_by(POKEMON_NAME=name).first()

	@staticmethod
	def get_id(id):
		return Pokemon.query.filter_by(POKEMON_ID=id).first()


class Routes(db.Model):
	__tablename__ = "ALL_ROUTES"
	ID = db.Column(db.Integer, primary_key=True)
	ROUTE_NAME = db.Column(db.VARCHAR(50))
	ROUTE_REGION = db.Column(db.VARCHAR(50))
	ROUTE_NORTH_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_SOUTH_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_EAST_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_WEST_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_ACCESS_TO = db.Column(db.VARCHAR(50))
	ROUTE_MINI_DESCRIPTION = db.Column(db.VARCHAR(50))
	ROUTE_MAIN_DESCRIPTION = db.Column(db.TEXT)
	ROUTE_TRIVIA = db.Column(db.TEXT)

	def __init__(self, name, region, nExit, sExit, eExit, wExit, access, mini, main, trivia):
		self.ROUTE_NAME = name;
		self.ROUTE_REGION = region;
		self.ROUTE_NORTH_EXIT = nExit;
		self.ROUTE_SOUTH_EXIT = sExit;
		self.ROUTE_EAST_EXIT = eExit;
		self.ROUTE_WEST_EXIT = wExit;
		self.ROUTE_ACCESS_TO = access;
		self.ROUTE_MINI_DESCRIPTION = mini;
		self.ROUTE_MAIN_DESCRIPTION = main;
		self.ROUTE_TRIVIA = trivia;

	@staticmethod
	def get_all():
		return Routes.query.all()
		
	@staticmethod
	def get(name):
		return Routes.query.join(RouteImgs).filter_by(ROUTE_NAME=name).first()

	@staticmethod
	def get_id(id):
		return Routes.query.filter_by(ID=id).first()

class Trainers(db.Model):
	__tablename__ = "ALL_TRAINERS"

	ID = db.Column(db.Integer, primary_key=True)
	TRAINER_NAME = db.Column(db.VARCHAR(50))
	TRAINER_GEN = db.Column(db.VARCHAR(50))
	TRAINER_ROUTE_NAME = db.Column(db.VARCHAR(50))
	TRAINER_POKEMON = db.Column(db.VARCHAR(50))
	TRAINER_LEVEL = db.Column(db.VARCHAR(50))

	def __init__(self, name, gen, route, pokemon, level):
		self.TRAINER_NAME = name
		self.TRAINER_GEN = gen
		self.TRAINER_ROUTE = route
		self.TRAINER_POKEMON = pokemon
		self.TRAINER_LEVEL = level

class Abilities(db.Model):
	__tablename__ = "POKEMON_ABILITIES"

	ID = db.Column(db.Integer, primary_key=True)
	POKEMON_ID = db.Column(db.Integer)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_ABILITY = db.Column(db.VARCHAR(50))

	def __init__(self, id, name, ability):
		self.POKEMON_ID = id
		self.POKEMON_NAME = name
		self.POKEMON_ABILITY = ability

	@staticmethod
	def get_pokemon_abilities(name):
		return Abilities.query.filter_by(POKEMON_NAME=name)

class Evolutions(db.Model):
	__tablename__ = "POKEMON_EVOLUTIONS"

	ID = db.Column(db.Integer, primary_key=True)
	POKEMON_ID = db.Column(db.Integer)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_EVOLUTION = db.Column(db.VARCHAR(50))
	POKEMON_EVOLVE_METHOD = db.Column(db.VARCHAR(50))
	POKEMON_EVOLVE_LEVEL = db.Column(db.Integer)

	def __init__(self, id, name, evolution, method, level):
		self.POKEMON_ID = id
		self.POKEMON_NAME = name
		self.POKEMON_EVOLUTION = evolution
		self.POKEMON_EVOLVE_METHOD = method
		self.POKEMON_EVOLVE_LEVEL = level

	@staticmethod
	def get_pokemon_evo(name):
		return Evolutions.query.filter_by(POKEMON_NAME=name)

class Types(db.Model):
	__tablename__ = "POKEMON_TYPES"

	ID = db.Column(db.Integer, primary_key=True)
	POKEMON_ID = db.Column(db.Integer)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_TYPE = db.Column(db.VARCHAR(50))

	def __init__(self, id, name, type):
		self.POKEMON_ID = id
		self.POKEMON_NAME = name
		self.POKEMON_TYPE = type

	@staticmethod
	def get_pokemon_types(name):
		return Types.query.filter_by(POKEMON_NAME=name)

class Locations(db.Model):
	__tablename__ = "POKEMON_LOCATIONS"

	ID = db.Column(db.Integer, primary_key=True)
	POKEMON_ID = db.Column(db.Integer)
	POKMEON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_GAME = db.Column(db.VARCHAR(50))
	POKEMON_METHOD = db.Column(db.VARCHAR(50))

	def __init__(self, id, name, game, method):
		self.POKEMON_ID = id
		self.POKEMON_NAME = name
		self.POKEMON_GAME = game
		self.POKEMON_METHOD = method

class PokemonMoves(db.Model):
	__tablename__ = "POKEMON_MOVES"

	ID = db.Column(db.Integer, primary_key=True)
	POKEMON_ID = db.Column(db.Integer, db.ForeignKey("ALL_POKEMON.POKEMON_ID"))
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_MOVE = db.Column(db.VARCHAR(50))
	POKEMON_LEARN_TYPE = db.Column(db.VARCHAR(50))
	POKEMON_LEVEL_LEARNED = db.Column(db.Integer)

	def __init__(self, id, name, move, type, level):
		self.POKEMON_ID = id
		self.POKEMON_NAME = name
		self.POKEMON_MOVE = move
		self.POKEMON_LEARN_TYPE = type
		self.POKEMON_LEVEL_LEARNED = level

	@staticmethod
	def get_for_pokemon(poke_name):
		return PokemonMoves.query.filter_by(POKEMON_NAME=poke_name)

	@staticmethod
	def get_for_level(move_name):
		return Pokemon.query.join(PokemonMoves).filter_by(POKEMON_MOVE=move_name, POKEMON_LEARN_TYPE='level up')

	@staticmethod
	def get_for_machine(move_name):
		return Pokemon.query.join(PokemonMoves).filter_by(POKEMON_MOVE=move_name, POKEMON_LEARN_TYPE='machine')

	@staticmethod
	def get_for_egg(move_name):
		return Pokemon.query.join(PokemonMoves).filter_by(POKEMON_MOVE=move_name, POKEMON_LEARN_TYPE='egg move')

	@staticmethod
	def get_for_tutor(move_name):
		return Pokemon.query.join(PokemonMoves).filter_by(POKEMON_MOVE=move_name, POKEMON_LEARN_TYPE='tutor')

class RouteImages(db.Model):
	__tablename__ = "ROUTE_IMGS"

	ID = db.Column(db.Integer, primary_key=True)
	ROUTE_NAME = db.Column(db.VARCHAR(50))
	ROUTE_GEN = db.Column(db.VARCHAR(50))
	ROUTE_IMG = db.Column(db.VARCHAR(256))

	def __init__(self, name, gen, img):
		self.ROUTE_NAME = name
		self.ROUTE_GEN = gen
		self.ROUTE_IMG = img

	@staticmethod
	def get(name):
		return RouteImages.query.filter_by(ROUTE_NAME=name);

class RouteItems(db.Model):
	__tablename__ = "ROUTE_ITEMS"

	ID = db.Column(db.Integer, primary_key=True)
	ROUTE_NAME = db.Column(db.VARCHAR(50))
	ROUTE_ITEM_NAME = db.Column(db.VARCHAR(50))
	ROUTE_ITEM_IMG = db.Column(db.VARCHAR(50))
	ROUTE_ITEM_GAMES = db.Column(db.VARCHAR(256))
	ROUTE_ITEM_METHOD = db.Column(db.VARCHAR(256))

	def __init__(self, rName, iName, iImage, iGame, iMethod):
		self.ROUTE_NAME = rName
		self.ROUTE_ITEM_NAME = iName
		self.ROUTE_ITEM_IMG = iImage
		self.ROUTE_ITEM_GAMES = iGame
		self.ROUTE_ITEM_METHOD = iMethod

class RoutePokemon(db.Model):
	__tablename__ = "ROUTE_POKEMON"

	ID = db.Column(db.Integer, primary_key=True)
	ROUTE_NAME = db.Column(db.VARCHAR(50))
	ROUTE_POKEMON_NAME = db.Column(db.VARCHAR(50))
	ROUTE_POKEMON_GEN = db.Column(db.VARCHAR(50))
	ROUTE_POKEMON_LEVELS = db.Column(db.VARCHAR(50))
	ROUTE_POKEMON_RATE = db.Column(db.VARCHAR(50))
	ROUTE_POKEMON_METHOD = db.Column(db.VARCHAR(50))
	ROUTE_METHOD_IMG = db.Column(db.VARCHAR(256))

	def __init__(self, rName, pName, pGen, pLevel, pRate, pMethod, pImg):
		self.ROUTE_NAME = rName
		self.ROUTE_POKEMON_NAME = str(pName)
		self.ROUTE_POKEMON_GEN = pGen
		self.ROUTE_POKEMON_LEVELS = pLevel
		self.ROUTE_POKEMON_RATE = pRate
		self.ROUTE_POKEMON_METHOD = str(pMethod)
		self.ROUTE_METHOD_IMG = pImg

	@staticmethod
	def get_pokemon_routes(poke_name):
		return RoutePokemon.query.filter_by(ROUTE_POKEMON_NAME=poke_name)
		
	@staticmethod
	def get(routeName):
		return RoutePokemon.query.filter_by(ROUTE_NAME=routeName)

class RouteTrainers(db.Model):
	__tablename__ = "ROUTE_TRAINERS"

	ID = db.Column(db.Integer, primary_key=True)
	ROUTE_NAME = db.Column(db.VARCHAR(50))
	ROUTE_TRAINER_NAME = db.Column(db.VARCHAR(50))
	ROUTE_TRAINER_GEN = db.Column(db.VARCHAR(50))
	ROUTE_TRAINER_REWARD = db.Column(db.VARCHAR(50))
	ROUTE_TRAINER_IMG = db.Column(db.VARCHAR(256))

	def __init__(self, name, tName, tGen, tReward, tImg):
		self.ROUTE_NAME = name
		self.ROUTE_TRAINER_NAME = tName
		self.ROUTE_TRAINER_GEN = tGen
		self.ROUTE_TRAINER_REWARD = tReward
		self.ROUTE_TRAINER_IMG = tImg

	@staticmethod
	def get(routeName):
		return RouteTrainers.query.filter_by(ROUTE_NAME=routeName)


