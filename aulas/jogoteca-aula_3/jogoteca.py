from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/') #Em página inicial utiliza somente '/'
def index():
    return render_template('lista.html', titulo='Jogos para jogar', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',]) #O Flask tem como método padrão o GET, por isso, é preciso especificar o POST
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True) #O parâmetro 'debug', funciona serve para o servidor após estar ativo, considerar as atualizações nos arquivos, sem precisar ficar reiniciando o servidor.