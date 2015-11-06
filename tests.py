#!/usr/bin/env python3
from unittest import main, TestCase
from models import Pokemon, Move, Routes
# from pokemonModel import PokemonContainer
# from movesModel import Moves
# from routeModel import RouteContainer
# from models import PokemonContainer, Moves, RouteContainer

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

		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[0].region, "Kanto")
		# self.assertEqual(allRoutes.routes[0].name, "Route 15")
		# self.assertEqual(allRoutes.routes[0].nextRoute, "Route 16")
		# self.assertEqual(allRoutes.routes[0].pokemon[0].name, "Oddish")
		# self.assertEqual(allRoutes.routes[0].trainers[1].name, "Biker Alex")
		# self.assertEqual(allRoutes.routes[0].items[0].name, "Rain-dance")

	def test_location_2(self):
		location = Routes.get_id(1)
		p = {c.name: getattr(location, c.name) for c in location.__table__.columns}
		self.assertEqual(p['ID'], 1)
		self.assertEqual(p['ROUTE_NAME'], 'Pallet Town')
		self.assertEqual(p['ROUTE_REGION'], 'Kanto')
		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[1].region, "Johto")
		# self.assertEqual(allRoutes.routes[1].name, "Route 30")
		# self.assertEqual(allRoutes.routes[1].prevRoute, "Route 29")
		# self.assertEqual(allRoutes.routes[1].pokemon[0].name, "Poliwhirl")
		# self.assertEqual(allRoutes.routes[1].trainers[0].name, "Youngster Joey")
		# self.assertEqual(allRoutes.routes[1].items[0].name, "Potion")

	def test_location_3(self):
		location = Routes.get_all()
		p = []
		for route in routes:
			p.append({c.name: getattr(route, c.name) for c in location.__table__.columns})
		self.assertEqual(p[0]['ID'], 1)
		self.assertEqual(p[0]['ROUTE_NAME'], 'Pallet Town')
		self.assertEqual(p[0]['ROUTE_REGION'], 'Kanto')
		self.assertEqual(p[1]['ID'], 2)
		self.assertEqual(p[1]['ROUTE_NAME'], 'Viridian City')
		self.assertEqual(p[1]['ROUTE_REGION'], 'Kanto')
		# allRoutes = RouteContainer()
		# self.assertEqual(allRoutes.routes[2].region, "Johto")
		# self.assertEqual(allRoutes.routes[2].name, "Route 31")
		# self.assertEqual(allRoutes.routes[2].nextRoute, "Route 32")
		# self.assertEqual(allRoutes.routes[2].pokemon[0].name, "Poliwag")
		# self.assertEqual(allRoutes.routes[2].trainers[0].name, "Bug Catcher Wade")
		# self.assertEqual(allRoutes.routes[2].items[0].name, "Rest")

if __name__ == "__main__" : 
	main()
