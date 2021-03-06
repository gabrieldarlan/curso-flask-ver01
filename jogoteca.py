from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alura'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return self.nome


jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Assassins Creed', 'Ação', 'PC')
jogo3 = Jogo('Batman', 'Ação', 'Xbox S')
jogo4 = Jogo('Halo', 'FPS', 'Xbox S')
lista = [jogo1, jogo2, jogo3, jogo4]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f"{request.form['usuario']} logou com sucesso!")
        return redirect('/')
    else:
        flash('Não logado')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect('/')


app.run(debug=True)
