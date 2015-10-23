from flask import Flask, render_template, abort, request
from models import PokemonContainer, Moves, RouteContainer

app = Flask(__name__)

pokemonContainer = PokemonContainer()
moveContainer = Moves()
routeContainer = RouteContainer()

@app.route('/')
def index():
    return render_template('index.html')

#======================================================================#

@app.route('/pokemon/')
def pokemon_id():
    pokemon = pokemonContainer.GetAllPokemon()
    return render_template('pokemon.html', pokemon=pokemon)

@app.route('/pokemon/<name>')
def pokemon(name):
    pokemon = pokemonContainer.GetPokemonByName(name)
    if pokemon is None:
        abort(404)
    return render_template('pokemon_details.html', pokemon=pokemon)

#======================================================================#

@app.route('/about/')
def about():
    return render_template('about.html')

# @app.route('/trainer/<int:id>')
# def trainer_id(id):
#     return 'Trainer ' + str(id) +  ' Page'
#     #return render_template('index.html')

#======================================================================#

@app.route('/moves/<name>')
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



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)