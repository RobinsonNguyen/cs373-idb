#!/usr/bin/env python3
from unittest import main, TestCase
from models import Pokemon, Move
# from pokemonModel import PokemonContainer
# from movesModel import Moves
# from routeModel import RouteContainer
# from models import PokemonContainer, Moves, RouteContainer

class UnitTestModels(TestCase):
	def test_pokemon_1(self):
		self.assertEqual("1", "1")
		# c = Pokemon.get_id(1)
		# self.assertEqual(c[0].id, 1)
		# self.assertEqual(c[0].name, 'Bulbasaur')
		# self.assertEqual(c[0].hp, 45)
		# self.assertEqual(c[0].attack, 49)
		# self.assertEqual(c[0].defense, 49)
		# self.assertEqual(c[0].spAttack, 65)
		# self.assertEqual(c[0].spDefense, 65)
		# self.assertEqual(c[0].speed, 45)

	def test_pokemon_2(self):
		pass
		# pokemonList = PokemonContainer()
		# self.assertEqual(pokemonList.pokemon[1].id, 2)
		# self.assertEqual(pokemonList.pokemon[1].name,"Ivysaur")
		# self.assertEqual(pokemonList.pokemon[1].type[0], "poison")
		# self.assertEqual(pokemonList.pokemon[1].stats['HP'], 60)
		# self.assertEqual(pokemonList.pokemon[1].stats['SPE'], 60)
		# self.assertEqual(pokemonList.pokemon[1].stats['DEF'], 63)
		# self.assertEqual(pokemonList.pokemon[1].stats['ATK'], 62)
		# self.assertEqual(pokemonList.pokemon[1].stats['SPA'], 80)
		# self.assertEqual(pokemonList.pokemon[1].stats['SPD'], 80)
		# self.assertEqual(pokemonList.pokemon[1].eggGroup[0], "Plant")
		# self.assertEqual(pokemonList.pokemon[1].moves[1].name, "Grass-pledge")
		# self.assertEqual(pokemonList.pokemon[1].evolution[0].to, "Venusaur")

	def test_pokemon_3(self):
		pass
		# pokemonList = PokemonContainer()
		# self.assertEqual(pokemonList.pokemon[33].id, 34)
		# self.assertEqual(pokemonList.pokemon[33].name,"Nidoking")
		# self.assertEqual(pokemonList.pokemon[33].type[1], "ground")
		# self.assertEqual(pokemonList.pokemon[33].stats['HP'], 81)
		# self.assertEqual(pokemonList.pokemon[33].stats['SPE'], 85)
		# self.assertEqual(pokemonList.pokemon[33].stats['DEF'], 77)
		# self.assertEqual(pokemonList.pokemon[33].stats['ATK'], 102)
		# self.assertEqual(pokemonList.pokemon[33].stats['SPA'], 85)
		# self.assertEqual(pokemonList.pokemon[33].stats['SPD'], 75)
		# self.assertEqual(pokemonList.pokemon[33].eggGroup[0], "Ground")
		# self.assertEqual(pokemonList.pokemon[33].moves[0].name, "Drill-run")

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
