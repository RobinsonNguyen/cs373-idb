from flask import Flask, render_template
from models import Pokemon

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#======================================================================#

@app.route('/pokemon/')
def pokemon_id():
	return render_template('pokemon.html')

@app.route('/pokemon/<int:id>')
def pokemon(id):
	
	return render_template('pokemon_details.html')

#======================================================================#

@app.route('/trainer')
def trainer():
    return 'Trainer Page'
    #return render_template('index.html')

@app.route('/trainer/<int:id>')
def trainer_id(id):
    return 'Trainer ' + str(id) +  ' Page'
    #return render_template('index.html')

#======================================================================#

@app.route('/move')
def move():
    return 'Move Page'
    #return render_template('index.html')

@app.route('/move/<int:id>')
def move_id(id):
    return 'move ' + str(id) +  ' Page'
    #return render_template('index.html')

#======================================================================#

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/location/<int:id>')
def location_id(id):
    return 'Location ' + str(id) +  ' Page'
    #return render_template('index.html')




if __name__ == '__main__':
    app.run(debug = True)