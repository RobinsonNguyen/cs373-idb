from flask import Flask, render_template, abort
from models import PokemonContainer
from movesModel import Moves

app = Flask(__name__)

pokemonContainer = PokemonContainer()
moveContainer = Moves()

@app.route('/')
def index():
    return render_template('index.html')

#======================================================================#

@app.route('/pokemon/')
def pokemon_id():
    pokemon = pokemonContainer.GetAllPokemon()
    return render_template('pokemon.html', pokemon=pokemon)

@app.route('/pokemon/<int:id>')
def pokemon(id):
    pokemon = pokemonContainer.GetPokemonById(id)
    if pokemon is None:
        abort(404)
    return render_template('pokemon_details.html', pokemon=pokemon)

#======================================================================#

# @app.route('/trainer')
# def trainer():
#     return 'Trainer Page'
#     #return render_template('index.html')

# @app.route('/trainer/<int:id>')
# def trainer_id(id):
#     return 'Trainer ' + str(id) +  ' Page'
#     #return render_template('index.html')

#======================================================================#

@app.route('/moves/<int:id>')
def move(id):
    move = moveContainer.getMoveByName(id)
    print(move.pp)
    return render_template('moves.html', move=move)    #return render_template('index.html')

@app.route('/moves')
def move_id():
	moves = moveContainer.getAllMoves()
	return render_template('allMoves.html', move=moves)
    #return render_template('index.html')

#======================================================================#

# @app.route('/location')
# def location():
#     return render_template('location.html')

# @app.route('/location/<int:id>')
# def location_id(id):
#     return 'Location ' + str(id) +  ' Page'
#     #return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)