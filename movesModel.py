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
						for k, v in value.items():
							if k == 'name':
								p.name = v
							elif k == 'lvl':
								p.lvl = v
							elif k == 'HP':
								p.hp = v
							elif k == 'attack':
								p.atk = v
							elif k == 'defense':
								p.defs = v
							elif k == 'speed':
								p.speed = v
							elif k == 'sp_atk':
								p.sp_atk = v
							elif k == 'sp_def':
								p.sp_def = v
							elif k == 'type':
								p.type = v
							elif k == 'abilities':
								p.abil = v
							elif k == 'img':
								p.img = v
						m.pokemonLVL.append(p)

					elif key == 'pokemon-byTM':
						for k, v in value.items():
							if k == 'name':
								p.name = v
							elif k == 'tm':
								p.lvl = v
							elif k == 'HP':
								p.hp = v
							elif k == 'attack':
								p.atk = v
							elif k == 'defense':
								p.defs = v
							elif k == 'speed':
								p.speed = v
							elif k == 'sp_atk':
								p.sp_atk = v
							elif k == 'sp_def':
								p.sp_def = v
							elif k == 'type':
								p.type = v
							elif k == 'abilities':
								p.abil = v
							elif k == 'img':
								p.img = v
						m.pokemonTM.append(p)

			moves.append(m)

		self.moves = moves

	def getMoveByName(self, id):
		for m in self.moves:
			if m.id is id:
				return m