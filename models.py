import json
import flask.ext.whooshalchemy
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pokemon@localhost/pokemasters'


db = SQLAlchemy(app)


#This function is borrowed from 'Free Spirits'
def parse_query(query):
    """
    Helper method to parse the queries
    This function is invoked in Move, Pokemon, and Route's search functions
    """
    terms = query.lower().split()
    query = "\"" + query.lower() + "\""
    and_term = ""
    or_term = ""

    for i, term in enumerate(terms):
        if i != 0:
            and_term += " AND " + term
            or_term += " OR " + term
        else:
            and_term += term
            or_term += term

    return (and_term, or_term)

class Move(db.Model):
	__tablename__ = 'ALL_MOVES'
	__searchable__ = ['MOVE_NAME', 'MOVE_TYPE', 'MOVE_CATEGORY']
	MOVE_ID = db.Column(db.Integer, primary_key=True)
	MOVE_NAME = db.Column(db.VARCHAR(50))
	MOVE_TYPE = db.Column(db.VARCHAR(50))
	MOVE_CATEGORY = db.Column(db.VARCHAR(50))
	MOVE_POWER = db.Column(db.Integer)
	MOVE_ACCURACY = db.Column(db.Integer)
	MOVE_PP = db.Column(db.Integer)
	MOVE_DESCRIPTION = db.Column(db.TEXT)
	
	# def __init__(self, name, type, category, power, accuracy, pp, description):
	# 	self.MOVE_NAME = name
	# 	self.MOVE_TYPE = type
	# 	self.MOVE_CATEGORY = category
	# 	self.MOVE_POWER = power
	# 	self.MOVE_ACCURACY = accuracy
	# 	self.MOVE_PP = pp
	# 	self.MOVE_DESCRIPTION = description
		
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
	def search(query):
		and_term, or_term = parse_query(query)

		or_results = []
		and_results = []

		or_seen = []
		and_seen = []

		or_moves = Move.query.whoosh_search(or_term, or_=True)
		and_moves = Move.query.whoosh_search(and_term)

		for op in or_moves:
			if op not in or_seen:
				or_results.append( [op, "NAME", None] )
				or_seen.append(op)

		for ap in and_moves:
			if ap not in and_seen:
				and_results.append( [ap, "NAME", None] )
				and_seen.append(ap)

		#search poke moves
		or_poke = PokemonMoves.query.whoosh_search(or_term, or_=True)
		and_poke = PokemonMoves.query.whoosh_search(and_term)

		#get moves from pokemoves
		for a in or_poke:
			m = Move.query.filter_by(MOVE_NAME=a.POKEMON_MOVE).first()
			if m not in or_seen:
				or_results.append( [m, "POKEMON", a] )
				or_seen.append(m)

		for a in and_poke:
			m = Move.query.filter_by(MOVE_NAME=a.POKEMON_MOVE).first()
			if m not in and_seen:
				and_results.append( [m, "POKEMON", a] )
				and_seen.append(m)

		return and_results, or_results
		
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
	__searchable__ = ['POKEMON_NAME', 'POKEMON_ID']
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
	POKEMON_EV = db.Column(db.VARCHAR(250))
	
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
		return '<name {}>'.format(self.POKEMON_NAME)
	
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

	@staticmethod
	def search(query):
		and_term, or_term = parse_query(query)

		or_results = []
		and_results = []

		and_seen = []
		or_seen = []

		or_pokemon = Pokemon.query.whoosh_search(or_term, or_=True)
		and_pokemon = Pokemon.query.whoosh_search(and_term)

		for op in or_pokemon:
			if op not in or_seen:
				or_results.append( [op, "NAME", None] )
				or_seen.append(op)

		for ap in and_pokemon:
			if ap not in and_seen:
				and_results.append( [ap, "NAME", None] )
				and_seen.append(ap)

		#search evolutions
		or_evos = Evolutions.query.whoosh_search(or_term, or_=True)
		and_evos = Evolutions.query.whoosh_search(and_term)

		#get pokemon from evolution
		for evo in or_evos:
			p = Pokemon.query.filter_by(POKEMON_NAME=evo.POKEMON_NAME).first()
			if p not in or_seen:
				or_results.append( [p, "EVOLUTION", evo] )
				or_seen.append(p)

		for evo in and_evos:
			p = Pokemon.query.filter_by(POKEMON_NAME=evo.POKEMON_NAME).first()
			if p not in and_seen:
				and_results.append( [p, "EVOLUTION", evo] )
				and_seen.append(p)

		#If we search by move name, return all pokemon that can learn that move
		or_moves = PokemonMoves.query.whoosh_search(or_term, or_=True)
		and_moves = PokemonMoves.query.whoosh_search(and_term)

		#get pokemon from move
		for move in or_moves:
			m = Pokemon.query.filter_by(POKEMON_NAME=move.POKEMON_NAME).first()
			if m not in or_seen:
				or_results.append( [m, "MOVE", move] )
				or_seen.append(m)

		for move in and_moves:
			m = Pokemon.query.filter_by(POKEMON_NAME=move.POKEMON_NAME).first()
			if m not in and_seen:
				and_results.append( [m, "MOVE", move] )
				and_seen.append(m)
				
		#Find route pokemon with given location  
		or_locs = RoutePokemon.query.whoosh_search(or_term, or_=True)
		and_locs = RoutePokemon.query.whoosh_search(and_term)

		#get pokemon from route
		for loc in or_locs:
			m = Pokemon.query.filter_by(POKEMON_NAME=loc.ROUTE_POKEMON_NAME)
			for r in m:
				if r not in or_seen:
					or_results.append( [r, "ROUTE", loc] )
					or_seen.append(r)

		for loc in and_locs:
			m = Pokemon.query.filter_by(POKEMON_NAME=loc.ROUTE_POKEMON_NAME)
			for r in m:
				if r not in and_seen:
					and_results.append( [r, "ROUTE", loc] )
					and_seen.append(r)


		#Search the type table
		or_types = Types.query.whoosh_search(or_term, or_=True)
		and_types = Types.query.whoosh_search(and_term)

		#get pokemon from type
		for typ in or_types:
			t = Pokemon.query.filter_by(POKEMON_NAME=typ.POKEMON_NAME).first()
			if t not in or_seen:
				or_results.append( [t, "TYPE", typ] )
				or_seen.append(t)

		for typ in and_types:
			t = Pokemon.query.filter_by(POKEMON_NAME=typ.POKEMON_NAME).first()
			if t not in and_seen:
				and_results.append( [t, "TYPE", typ] )
				and_seen.append(t)

		return and_results, or_results
	
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
	__searchable__ = ['ROUTE_NAME', 'ROUTE_REGION', 'ROUTE_NORTH_EXIT', 'ROUTE_SOUTH_EXIT', 'ROUTE_EAST_EXIT' ,'ROUTE_WEST_EXIT']
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
	def search(query):
		and_term, or_term = parse_query(query)

		or_seen = []
		and_seen = []

		or_results = []
		and_results = []

		or_routes = Routes.query.whoosh_search(or_term, or_=True)
		and_routes = Routes.query.whoosh_search(and_term)

		for op in or_routes:
			if op not in or_seen:
				or_results.append( [op, "NAME", None] )
				or_seen.append(op)

		for ap in and_routes:
			if ap not in and_seen:
				and_results.append( [ap, "NAME", None] )
				and_seen.append(ap)

		#search routes
		or_loc = RoutePokemon.query.whoosh_search(or_term, or_=True)
		and_loc = RoutePokemon.query.whoosh_search(and_term)

		#get routes from Routes
		for a in or_loc:
			r = Routes.query.filter_by(ROUTE_NAME=a.ROUTE_NAME).first()
			if r not in or_seen:
				or_results.append( [r, "POKEMON", a] )
				or_seen.append(r)

		for a in and_loc:
			r = Routes.query.filter_by(ROUTE_NAME=a.ROUTE_NAME).first()
			if r not in and_seen:
				and_results.append( [r, "POKEMON", a] )
				and_seen.append(r)

		return and_results, or_results

	@staticmethod
	def get_all():
		return Routes.query.all()
		
	@staticmethod
	def get(name):
		return Routes.query.filter_by(ROUTE_NAME=name).first()

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
	__searchable__ = ['POKEMON_EVOLUTION', 'POKEMON_NAME']
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
	__searchable__ = ['POKEMON_TYPE']

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
	__searchable__ = ['POKEMON_NAME', 'POKEMON_MOVE']

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

	@staticmethod
	def get(routeName):
		return RouteItems.query.filter_by(ROUTE_NAME=routeName)

class RoutePokemon(db.Model):
	__tablename__ = "ROUTE_POKEMON"
	__searchable__ = ['ROUTE_NAME', 'ROUTE_POKEMON_NAME']
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

flask.ext.whooshalchemy.whoosh_index(app, Move)
flask.ext.whooshalchemy.whoosh_index(app, Pokemon)
flask.ext.whooshalchemy.whoosh_index(app, Routes)
flask.ext.whooshalchemy.whoosh_index(app, Evolutions)
flask.ext.whooshalchemy.whoosh_index(app, PokemonMoves)
flask.ext.whooshalchemy.whoosh_index(app, RoutePokemon)
flask.ext.whooshalchemy.whoosh_index(app, Types)



