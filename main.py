from flask import Flask, render_template, abort, request, jsonify
from models import PokemonContainer, Moves, RouteContainer
from flask.ext.sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pokemon@localhost/pokemasters'
db = SQLAlchemy(app)

pokemonContainer = PokemonContainer()
moveContainer = Moves()
routeContainer = RouteContainer()

@app.route('/')
def index():
    return render_template('index.html')

#=====================Pokemon==========================================#

@app.route('/pokemon/')
def pokemon_id():
    pokemon = pokemonContainer.GetAllPokemon()
    return render_template('pokemon.html', pokemon=pokemon)

@app.route('/pokemon/<name>/')
def pokemon(name):
    pokemon = pokemonContainer.GetPokemonByName(name)
    if pokemon is None:
        abort(404)
    return render_template('pokemon_details.html', pokemon=pokemon)

#=============API==========#
@app.route('/api/v1.0/pokemon/', methods=['GET'])
def get_pokemon():
    return jsonify({'pokemon': 'test'})

@app.route('/api/v1.0/pokemon/<int:id>/', methods=['GET'])
def get_pokemon_id(id):
    return jsonify({'pokemon': 'test'})

@app.route('/api/v1.0/pokemon', methods=['POST'])
def create_pokemon():
    if not request.json:
        abort(400)

    return jsonify({'pokemon': 'test'}), 201

@app.route('/api/v1.0/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    if not request.json:
        abort(400)
    return jsonify({'pokemon': 'test'})

@app.route('/api/v1.0/pokemon/<int:id>', methods=['DELETE'])
def delete_task(id):
    return jsonify({'result': True})

#======================================================================#

@app.route('/about/')
def about():
    return render_template('about.html')

#======================================================================#

@app.route('/moves/<name>/')
def move(name):
    move = moveContainer.getMoveByName(name)
    if move is None:
        abort(404)
    print(move.pp)
    return render_template('moves.html', move=move)

@app.route('/moves/')
def move_id():
	moves = moveContainer.getAllMoves()
	return render_template('allMoves.html', moves=moves)

#=============API==========#
@app.route('/api/v1.0/moves/', methods=['GET'])
def get_moves():
    return jsonify({'moves': 'test'})

@app.route('/api/v1.0/moves/<int:id>/', methods=['GET'])
def get_moves_id(id):
    return jsonify({'moves': 'test'})

@app.route('/api/v1.0/moves/', methods=['POST'])
def create_moves():
    if not request.json:
        abort(400)

    return jsonify({'moves': 'test'}), 201

@app.route('/api/v1.0/moves/<int:id>/', methods=['PUT'])
def update_moves(id):
    if not request.json:
        abort(400)
    return jsonify({'moves': 'test'})

@app.route('/api/v1.0/moves/<int:id>/', methods=['DELETE'])
def delete_moves(id):
    return jsonify({'result': True})

#======================================================================#

@app.route('/location/')
@app.route('/location', methods=['GET'])
def location_id():
    if request.args.get("region") is not None and request.args.get("name") is not None:
        route = routeContainer.getRouteByRegion(request.args.get("region"), request.args.get("name"))
        if route is None:
            abort(404)
        return render_template("route_data.html", route=route)
    return render_template('location.html')

#=============API==========#
@app.route('/api/v1.0/locations/', methods=['GET'])
def get_locations():
    return jsonify({'locations': 'test'})

@app.route('/api/v1.0/locations/<int:id>/', methods=['GET'])
def get_locations_id(id):
    return jsonify({'locations': 'test'})

@app.route('/api/v1.0/locations/', methods=['POST'])
def create_locations():
    if not request.json:
        abort(400)

    return jsonify({'locations': 'test'}), 201

@app.route('/api/v1.0/locations/<int:id>/', methods=['PUT'])
def update_locations(id):
    if not request.json:
        abort(400)
    return jsonify({'locations': 'test'})

@app.route('/api/v1.0/locations/<int:id>/', methods=['DELETE'])
def delete_locations(id):
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)