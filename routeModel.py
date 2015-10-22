import json

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
			self.rates = ""

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
		routeData = json.loads(open("./static/json/routes.json").read())
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
					newPokemon = self.wildPokemon()
					for val in value:
						if 'name' in val:
							newPokemon.name = val['name']
						if 'img' in val:
							newPokemon.img = val['img']
						if 'area' in val:
							newPokemon.area = val['area']
						if 'levels' in val:
							newPokemon.levels = val['levels']
						if 'rates' in val:
							newPokemon.rates = val['rates']
					newRoute.pokemon.append(newPokemon)
				if key == "trainers":
					newTrainer = self.trainer()
					for val in value:
						if 'name' in val:
							newTrainer.name = val['name']
						if 'area' in val:
							newTrainer.area = val['area']
						if 'pokemon' in val:
							newTrainerPokemon = self.trainerPokemon()
							for v in val["pokemon"]:
								if "name" in v:
									newTrainerPokemon.name = v["name"]
								if "img" in v:
									newTrainerPokemon.img = v["img"]
								if "level" in v:
									newTrainerPokemon.level = v["level"]
							newTrainer.pokemon.append(newTrainerPokemon)
					newRoute.trainers.append(newTrainer)
				if key == "items":
					newItem = self.item()
					for val in value:
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
		print(region)
		print(name)
		for r in self.routes:
			if r.region == region and r.name == name:
				return r