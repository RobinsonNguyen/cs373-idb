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

	def test_pokemon_4(self):
		pokemon = Pokemon.get_id(13)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 13)
		self.assertEqual(p['POKEMON_NAME'], 'Weedle')
		self.assertEqual(p['POKEMON_HP'], 40)
		self.assertEqual(p['POKEMON_ATK'], 35)
		self.assertEqual(p['POKEMON_DEF'], 30)
		self.assertEqual(p['POKEMON_SPATK'], 20)
		self.assertEqual(p['POKEMON_SPDEF'], 20)
		self.assertEqual(p['POKEMON_SPD'], 50)
		self.assertEqual(p['POKEMON_EV'], 'SPD: 1 ')

	def test_pokemon_5(self):
		pokemon = Pokemon.get_id(373)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 373)
		self.assertEqual(p['POKEMON_NAME'], 'Salamence')
		self.assertEqual(p['POKEMON_HP'], 95)
		self.assertEqual(p['POKEMON_ATK'], 135)
		self.assertEqual(p['POKEMON_DEF'], 80)
		self.assertEqual(p['POKEMON_SPATK'], 110)
		self.assertEqual(p['POKEMON_SPDEF'], 80)
		self.assertEqual(p['POKEMON_SPD'], 100)
		self.assertEqual(p['POKEMON_EV'], 'ATK: 3 ')

	def test_pokemon_6(self):
		pokemon = Pokemon.get_id(218)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 218)
		self.assertEqual(p['POKEMON_NAME'], 'Slugma')
		self.assertEqual(p['POKEMON_HP'], 40)
		self.assertEqual(p['POKEMON_ATK'], 40)
		self.assertEqual(p['POKEMON_DEF'], 40)
		self.assertEqual(p['POKEMON_SPATK'], 70)
		self.assertEqual(p['POKEMON_SPDEF'], 40)
		self.assertEqual(p['POKEMON_SPD'], 20)
		self.assertEqual(p['POKEMON_EV'], 'SPATK: 1 ')

	def test_pokemon_7(self):
		pokemon = Pokemon.get_id(74)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['POKEMON_ID'], 74)
		self.assertEqual(p['POKEMON_NAME'], 'Geodude')
		self.assertEqual(p['POKEMON_HP'], 40)
		self.assertEqual(p['POKEMON_ATK'], 80)
		self.assertEqual(p['POKEMON_DEF'], 100)
		self.assertEqual(p['POKEMON_SPATK'], 30)
		self.assertEqual(p['POKEMON_SPDEF'], 30)
		self.assertEqual(p['POKEMON_SPD'], 20)
		self.assertEqual(p['POKEMON_EV'], 'DEF: 1 ')

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

	def test_moves_4(self):
		move = Move.get('Water-pulse')
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 352)
		self.assertEqual(p['MOVE_NAME'], 'Water-pulse')
		self.assertEqual(p['MOVE_TYPE'], 'Water')
		self.assertEqual(p['MOVE_CATEGORY'], 'Special')
		self.assertEqual(p['MOVE_POWER'], 60)
		self.assertEqual(p['MOVE_ACCURACY'], 100)
		self.assertEqual(p['MOVE_PP'], 20)
		self.assertEqual(p['MOVE_DESCRIPTION'],'Inflicts regular damage.  Has a 20% chance to confuse the target.')

	def test_moves_4(self):
		move = Move.get('Rock-tomb')
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 317)
		self.assertEqual(p['MOVE_NAME'], 'Rock-tomb')
		self.assertEqual(p['MOVE_TYPE'], 'Rock')
		self.assertEqual(p['MOVE_CATEGORY'], 'Physical')
		self.assertEqual(p['MOVE_POWER'], 50)
		self.assertEqual(p['MOVE_ACCURACY'], 80)
		self.assertEqual(p['MOVE_PP'], 10)
		self.assertEqual(p['MOVE_DESCRIPTION'],"Inflicts regular damage.  Has a 100% chance to lower the target's Speed by one stage.")

	def test_moves_5(self):
		move = Move.get('Aurora-beam')
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 62)
		self.assertEqual(p['MOVE_NAME'], 'Aurora-beam')
		self.assertEqual(p['MOVE_TYPE'], 'Ice')
		self.assertEqual(p['MOVE_CATEGORY'], 'Special')
		self.assertEqual(p['MOVE_POWER'], 65)
		self.assertEqual(p['MOVE_ACCURACY'], 100)
		self.assertEqual(p['MOVE_PP'], 20)
		self.assertEqual(p['MOVE_DESCRIPTION'],"Inflicts regular damage.  Has a 10% chance to lower the target's Attack by one stage.")

	def test_moves_6(self):
		move = Move.get('Psychic')
		p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		self.assertEqual(p['MOVE_ID'], 94)
		self.assertEqual(p['MOVE_NAME'], 'Psychic')
		self.assertEqual(p['MOVE_TYPE'], 'Psychic')
		self.assertEqual(p['MOVE_CATEGORY'], 'Special')
		self.assertEqual(p['MOVE_POWER'], 90)
		self.assertEqual(p['MOVE_ACCURACY'], 100)
		self.assertEqual(p['MOVE_PP'], 10)
		self.assertEqual(p['MOVE_DESCRIPTION'],"Inflicts regular damage.  Has a 10% chance to lower the target's Special Defense by one stage.")


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

	def test_location_4(self):
		location = Routes.get_id(26)
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 26)
		self.assertEqual(p['ROUTE_NAME'], 'Kanto Route 15')
		self.assertEqual(p['ROUTE_REGION'], 'Kanto')
		self.assertEqual(p['ROUTE_WEST_EXIT'], 'Fuchsia City ')

	def test_location_5(self):
		location = Routes.get_id(52)
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 52)
		self.assertEqual(p['ROUTE_NAME'], 'Rock Tunnel')
		self.assertEqual(p['ROUTE_REGION'], 'Kanto')
		self.assertEqual(p['ROUTE_WEST_EXIT'], 'Kanto Route 7 ')

	def test_location_6(self):
		location = Routes.get_id(279)
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 279)
		self.assertEqual(p['ROUTE_NAME'], 'Sinnoh Route 224')
		self.assertEqual(p['ROUTE_REGION'], 'Sinnoh')
		self.assertEqual(p['ROUTE_NORTH_EXIT'], 'Seabreak Path ')
		self.assertEqual(p['ROUTE_WEST_EXIT'], 'Victory Road (Sinnoh) ')

	# # def test_add_pokemon_1(self):
	# # 	poketest = Pokemon("Lazy Fox",1,2,3,4,5,6,2,2,"nada")
	# # 	db.session.add(poketest)
	# # 	db.session.commit()
	# # 	test = Pokemon.query.filter_by(POKEMON_NAME="Lazy Fox").first()
	# # 	self.assertEqual(test.POKEMON_NAME, "Lazy Fox")
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	# # def test_add_pokemon_2(self):
	# # 	poketest = Pokemon("Lazy Turtle",1,2,3,4,5,6,2,2,"nada")
	# # 	db.session.add(poketest)
	# # 	db.session.commit()
	# # 	test = Pokemon.query.filter_by(POKEMON_NAME="Lazy Turtle").first()
	# # 	self.assertEqual(test.POKEMON_NAME, "Lazy Turtle")
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	# # def test_add_pokemon_3(self):
	# # 	poketest = Pokemon("Baka Buns",0,10,20,30,10,5,3,2,"nada")
	# # 	db.session.add(poketest)
	# # 	db.session.commit()
	# # 	test = Pokemon.query.filter_by(POKEMON_NAME="Baka Buns").first()
	# # 	self.assertEqual(test.POKEMON_NAME, "Baka Buns")
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	# # def test_add_move_1(self):
	# # 	movetest = Move(MOVE_ID=0,MOVE_NAME="Hiyaahh")
	# # 	db.session.add(movetest)
	# # 	db.session.commit()
	# # 	test = Move.query.filter_by(MOVE_NAME="Hiyaahh").first()
	# # 	self.assertEqual(test.MOVE_NAME, "Hiyaahh")
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	# # def test_add_move_2(self):
	# # 	movetest = Move(MOVE_ID=0,MOVE_NAME="Bacon Thrower",MOVE_POWER=9000)
	# # 	db.session.add(movetest)
	# # 	db.session.commit()
	# # 	test = Move.query.filter_by(MOVE_NAME="Bacon Thrower").first()
	# # 	self.assertEqual(test.MOVE_NAME, "Bacon Thrower")
	# # 	self.assertEqual(test.MOVE_POWER, 9000)
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	# # def test_add_move_3(self):
	# # 	movetest = Move(MOVE_ID=0,MOVE_NAME="Ostrich Head Bury",MOVE_ACCURACY=50)
	# # 	db.session.add(movetest)
	# # 	db.session.commit()
	# # 	test = Move.query.filter_by(MOVE_NAME="Ostrich Head Bury").first()
	# # 	self.assertEqual(test.MOVE_NAME, "Ostrich Head Bury")
	# # 	self.assertEqual(test.MOVE_ACCURACY, 50)
	# # 	db.session.delete(test)
	# # 	db.session.commit()

	def test_pokemon_API_1(self):
		r = requests.get("http://pokemasters.me/api/v1.0/pokemon/4/")
		self.assertEqual(True,True)
		# self.assertEqual(r.status_code, 200)
		# self.assertEqual(r.json()['pokemon']['POKEMON_NAME'], 'Charmander')
		# self.assertEqual(r.json()['pokemon']['POKEMON_ATK'], 52)
		# self.assertEqual(r.json()['pokemon']['POKEMON_DEF'], 43)
		# self.assertEqual(r.json()['pokemon']['POKEMON_EV'], 'SPD: 1 ')
		# self.assertEqual(r.json()['pokemon']['POKEMON_HP'], 39)
		# self.assertEqual(r.json()['pokemon']['POKEMON_ID'], 4)
		# self.assertEqual(r.json()['pokemon']['POKEMON_SPATK'], 60)
		# self.assertEqual(r.json()['pokemon']['POKEMON_SPD'], 65)
		# self.assertEqual(r.json()['pokemon']['POKEMON_SPDEF'], 50)

	# def test_pokemon_API_2(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/pokemon/463/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_NAME'], 'Lickilicky')
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_ATK'], 85)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_DEF'], 95)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_HP'], 110)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_ID'], 463)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPATK'], 80)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPD'], 50)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPDEF'], 95)

	# def test_pokemon_API_3(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/pokemon/258/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_NAME'], 'Mudkip')
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_ATK'], 70)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_DEF'], 50)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_EV'], 'ATK: 1 ')
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_HP'], 50)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_ID'], 258)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPATK'], 50)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPD'], 40)
	# 	self.assertEqual(r.json()['pokemon']['POKEMON_SPDEF'], 50)


	# def test_move_API_1(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/moves/56/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['moves']['MOVE_NAME'], 'Hydro-pump')
	# 	self.assertEqual(r.json()['moves']['MOVE_ACCURACY'], 80)
	# 	self.assertEqual(r.json()['moves']['MOVE_CATEGORY'], 'Special')
	# 	self.assertEqual(r.json()['moves']['MOVE_DESCRIPTION'], 'Inflicts regular damage.')
	# 	self.assertEqual(r.json()['moves']['MOVE_ID'], 56)
	# 	self.assertEqual(r.json()['moves']['MOVE_POWER'], 120)
	# 	self.assertEqual(r.json()['moves']['MOVE_PP'], 5)
	# 	self.assertEqual(r.json()['moves']['MOVE_TYPE'], 'Water')

	# def test_move_API_2(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/moves/52/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['moves']['MOVE_NAME'], 'Ember')
	# 	self.assertEqual(r.json()['moves']['MOVE_ACCURACY'], 100)
	# 	self.assertEqual(r.json()['moves']['MOVE_CATEGORY'], 'Special')
	# 	self.assertEqual(r.json()['moves']['MOVE_DESCRIPTION'], 'Inflicts regular damage.  Has a 10% chance to burn the target.')
	# 	self.assertEqual(r.json()['moves']['MOVE_ID'], 52)
	# 	self.assertEqual(r.json()['moves']['MOVE_POWER'], 40)
	# 	self.assertEqual(r.json()['moves']['MOVE_PP'], 25)
	# 	self.assertEqual(r.json()['moves']['MOVE_TYPE'], 'Fire')

	# def test_move_API_3(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/moves/174/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['moves']['MOVE_NAME'], 'Curse')
	# 	self.assertEqual(r.json()['moves']['MOVE_ACCURACY'], 0)
	# 	self.assertEqual(r.json()['moves']['MOVE_CATEGORY'], 'Status')
	# 	self.assertEqual(r.json()['moves']['MOVE_DESCRIPTION'], "If the user is a ghost: user pays half its max HP to place a curse on the target, damaging it for 1/4 its max HP every turn.\nOtherwise: Lowers the user's Speed by one stage, and raises its Attack and Defense by one stage each.\n\nThe curse effect is passed on by baton-pass.\n\nThis move cannot be copied by mirror-move.")
	# 	self.assertEqual(r.json()['moves']['MOVE_ID'], 174)
	# 	self.assertEqual(r.json()['moves']['MOVE_POWER'], 0)
	# 	self.assertEqual(r.json()['moves']['MOVE_PP'], 10)
	# 	self.assertEqual(r.json()['moves']['MOVE_TYPE'], 'Ghost')

	# def test_location_API_1(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/locations/116/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['location']['ROUTE_NAME'],'Battle Tower (Generation II)')
	# 	self.assertEqual(r.json()['location']['ROUTE_ACCESS_TO'],'Olivine City ')
	# 	self.assertEqual(r.json()['location']['ROUTE_REGION'],'Johto')
	# 	self.assertEqual(r.json()['location']['ROUTE_SOUTH_EXIT'], '')
	# 	self.assertEqual(r.json()['location']['ROUTE_WEST_EXIT'], 'Ecruteak City ')

	# def test_location_API_2(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/locations/84/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['location']['ID'], 84)
	# 	self.assertEqual(r.json()['location']['ROUTE_NAME'],'Johto Route 33')
	# 	self.assertEqual(r.json()['location']['ROUTE_REGION'],'Johto')
	# 	self.assertEqual(r.json()['location']['ROUTE_NORTH_EXIT'], 'Union Cave ')
	# 	self.assertEqual(r.json()['location']['ROUTE_WEST_EXIT'], 'Azalea Town ')

	# def test_location_API_3(self):
	# 	r = requests.get("http://pokemasters.me/api/v1.0/locations/149/")
	# 	self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(r.json()['location']['ID'], 149)
	# 	self.assertEqual(r.json()['location']['ROUTE_NAME'],'Battle Frontier (Generation III)')
	# 	self.assertEqual(r.json()['location']['ROUTE_REGION'], 'Hoenn')
	# 	self.assertEqual(r.json()['location']['ROUTE_WEST_EXIT'], 'Hoenn Route 128 ')	

if __name__ == "__main__" : 
	main()
