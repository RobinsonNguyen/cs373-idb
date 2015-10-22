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
				elif key == 'pp':
					m.pp = value
				elif key == 'description':
					m.description = value
				else:
					p = self.pokemon()
					if key == 'pokemon-byLVL':
						for k in value:
							if 'name' in k:
								p.name = k['name']
							elif 'lvl' in k:
								p.lvl = k['lvl']
							elif 'HP' in k:
								p.hp = k['HP']
							elif 'attack' in k:
								p.atk = k['attack']
							elif 'defense' in k:
								p.defs = k['defense']
							elif 'speed' in k:
								p.speed = k['speed']
							elif 'sp_atk' in k:
								p.sp_atk = k['sp_atk']
							elif 'sp_def' in k:
								p.sp_def = k['sp_def']
							elif 'type' in k:
								p.type = k['type']
							elif 'abilities' in k:
								p.abil = k['abilities']
							elif 'img' in k:
								p.img = k['img']
						m.pokemonLVL.append(p)

					elif key == 'pokemon-byTM':
						for k in value:
							if 'name' in k:
								p.name = k['name']
							elif 'tm' in k:
								p.lvl = k['tm']
							elif 'HP' in k:
								p.hp = k['HP']
							elif 'attack' in k:
								p.atk = k['attack']
							elif 'defense' in k:
								p.defs = k['defense']
							elif 'speed' in k:
								p.speed = k['speed']
							elif 'sp_atk' in k:
								p.sp_atk = k['sp_atk']
							elif 'sp_def' in k:
								p.sp_def = k['sp_def']
							elif 'type' in k:
								p.type = k['type']
							elif 'abilities' in k:
								p.abil = k['abilities']
							elif 'img' in k:
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