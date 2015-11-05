import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pokemon@localhost/pokemasters'
db = SQLAlchemy(app)

class Move(db.Model):
	__tablename__ = 'ALL_MOVES'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.VARCHAR(50))
	type = db.Column(db.VARCHAR(50))
	category = db.Column(db.VARCHAR(50))
	power = db.Column(db.Integer)
	accuracy = db.Column(db.Integer)
	pp = db.Column(db.Integer)
	description = db.Column(db.BLOB)
	
	def __init__(self, name, type, category, power, accuracy, pp, description):
		self.name = name
		self.type = type
		self.category = category
		self.power = power
		self.accuracy = accuracy
		self.pp = pp
		self.description = description
		
	def __repr__(self):
		"""
        Return representation of this move in format
        <name {}> where {} is move's name
        """
		return '<name {}>'.format(self.name)
		
	@property
	def serialize(self):
		return {
            'name' : self.name,
            'type' : self.type,
            'category' : self.category,
            'power' : self.power,
            'accuracy' : self.accuracy,
            'pp' : self.pp,
            'description' : self.description}
		
	@staticmethod
	def get_all():
		return Move.query.all()
		
	@staticmethod
	def get(move):
		return Move.query.filter_by(name=move).first()
		

	
class Pokemon(db.Model):
	__tablename__ = "pokemon"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.VARCHAR(50))
	hp = db.Column(db.Integer)
	attack = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	spAttack = db.Column(db.Integer)
	spDefense = db.Column(db.Integer)
	speed = db.Column(db.Integer)
	stats = []
	
	def __init__(self, name, hp, attack, defense, spAttack, spDefense, speed):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.spAttack = spAttack
		self.spDefense = spDefense
		self.speed = speed
		
	def __repr__(self):
		return '<name {}>'.format(self.name)
	
	@property
	def serialize(self):
		dtest = {
			'name' : self.name,
			'hp' : self.hp, 
			'atk' : self.attack, 
			'def' : self.defense, 
			'spa' : self.spAttack, 
			'spd' : self.spDefense, 
			'spe' : self.speed,
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
