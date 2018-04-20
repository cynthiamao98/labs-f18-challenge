from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


@app.route('/pokemon/<input>')
# show the pokemon name corresponding to the pokemon i
def show_pokemon(input):
    if input.isdigit():
        # show the pokemon name corresponding to the pokemon i
        id = input
        address = 'http://pokeapi.co/api/v2/pokemon/' + id
        r = requests.get(address)
        name = r.json()['name']
        return "The pokemon with id " + id + " is " + name
    else:
        # show the pokemon id corresponding to the pokemon name
        name = input
        address = 'http://pokeapi.co/api/v2/pokemon/' + name
        r = requests.get(address)
        id = r.json()['id']
        return "The pokemon with name " + name + " has id " + str(id)
