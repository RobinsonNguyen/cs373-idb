from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#======================================================================#

@app.route('/pokemon/')
def pokemon_id():
	#return render_template('index.html')
    return 'Pokemon Page'

@app.route('/pokemon/<int:id>')
def pokemon(id):
	#return render_template('index.html')
    return 'Pokemon ' + str(id) +  ' Page'

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

@app.route('/route')
def route():
    return 'Route Page'
    #return render_template('index.html')

@app.route('/route/<int:id>')
def route_id(id):
    return 'route ' + str(id) +  ' Page'
    #return render_template('index.html')




if __name__ == '__main__':
    app.run(debug = True)