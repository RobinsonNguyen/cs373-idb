#!/usr/bin/env python3
from unittest import main, TestCase
from models import Pokemon, Move, Routes
from models import db
import requests


class UnitTestModels(TestCase):
	def test_pokemon_1(self):
		pokemon = Pokemon.get_id(1)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 1)
		self.assertEqual(p['POKEMON_NAME'], 'Bulbasaur')
		self.assertEqual(p['POKEMON_HP'], 45)
		self.assertEqual(p['POKEMON_ATK'], 49)
		self.assertEqual(p['POKEMON_DEF'], 49)
		self.assertEqual(p['POKEMON_SPATK'], 65)
		self.assertEqual(p['POKEMON_SPDEF'], 65)
		self.assertEqual(p['POKEMON_SPD'], 45)

	def test_pokemon_2(self):
		pokemon = Pokemon.get('Bulbasaur')
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 1)
		self.assertEqual(p['POKEMON_NAME'], 'Bulbasaur')
		self.assertEqual(p['POKEMON_HP'], 45)
		self.assertEqual(p['POKEMON_ATK'], 49)
		self.assertEqual(p['POKEMON_DEF'], 49)
		self.assertEqual(p['POKEMON_SPATK'], 65)
		self.assertEqual(p['POKEMON_SPDEF'], 65)
		self.assertEqual(p['POKEMON_SPD'], 45)


	def test_pokemon_3(self):
		pokemon = Pokemon.get_all()
		p = []
		for poke in pokemon:
			p.append({c.name: getattr(poke, c.name) for c in poke.__table__.columns})
		self.assertEqual(p[0]['POKEMON_ID'], 1)
		self.assertEqual(p[0]['POKEMON_NAME'], 'Bulbasaur')
		self.assertEqual(p[1]['POKEMON_ID'], 2)
		self.assertEqual(p[1]['POKEMON_NAME'], 'Ivysaur')


	def test_moves_1(self):
		move = Move.get_id(1)
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 1)
		self.assertEqual(p['MOVE_NAME'], 'Pound')
		self.assertEqual(p['MOVE_POWER'], 40)
		self.assertEqual(p['MOVE_ACCURACY'], 100)
		self.assertEqual(p['MOVE_PP'], 35)

	def test_moves_2(self):
		move = Move.get('Pound')
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 1)
		self.assertEqual(p['MOVE_NAME'], 'Pound')
		self.assertEqual(p['MOVE_POWER'], 40)
		self.assertEqual(p['MOVE_ACCURACY'], 100)
		self.assertEqual(p['MOVE_PP'], 35)


	def test_moves_3(self):
		moves = Move.get_all()
		p = []
		for move in moves:
			p.append({c.name: getattr(move, c.name) for c in move.__table__.columns})
		self.assertEqual(p[0]['MOVE_ID'], 1)
		self.assertEqual(p[0]['MOVE_NAME'], 'Pound')
		self.assertEqual(p[1]['MOVE_ID'], 2)
		self.assertEqual(p[1]['MOVE_NAME'], 'Karate-chop')

	# def test_moves_4(self):
	# 	p = Move('Punch', 'fighting', 'physical', 300, 100, 100, 'A strong punch')
	# 	self.assertEqual(p.name, 'Punch')
	# 	self.assertEqual(p.type, 'fighting')
	# 	self.assertEqual(p.category, 'physical')
	# 	self.assertEqual(p.power, 300)
	# 	self.assertEqual(p.accuracy, 100)
	# 	self.assertEqual(p.pp, 100)
	# 	self.assertEqual(p.description, 'A strong punch')

	def test_location_1(self):
		location = Routes.get('Pallet Town')
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 1)
		self.assertEqual(p['ROUTE_NAME'], 'Pallet Town')
		self.assertEqual(p['ROUTE_REGION'], 'Kanto')

	def test_location_2(self):
		location = Routes.get_id(1)
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 1)
		self.assertEqual(p['ROUTE_NAME'], 'Pallet Town')
		self.assertEqual(p['ROUTE_REGION'], 'Kanto')

	def test_location_3(self):
		locations = Routes.get_all()
		p = []
		for route in locations:
			p.append({c.name: getattr(route, c.name) for c in route.__table__.columns})
		self.assertEqual(p[0]['ID'], 1)
		self.assertEqual(p[0]['ROUTE_NAME'], 'Pallet Town')
		self.assertEqual(p[0]['ROUTE_REGION'], 'Kanto')
		self.assertEqual(p[1]['ID'], 2)
		self.assertEqual(p[1]['ROUTE_NAME'], 'Viridian City')
		self.assertEqual(p[1]['ROUTE_REGION'], 'Kanto')

	# def test_add_pokemon_1(self):
	# 	poketest = Pokemon("Lazy Fox",1,2,3,4,5,6,2,2,"nada")
	# 	db.session.add(poketest)
	# 	db.session.commit()
	# 	test = Pokemon.query.filter_by(POKEMON_NAME="Lazy Fox").first()
	# 	self.assertEqual(test.POKEMON_NAME, "Lazy Fox")
	# 	db.session.delete(test)
	# 	db.session.commit()

	# def test_add_pokemon_2(self):
	# 	poketest = Pokemon("Lazy Turtle",1,2,3,4,5,6,2,2,"nada")
	# 	db.session.add(poketest)
	# 	db.session.commit()
	# 	test = Pokemon.query.filter_by(POKEMON_NAME="Lazy Turtle").first()
	# 	self.assertEqual(test.POKEMON_NAME, "Lazy Turtle")
	# 	db.session.delete(test)
	# 	db.session.commit()

	# def test_add_pokemon_3(self):
	# 	poketest = Pokemon("Baka Buns",0,10,20,30,10,5,3,2,"nada")
	# 	db.session.add(poketest)
	# 	db.session.commit()
	# 	test = Pokemon.query.filter_by(POKEMON_NAME="Baka Buns").first()
	# 	self.assertEqual(test.POKEMON_NAME, "Baka Buns")
	# 	db.session.delete(test)
	# 	db.session.commit()

	# def test_add_move_1(self):
	# 	movetest = Move(MOVE_ID=0,MOVE_NAME="Hiyaahh")
	# 	db.session.add(movetest)
	# 	db.session.commit()
	# 	test = Move.query.filter_by(MOVE_NAME="Hiyaahh").first()
	# 	self.assertEqual(test.MOVE_NAME, "Hiyaahh")
	# 	db.session.delete(test)
	# 	db.session.commit()

	# def test_add_move_2(self):
	# 	movetest = Move(MOVE_ID=0,MOVE_NAME="Bacon Thrower",MOVE_POWER=9000)
	# 	db.session.add(movetest)
	# 	db.session.commit()
	# 	test = Move.query.filter_by(MOVE_NAME="Bacon Thrower").first()
	# 	self.assertEqual(test.MOVE_NAME, "Bacon Thrower")
	# 	self.assertEqual(test.MOVE_POWER, 9000)
	# 	db.session.delete(test)
	# 	db.session.commit()

	# def test_add_move_3(self):
	# 	movetest = Move(MOVE_ID=0,MOVE_NAME="Ostrich Head Bury",MOVE_ACCURACY=50)
	# 	db.session.add(movetest)
	# 	db.session.commit()
	# 	test = Move.query.filter_by(MOVE_NAME="Ostrich Head Bury").first()
	# 	self.assertEqual(test.MOVE_NAME, "Ostrich Head Bury")
	# 	self.assertEqual(test.MOVE_ACCURACY, 50)
	# 	db.session.delete(test)
	# 	db.session.commit()

	def test_API_1(self):
		r = requests.get("http://pokemasters.me/api/v1.0/pokemon/4/")
		self.assertEqual(r.json()['pokemon']['POKEMON_NAME'], 'Charmander')
		self.assertEqual(r.json()['pokemon']['POKEMON_SPATK'], 60)

	def test_API_2(self):
		r = requests.get("http://pokemasters.me/api/v1.0/moves/56/")
		self.assertEqual(r.json()['moves']['MOVE_NAME'], 'Hydro-pump')
		self.assertEqual(r.json()['moves']['MOVE_TYPE'], 'Water')

	def test_API_3(self):
		r = requests.get("http://pokemasters.me/api/v1.0/locations/116/")
		self.assertEqual(r.json()['location']['ROUTE_ACCESS_TO'],'Olivine City ')
		self.assertEqual(r.json()['location']['ROUTE_SOUTH_EXIT'], 'Johto Route 47 ')
		



if __name__ == "__main__" : 
	main()
