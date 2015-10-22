import json
from models import PokemonContainer

class Moves:

	class pokemon:

		def __init__(self):
			self.id = 0
			self.name = ""
			self.lvl = 0
			self.tm = ""
			self.hp = 0
			self.atk = 0
			self.defs = 0
			self.speed = 0
			self.sp_atk = 0
			self.sp_def = 0
			self.type = ()


	class move:

		def __init__(self):
			self.id = 0
			self.name = ""
			self.tm = ""
			self.type = ""
			self.category = ""
			self.power = ""
			self.accuracy = ""
			self.pp = ""
			self.description = ""
			self.pokemonLVL= []
			self.pokemonTM= []

	def __init__(self):
		self.ReadMoves()
		self.ReadAllMoves()

	def ReadMoves(self):
		pokemonContainer = PokemonContainer()
		p = pokemonContainer.GetAllPokemon()
		path = "./static/json/moves.json"
		inputFile = open(path)
		data = json.loads(inputFile.read())
		inputFile.close()
		moves = []

		for x in data['moves']:
			m = self.move()
			for key, value in x.items():
				if key == "id":
					m.id = value
				elif key == 'name':
					m.name = value
				elif key == 'tm':
					m.tm = value
				elif key == 'type':
					m.type = value
				elif key == 'category':
					m.category = value
				elif key == 'power':
					m.power = value
				elif key == 'accuracy':
					m.accuracy = value
				elif key == 'PP':
					m.pp = value
				elif key == 'description':
					m.description = value

			for x in p:
				poke = self.pokemon()
				for y in x.moves:
					if y.name == m.name:
						if y.learn_type == "level up":
							poke.id = x.id
							poke.name = x.name
							poke.lvl = y.level
							poke.hp = x.stats["HP"]
							poke.atk = x.stats["ATK"]
							poke.defs = x.stats["DEF"]
							poke.speed = x.stats["SPE"]
							poke.sp_atk = x.stats["SPA"]
							poke.sp_def = x.stats["SPD"]
							poke.type = x.type
							poke.img = x.imgPath
							m.pokemonLVL.append(poke)
						elif y.learn_type == "machine":
							poke.id = x.id
							poke.name = x.name
							poke.tm = m.tm
							poke.hp = x.stats["HP"]
							poke.atk = x.stats["ATK"]
							poke.defs = x.stats["DEF"]
							poke.speed = x.stats["SPE"]
							poke.sp_atk = x.stats["SPA"]
							poke.sp_def = x.stats["SPD"]
							poke.type = x.type
							poke.img = x.imgPath
							m.pokemonTM.append(poke)

			moves.append(m)

		self.moves = moves

	def ReadAllMoves(self):
		path = "./SomeScrapingData/move_data.txt"
		inputFile = open(path)
		data = json.loads(inputFile.read())
		inputFile.close()
		moves = []

		for x in data['moves']:
			m = self.move()
			for key, value in x.items():
				if key == "id":
					m.id = value
				elif key == 'name':
					m.name = value
				elif key == 'power':
					m.power = value
				elif key == 'accuracy':
					m.accuracy = value
				elif key == 'pp':
					m.pp = value
			moves.append(m)

		self.Allmoves = moves

	def getAllMoves(self):
		return self.Allmoves

	def getMoveByName(self, name):
		for m in self.moves:
			if m.name == name:
				return m