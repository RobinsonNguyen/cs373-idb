#!/usr/bin/env python3
from unittest import main, TestCase
from models import *
# from pokemonModel import PokemonContainer
# from movesModel import Moves
# from routeModel import RouteContainer
# from models import PokemonContainer, Moves, RouteContainer

class UnitTestModels(TestCase):
	def test_pokemon_1(self):
		pokemon = Pokemon.get_id(1)
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['id'], 1)
		self.assertEqual(p['name'], 'Bulbasaur')
		self.assertEqual(p['hp'], 45)
		self.assertEqual(p['attack'], 49)
		self.assertEqual(p['defense'], 49)
		self.assertEqual(p['spAttack'], 65)
		self.assertEqual(p['spDefense'], 65)
		self.assertEqual(p['speed'], 45)

	# def test_pokemon_2(self):
	# 	pokemon = Pokemon.get('Bulbasaur')
	# 	p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
	# 	self.assertEqual(p['id'], 1)
	# 	self.assertEqual(p['name'], 'Bulbasaur')
	# 	self.assertEqual(p['hp'], 45)
	# 	self.assertEqual(p['attack'], 49)
	# 	self.assertEqual(p['defense'], 49)
	# 	self.assertEqual(p['spAttack'], 65)
	# 	self.assertEqual(p['spDefense'], 65)
	# 	self.assertEqual(p['speed'], 45)


	# def test_pokemon_3(self):
	# 	pokemon = Pokemon.get_all()
	# 	p = []
	# 	for poke in pokemon:
	# 		p.append({c.name: getattr(poke, c.name) for c in poke.__table__.columns})
	# 	self.assertEqual(p[0]['id'], 1)
	# 	self.assertEqual(p[0]['name'], 'Bulbasaur')
	# 	self.assertEqual(p[1]['id'], 2)
	# 	self.assertEqual(p[1]['name'], 'Ivysaur')

	# def test_pokemon_4(self):
	# 	p = Pokemon('Jimmy', 1,2,3,4,5,6,'image')
	# 	self.assertEqual(p.name, 'Jimmy')
	# 	self.assertEqual(p.hp, 1)
	# 	self.assertEqual(p.attack, 1)
	# 	self.assertEqual(p.defense, 1)
	# 	self.assertEqual(p.spAttack, 1)
	# 	self.assertEqual(p.spDefense, 1)
	# 	self.assertEqual(p.speed, 1)
	# 	self.assertEqual(p.imgPath, "image")

	def test_moves_1(self):
		pass
		#move = Move.get_id(1)
		#p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
		#self.assertEqual(p['id'], 1)
		#self.assertEqual(p['name'], 'Pound')
		#self.assertEqual(p['power'], 45)
		#self.assertEqual(p['accuracy'], 49)
		#self.assertEqual(p['pp'], 49)

	# def test_moves_2(self):
	# 	move = Move.get('Pound')
	# 	p = {c.name: getattr(move, c.name) for c in move.__table__.columns}
	# 	self.assertEqual(p['id'], 1)
	# 	#self.assertEqual(p['name'], 'Pound')
	# 	#self.assertEqual(p['power'], 45)
	# 	#self.assertEqual(p['accuracy'], 49)
	# 	#self.assertEqual(p['pp'], 49)


	# def test_moves_3(self):
	# 	moves = Move.get_all()
	# 	p = []
	# 	for move in moves:
	# 		p.append({c.name: getattr(move, c.name) for c in move.__table__.columns})
	# 	self.assertEqual(p[0]['id'], 1)
	# 	self.assertEqual(p[0]['name'], 'Pound')
	# 	self.assertEqual(p[1]['id'], 2)
	# 	#self.assertEqual(p[1]['name'], 'Ivysaur')

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
		pass
		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[0].region, "Kanto")
		# self.assertEqual(allRoutes.routes[0].name, "Route 15")
		# self.assertEqual(allRoutes.routes[0].nextRoute, "Route 16")
		# self.assertEqual(allRoutes.routes[0].pokemon[0].name, "Oddish")
		# self.assertEqual(allRoutes.routes[0].trainers[1].name, "Biker Alex")
		# self.assertEqual(allRoutes.routes[0].items[0].name, "Rain-dance")

	def test_location_2(self):
		pass
		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[1].region, "Johto")
		# self.assertEqual(allRoutes.routes[1].name, "Route 30")
		# self.assertEqual(allRoutes.routes[1].prevRoute, "Route 29")
		# self.assertEqual(allRoutes.routes[1].pokemon[0].name, "Poliwhirl")
		# self.assertEqual(allRoutes.routes[1].trainers[0].name, "Youngster Joey")
		# self.assertEqual(allRoutes.routes[1].items[0].name, "Potion")

	def test_location_3(self):
		pass
		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[2].region, "Johto")
		# self.assertEqual(allRoutes.routes[2].name, "Route 31")
		# self.assertEqual(allRoutes.routes[2].nextRoute, "Route 32")
		# self.assertEqual(allRoutes.routes[2].pokemon[0].name, "Poliwag")
		# self.assertEqual(allRoutes.routes[2].trainers[0].name, "Bug Catcher Wade")
		# self.assertEqual(allRoutes.routes[2].items[0].name, "Rest")

if __name__ == "__main__" : 
	main()
