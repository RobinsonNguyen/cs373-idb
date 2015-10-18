
class PokemonContainer:

	class Pokemon:

		def __init__ (self, _id, _name, _type, _egg, _stats, _img):
			self.id = _id
			self.name = _name
			self.type = _type
			self.eggGroup = _egg
			self.stats = _stats
			self.imgPath = _img

	def __init__ (self):
		x = []
		x.append(self.Pokemon(1, 'Bulbasaur', ('Grass', 'Poison'), ('Monster', 'Grass'), { 'HP': 45, 'ATK': 49, 'DEF': 49, 'SPA': 65, 'SPD': 65, 'SPE': 45 }, '001Bulbasaur'))
		x.append(self.Pokemon(2, 'Ivysaur', ('Grass', 'Poison'), ('Monster', 'Grass'), { 'HP': 60, 'ATK': 62, 'DEF': 63, 'SPA': 80, 'SPD': 80, 'SPE': 60 }, '002Ivysaur'))
		x.append(self.Pokemon(3, 'Venusaur', ('Grass', 'Poison'), ('Monster', 'Grass'), { 'HP': 80, 'ATK': 100, 'DEF': 123, 'SPA': 122, 'SPD': 12, 'SPE': 80 }, '003Venusaur'))
		self.pokemon = x

	def GetPokemonById(self, id):
		for p in self.pokemon:
			if p.id is id:
				return p

	def GetAllPokemon(self):
		return self.pokemon