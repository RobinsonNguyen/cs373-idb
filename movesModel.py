import json

class Moves:

	class move:

		def __init__(self):
			self.name = ""
			self.type = ""
			self.category = ""
			self.power = ""
			self.accuracy = ""
			self.pp = ""
			self.description = ""

	def __init__(self):
		self.ReadMoves()

	def ReadMoves(self):
		path = "./static/json/moves.json"

		data = json.loads(open(path).read())

		moves = []

		for x in data['moves']:
			m = self.move()
			for key, value in x:
				if key == 'name':
					m.name = value
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
				else:
					m.description = value
			moves.append(m)

		self.moves = moves

	def getMoveByName(self, name):
		for m in self.moves:
			if m.name is name:
				return m