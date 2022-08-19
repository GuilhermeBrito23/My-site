from flask import Flask, render_template
import pokemon
import passgen
import advinha_game

app = Flask(__name__)


@app.route('/pokemon', methods=['GET', 'POST'])
def poke():
    return pokemon.pokedex()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/passgen', methods=['GET', 'POST'])
def gera_senha():
    return passgen.GeraSenha()


@app.route('/guess-game', methods=['GET', 'POST'])
def adivinha_game():
    return advinha_game.adivinha_game_func()


if __name__ == '__main__':
    app.run(debug=True)
