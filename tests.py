#!/usr/bin/env python3
from unittest import main, TestCase
from models import PokemonContainer
from movesModel import Moves
from routeModel import RouteContainer

class UnitTestModels(TestCase):
	def test_pokemon_1(self):
		pokemonList = PokemonContainer()
		self.assertEqual(pokemonList.pokemon[0].id, 1)
		self.assertEqual(pokemonList.pokemon[0].name,"Bulbasaur")
		self.assertEqual(pokemonList.pokemon[1].type[0], "poison")
		self.assertEqual(pokemonList.pokemon[0].stats['HP'], 45)
		self.assertEqual(pokemonList.pokemon[0].stats['SPE'], 45)
		self.assertEqual(pokemonList.pokemon[0].stats['DEF'], 49)
		self.assertEqual(pokemonList.pokemon[0].stats['ATK'], 49)
		self.assertEqual(pokemonList.pokemon[0].stats['SPA'], 65)
		self.assertEqual(pokemonList.pokemon[0].stats['SPD'], 65)
		self.assertEqual(pokemonList.pokemon[0].eggGroup[0], "Plant")
		self.assertEqual(pokemonList.pokemon[0].moves[2].name, "Echoed-voice")
		self.assertEqual(pokemonList.pokemon[0].evolution[0].to, "Ivysaur")

	def test_pokemon_2(self):
		pokemonList = PokemonContainer()
		self.assertEqual(pokemonList.pokemon[1].id, 2)
		self.assertEqual(pokemonList.pokemon[1].name,"Ivysaur")
		self.assertEqual(pokemonList.pokemon[1].type[0], "poison")
		self.assertEqual(pokemonList.pokemon[1].stats['HP'], 60)
		self.assertEqual(pokemonList.pokemon[1].stats['SPE'], 60)
		self.assertEqual(pokemonList.pokemon[1].stats['DEF'], 63)
		self.assertEqual(pokemonList.pokemon[1].stats['ATK'], 62)
		self.assertEqual(pokemonList.pokemon[1].stats['SPA'], 80)
		self.assertEqual(pokemonList.pokemon[1].stats['SPD'], 80)
		self.assertEqual(pokemonList.pokemon[1].eggGroup[0], "Plant")
		self.assertEqual(pokemonList.pokemon[1].moves[1].name, "Grass-pledge")
		self.assertEqual(pokemonList.pokemon[1].evolution[0].to, "Venusaur")

	def test_pokemon_3(self):
		pokemonList = PokemonContainer()
		self.assertEqual(pokemonList.pokemon[33].id, 34)
		self.assertEqual(pokemonList.pokemon[33].name,"Nidoking")
		self.assertEqual(pokemonList.pokemon[33].type[1], "ground")
		self.assertEqual(pokemonList.pokemon[33].stats['HP'], 81)
		self.assertEqual(pokemonList.pokemon[33].stats['SPE'], 85)
		self.assertEqual(pokemonList.pokemon[33].stats['DEF'], 77)
		self.assertEqual(pokemonList.pokemon[33].stats['ATK'], 102)
		self.assertEqual(pokemonList.pokemon[33].stats['SPA'], 85)
		self.assertEqual(pokemonList.pokemon[33].stats['SPD'], 75)
		self.assertEqual(pokemonList.pokemon[33].eggGroup[0], "Ground")
		self.assertEqual(pokemonList.pokemon[33].moves[0].name, "Drill-run")

	def test_move_1(self):
		allMoves = Moves()
		self.assertEqual(allMoves.moves[0].id, 240)
		self.assertEqual(allMoves.moves[0].name, "Rain-dance")
		self.assertEqual(allMoves.moves[0].type, "Water")

	def test_move_2(self):
		allMoves = Moves()
		self.assertEqual(allMoves.moves[1].id, 156)
		self.assertEqual(allMoves.moves[1].name, "Rest")
		self.assertEqual(allMoves.moves[1].type, "Psychic")

	def test_move_3(self):
		pass

	def test_location_1(self):
		allRoutes = RouteContainer()
		self.assertEqual(allRoutes.routes[0].region, "Kanto")
		self.assertEqual(allRoutes.routes[0].name, "Route 15")
		self.assertEqual(allRoutes.routes[0].nextRoute, "Route 16")
		self.assertEqual(allRoutes.routes[0].pokemon[0].name, "Oddish")
		self.assertEqual(allRoutes.routes[0].trainers[1].name, "Biker Alex")
		self.assertEqual(allRoutes.routes[0].items[0].name, "TM18(Rain Dance)")

	def test_location_2(self):
		allRoutes = RouteContainer()
		self.assertEqual(allRoutes.routes[1].region, "Johto")
		self.assertEqual(allRoutes.routes[1].name, "Route 30")
		self.assertEqual(allRoutes.routes[1].prevRoute, "Route 29")
		self.assertEqual(allRoutes.routes[1].pokemon[0].name, "Poliwhirl")
		self.assertEqual(allRoutes.routes[1].trainers[0].name, "Youngster Joey")
		self.assertEqual(allRoutes.routes[1].items[0].name, "Potion")

	def test_location_2(self):
		allRoutes = RouteContainer()
		self.assertEqual(allRoutes.routes[2].region, "Johto")
		self.assertEqual(allRoutes.routes[2].name, "Route 31")
		self.assertEqual(allRoutes.routes[2].nextRoute, "Route 32")
		self.assertEqual(allRoutes.routes[2].pokemon[0].name, "Poliwag")
		self.assertEqual(allRoutes.routes[2].trainers[0].name, "Bug Catcher Wade")
		self.assertEqual(allRoutes.routes[2].items[0].name, "TM44 (Rest)")

if __name__ == "__main__" : 
	main()