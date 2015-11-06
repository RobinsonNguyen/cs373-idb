#!/usr/bin/env python3
from unittest import main, TestCase
from models import Pokemon, Move
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

	def test_pokemon_2(self):
		pokemon = Pokemon.get('Bulbasaur')
		p = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
		self.assertEqual(p['id'], 1)
		self.assertEqual(p['name'], 'Bulbasaur')
		self.assertEqual(p['hp'], 45)
		self.assertEqual(p['attack'], 49)
		self.assertEqual(p['defense'], 49)
		self.assertEqual(p['spAttack'], 65)
		self.assertEqual(p['spDefense'], 65)
		self.assertEqual(p['speed'], 45)


	def test_pokemon_3(self):
		pokemon = Pokemon.get_all()
		p = []
		for poke in pokemon:
			p.append({c.name: getattr(poke, c.name) for c in poke.__table__.columns})
		self.assertEqual(p[0]['id'], 1)
		self.assertEqual(p[0]['name'], 'Bulbasaur')
		self.assertEqual(p[1]['id'], 2)
		self.assertEqual(p[1]['name'], 'Ivysaur')

	def test_move_1(self):
		pass
		# allMoves = Moves()
		# self.assertEqual(allMoves.moves[239].id, 240)
		# self.assertEqual(allMoves.moves[239].name, "Rain-dance")
		# self.assertEqual(allMoves.moves[239].power, 0)

	def test_move_2(self):
		pass
		# allMoves = Moves()
		# self.assertEqual(allMoves.moves[155].id, 156)
		# self.assertEqual(allMoves.moves[155].name, "Rest")
		# self.assertEqual(allMoves.moves[155].power, 0)

	def test_move_3(self):
		pass
		# allMoves = Moves()
		# self.assertEqual(allMoves.moves[357].id, 358)
		# self.assertEqual(allMoves.moves[357].name, "Wake-up-slap")
		# self.assertEqual(allMoves.moves[357].power, 60)

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
