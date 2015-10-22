import json

class Moves:

	class pokemon:

		def __init__(self):
			self.name = ""
			self.lvl = ""
			self.tm = ""
			self.img = ""
			self.hp = ""
			self.atk = ""
			self.defs = ""
			self.speed = ""
			self.sp_atk = ""
			self.sp_def = ""
			self.type = ""
			self.abil = ""


	class move:

		def __init__(self):
			self.id = 0
			self.name = ""
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
		path = "./static/json/moves.json"

		data = json.loads(open(path).read())

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
				else:
					p = self.pokemon()
					if key == 'pokemon-byLVL':
						for k in value:
							if 'name' in k:
								p.name = k['name']
							if 'lvl' in k:
								p.lvl = k['lvl']
							if 'HP' in k:
								p.hp = k['HP']
							if 'attack' in k:
								p.atk = k['attack']
							if 'defense' in k:
								p.defs = k['defense']
							if 'speed' in k:
								p.speed = k['speed']
							if 'sp_atk' in k:
								p.sp_atk = k['sp_atk']
							if 'sp_def' in k:
								p.sp_def = k['sp_def']
							if 'type' in k:
								p.type = k['type']
							if 'abilities' in k:
								p.abil = k['abilities']
							if 'img' in k:
								p.img = k['img']
						m.pokemonLVL.append(p)

					elif key == 'pokemon-byTM':
						for k in value:
							if 'name' in k:
								p.name = k['name']
							if 'tm' in k:
								p.lvl = k['tm']
							if 'HP' in k:
								p.hp = k['HP']
							if 'attack' in k:
								p.atk = k['attack']
							if 'defense' in k:
								p.defs = k['defense']
							if 'speed' in k:
								p.speed = k['speed']
							if 'sp_atk' in k:
								p.sp_atk = k['sp_atk']
							if 'sp_def' in k:
								p.sp_def = k['sp_def']
							if 'type' in k:
								p.type = k['type']
							if 'abilities' in k:
								p.abil = k['abilities']
							if 'img' in k:
								p.img = k['img']
						m.pokemonTM.append(p)

			moves.append(m)

		self.moves = moves

	def ReadAllMoves(self):
		path = "./SomeScrapingData/move_data.txt"

		data = json.loads(open(path).read())

		moves = []

		for x in data['moves']:
			m = self.move()
			for key, value in x.items():
				if key == "id":
					m.id = value
				elif key == 'name':
					m.name = value
			moves.append(m)

		self.Allmoves = moves

	def getAllMoves(self):
		return self.Allmoves

	def getMoveByName(self, id):
		for m in self.moves:
			if m.id is id:
				return m