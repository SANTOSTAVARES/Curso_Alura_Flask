from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['God of War', 'The Last of Us', 'FIFA 2022', 'GTA V']
    return render_template('lista.html', titulo='Jogos', jogos=lista) #Por padrão, o Flask procura o arquivo na pasta 'templates'.

#app.run(host='0.0.0.0', port=8000) #esta definição de rota, não deve ser utilizada em produção.
app.run()