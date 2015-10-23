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
		inputFile = open(path)
		data = json.loads(inputFile.read())
		inputFile.close()
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

		path = "./static/json/move_data.json"
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
				elif key == 'pp':
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

		path = "./static/json/move_data.json"
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

class RouteContainer:

	class item:
		def __init__(self):
			self.name = ""
			self.area = ""
			self.description = ""

	class trainer:
		def __init__(self):
			self.name = ""
			self.area = ""
			self.pokemon = []

	class trainerPokemon:
		def __init__(self):
			self.name = ""
			self.img = ""
			self.level = ""

	class wildPokemon:
		def __init__(self):
			self.name = ""
			self.img = ""
			self.area = ""
			self.levels = ""
			self.rate = ""

	class route:
		def __init__(self):
			self.region = ""
			self.name = ""
			self.prevRoute = ""
			self.nextRoute = ""
			self.routeImg = ""
			self.routeDesc = ""
			self.pokemon = []
			self.trainers = []
			self.items = []

	def __init__(self):
		self.readInRoutes()

	def readInRoutes(self):
		inputFile = open("./static/json/routes.json")
		routeData = json.loads(inputFile.read())
		inputFile.close()
		routes = []

		for r in routeData["routes"]:
			newRoute = self.route()
			for key, value in r.items():
				if key == "region":
					newRoute.region = value
				if key == "name":
					newRoute.name = value
				if key == "prevRoute":
					newRoute.prevRoute = value
				if key == "nextRoute":
					newRoute.nextRoute = value
				if key == "routeImg":
					newRoute.routeImg = value
				if key == "routeDesc":
					newRoute.routeDesc = value
				if key == "wildPokemon":
					for val in value:
						newPokemon = self.wildPokemon()
						if 'name' in val:
							newPokemon.name = str(val['name'])
						if 'img' in val:
							newPokemon.img = val['img']
						if 'area' in val:
							newPokemon.area = val['area']
						if 'levels' in val:
							newPokemon.levels = val['levels']
						if 'rate' in val:
							newPokemon.rate = val['rate']
						newRoute.pokemon.append(newPokemon)
				if key == "trainers":
					for val in value:
						newTrainer = self.trainer()
						if 'name' in val:
							newTrainer.name = val['name']
						if 'area' in val:
							newTrainer.area = val['area']
						if 'pokemon' in val:
							for v in val["pokemon"]:
								newTrainerPokemon = self.trainerPokemon()
								if "name" in v:
									newTrainerPokemon.name = v["name"]
								if "img" in v:
									newTrainerPokemon.img = v["img"]
								if "level" in v:
									newTrainerPokemon.level = v["level"]
								newTrainer.pokemon.append(newTrainerPokemon)
						newRoute.trainers.append(newTrainer)
				if key == "items":
					for val in value:
						newItem = self.item()
						if "name" in val:
							newItem.name = val["name"]
						if "area" in val:
							newItem.area = val["area"]
						if "description" in val:
							newItem.description = val["description"]
						newRoute.items.append(newItem)
			routes.append(newRoute)
		self.routes = routes;

	def getRouteByRegion(self, region, name):
		for r in self.routes:
			if r.region == region and r.name == name:
				return r