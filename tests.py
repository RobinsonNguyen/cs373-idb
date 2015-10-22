#!/usr/bin/env python3
from unittest import main, TestCase
from movesModel import Moves

class UnitTestModels(TestCase):
	def test_move_1(self):
		allMoves = Moves()
		allMoves.move
		self.assertEqual(allMoves.moves[0].id, 1)
		self.assertEqual(allMoves.moves[0].name, "Rain-dance")
		self.assertEqual(allMoves.moves[0].type, "Water")

	def test_move_2(self):
		allMoves = Moves()
		allMoves.move
		self.assertEqual(allMoves.moves[1].id, 2)

if __name__ == "__main__" : 
	main()