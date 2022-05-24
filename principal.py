#principal.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from dao import ProdutoDao
from produto import Produto

produto_dao = ProdutoDao('bancodados.db')

app = Flask(__name__)
app.secret_key = 'softgraf'

@app.route('/')    #o @ é uma anotação para você inserir as rotas
def index():
    lista = produto_dao.listar()
    return render_template('relatorio.html', title= 'report', products= lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html',titulo='cadastro de produto')

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto = Produto(descricao, preco, quantidade, id)
    produto_dao.salvar(produto)
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    produto = produto_dao.buscar_por_id(id)
    return render_template('editar.html',titulo='editar produto', produto=produto)


@app.route('/deletar/<string:id>')
def deletar(id):
    produto_dao.deletar(id)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = 'usuario logado'
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect(url_for('index'))
    else:
        flash('Senha inválida')
        return redirect(url_for('login'))

if __name__== '__main__':
    app.run(debug=True)

#app.run(debug=True) #debug atualiza automaticamente toda alteração que é feita no código