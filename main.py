from flask import Flask, render_template, abort, request, jsonify
from models import *

import subprocess

# -----
# index
# -----
@app.route('/')
def index():
    return render_template('index.html')

# --------
# about
# --------	
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/v1.0/tests/', methods=['GET'])
def get_test_results():
    script = subprocess.Popen("make test", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        out, errs = script.communicate()
    except:
        script.kill()
    return jsonify({'results': out.decode() })
	
# --------
# location
# --------	 
'''
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
'''
	
# -------
# pokemon
# -------
@app.route('/pokemon/')
@app.route('/pokemon/<name>/')
def pokemon(name=None):
    if name is not None:
        return render_template('pokemon_details.html', pokemon=Pokemon.get(name))
    return render_template('pokemon.html', pokemon=Pokemon.get_all())
	
#=============API==========#

@app.route('/api/v1.0/pokemon/', methods=['GET'])
def get_pokemon():
    pokemon = Pokemon.get_all()
    poke_list = []
    for poke in pokemon:
        poke_list.append({c.name: getattr(poke, c.name) for c in poke.__table__.columns})
    return jsonify({'pokemon': poke_list})

@app.route('/api/v1.0/pokemon/<int:id>/', methods=['GET'])
def get_pokemon_id(id):
    pokemon = Pokemon.get_id(id)
    poke_dic = {c.name: getattr(pokemon, c.name) for c in pokemon.__table__.columns}
    return jsonify({'pokemon': poke_dic})

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

# -----
# moves
# -----
@app.route('/moves')
@app.route('/moves/<name>')
def moves(name=None):
	if name is not None:
		return render_template('moves.html', move=Move.get(name))
	# change name of the above html to move and the below one to moves
	return render_template('allMoves.html', moves=Move.get_all())

#=============API==========#
'''
#@app.route('/api/v1.0/moves/', methods=['GET'])
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
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)