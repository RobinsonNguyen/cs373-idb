import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pokemon@localhost/pokemasters'
db = SQLAlchemy(app)

class Move(db.Model):
	__tablename__ = 'ALL_MOVES'
	id = db.Column(db.Integer, primary_key=True)
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
		
	def __repr__(self):
		"""
        Return representation of this move in format
        <name {}> where {} is move's name
        """
		return '<name {}>'.format(self.name)
		
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
	
	
	def __init__(self, name, hp, attack, defense, spAttack, spDefense, speed):
		self.POKEMON_NAME = name
		self.POKEMON_HP = hp
		self.POKEMON_ATK = attack
		self.POKEMON_DEF = defense
		self.POKEMON_SPATK = spAttack
		self.POKEMON_SPDEF = spDefense
		self.POKEMON_SPD = speed
		
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
			'spd' : self.POKEMON_SPD, 
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
		return Pokemon.query.filter_by(name=name).first()

	@staticmethod
	def get_id(id):
		return Pokemon.query.filter_by(id=id).first()
		
class Pokemon_Moves(db.Model):
	__tablename__ = "pokemon_moves"

	id = db.Column(db.Integer, primary_key=True)
	pokemon_id = db.Column(db.Integer)
	move_id = db.Column(db.Integer)
	
	def __init__(self, pokemon_id, move_id):
		self.pokemon_id = pokemon_id
		self.move_id = move_id


class Routes(db.Model):
	__tablename__ = "ALL_ROUTES"

	ROUTE_NAME = db.Column(db.VARCHAR(50), primary_key=True)
	ROUTE_REGION = db.Column(db.VARCHAR(50))
	ROUTE_NORTH_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_SOUTH_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_EAST_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_WEST_EXIT = db.Column(db.VARCHAR(50))
	ROUTE_ACCESS_TO = db.Column(db.VARCHAR(50))
	ROUTE_MINI_DESCRIPTION = db.Column(db.VARCHAR(50))
	ROUTE_MAIN_DESCRIPTION = db.Column(db.BLOB)
	ROUTE_TRIVIA = db.Column(db.BLOB)

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

class Trainers(db.Model):
	__tablename__ = "ALL_TRAINERS"

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

	POKEMON_ID = db.Column(db.Integer)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_ABILITY = db.Column(db.VARCHAR(50))

	def __init__(self, name, ability):
		self.POKEMON_NAME = name
		self.POKEMON_ABILITY = ability

class Evolutions(db.Model):
	__tablename__ = "POKEMON_EVOLUTIONS"

	POKEMON_ID = db.Column(db.Integer)
	POKEMON_NAME = db.Column(db.VARCHAR(50))
	POKEMON_EVOLUTION = db.Column(db.VARCHAR(50))
	POKEMON_EVOLVE_METHOD = db.Column(db.VARCHAR(50))
	POKEMON_EVOLVE_LEVEL = db.Column(db.Integer)

	def __init__(self, name, evolution, method, level):
		self.POKEMON_NAME = name
		self.POKEMON_EVOLUTION = evolution
		self.POKEMON_EVOLVE_METHOD = method
		self.POKEMON_EVOLVE_LEVEL = level

