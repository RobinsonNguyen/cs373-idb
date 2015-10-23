import json

class PokemonContainer:

	class Move:
		def __init__(self):
			self.name = ""
			self.learn_type = ""
			self.level = ""
			self.tm = ""

	class Evolution:
		def __init__(self):
			self.to = ""
			self.method = ""
			self.level = 0
			
	class Location:
		def __init__(self):
			self.method = ""
			self.game = ""

	class Pokemon:
		def __init__ (self):
			self.id = 0
			self.name = ""
			self.type = ()
			self.eggGroup = ()
			self.stats = {}
			self.imgPath = ""
			self.moves = []
			self.evolution = []

	def __init__ (self):
		self.ReadPokemonData()

	def GetPokemonById(self, id):
		for p in self.pokemon:
			if p.id is id:
				return p
	def GetPokemonByName(self, name):
		for p in self.pokemon:
			if p.name == name:
				return p

	def GetAllPokemon(self):
		return self.pokemon

	def ReadPokemonData(self):
		x = []

		path = "./static/json/pokemon_data_fixed_names.json"
		data = json.loads(open(path).read())
		pokeList = data['pokemon']

		for poke in pokeList:
			p = self.Pokemon()
			for key, value in poke.items():
				if key == 'pkdx_id':
					p.id = value
				if key == 'name':
					p.name = value
					p.imgPath = value + '_regular_.png'
				if key == 'hp':
					p.stats['HP'] = value
				if key == 'attack':
					p.stats['ATK'] = value
				if key == 'defense':
					p.stats['DEF'] = value
				if key == 'sp_atk':
					p.stats['SPA'] = value
				if key == 'sp_def':
					p.stats['SPD'] = value
				if key == 'speed':
					p.stats['SPE'] = value
				if key == 'types':
					types = []
					for t in value:
						for k, v in t.items():
							if k == 'name':
								types.append(v)
					p.type = types
				if key == 'egg_groups':
					egg_groups = []
					for e in value:
						for k, v in e.items():
							if k == 'name':
								egg_groups.append(v)
					p.eggGroup = egg_groups
				if key == 'moves':
					moves = []
					for m in value:
						move = self.Move()
						for k, v in m.items():
							if k == 'name':
								move.name = v
							if k == 'learn_type':
								move.learn_type = v
							if k == 'level':
								move.level = v
						moves.append(move)
					p.moves = moves
				if key == 'locations':
					locations = []
					for l in value:
						location = self.Location()
						for k, v in l.items():
							if k == 'game':
								move.name = v
							if k == 'method':
								move.learn_type = v
						locations.append(location)
					p.locations = locations
				if key == 'evolutions':
					evolution = []
					for e in value:
						evo = self.Evolution()
						for k, v in e.items():
							if k == 'method':
								if v == 'level_up':
									evo.method = 'Level Up'
								if v == 'trade':
									evo.method = 'Trade'
								if v == 'stone':
									evo.method = 'Stone'
							if k == 'to':
								evo.to = v
						evolution.append(evo)
					p.evolution = evolution

			x.append(p)
		self.pokemon = x