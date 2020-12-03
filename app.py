from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Book, Categoria, Tematicas, Titulos

if __name__ == '__main__':
    app.run()

livrosArray = [];
categorias = [];
tematicas = [];
titulos = [];

@app.route('/')
def home():  
    return render_template('home.html')

@app.route('/livros')
def livros():
    livrosDba = Book.query.all()
    categorias = Categoria.query.all()
    return render_template('livros.html', livros=livrosDba,categorias = categorias)

@app.route('/buscar-livros', methods=['POST'])
def buscarLivros():
    categorias = Categoria.query.all()

    if(request.form['categoria_id'] == 'todos'):
        livros = Book.query.all();
    else:
        livros = Book.query.filter((Book.categoria_id == request.form['categoria_id'])).all();

    return render_template('livros.html', livros=livros, categorias = categorias)

@app.route('/categorias')
def indexCategorias():
    categoriasDba = Categoria.query.all()
    print(categoriasDba)
    return render_template('categorias.html', categorias = categoriasDba)

@app.route('/tematicas')
def indexTematicas():
    tematicasDba = Tematicas.query.all()
    print(tematicasDba)
    return render_template('tematicas.html', tematicas = tematicasDba)

@app.route('/titulos', methods=['GET'])
def indexCadastrarTitulos():
    titulos = Titulos.query.all()
    print(titulos)
    return render_template('titulos.html', titulos = titulos)

@app.route('/deletar-titulo', methods=['POST', 'GET'])
def deletarTitulo():
    db.session.delete(Titulos.query.filter_by(id=request.form['tituloDelete']).first())
    db.session.commit()
    titulos = Titulos.query.all()
    print(titulos)
    return render_template('titulos.html', titulos = titulos)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if "submit_button" in request.form:
            if ((request.form['username'] == 'Marcos') and (request.form['password'] == '123456')):
                print("Login realizado com sucesso!")
                return home()
            else:
                return render_template('login.html') 
    return render_template('login.html')

@app.route('/cadastrar-livro', methods=['POST', 'GET'])
def cadastrar_livro():
    if request.method == 'POST':
        if "submit_button" in request.form:
            titulo = request.form['titulo']
            autor = request.form['autor']
            ano = request.form['ano']
            editora = request.form['editora']
            categoria_id = request.form['categoria_id']
            tematica_id = request.form['tematica_id']
            podeAlugar = False

            if request.form.get('alugar'):
                podeAlugar = True    

            db.session.add(Book(autor, titulo, ano, editora, podeAlugar, False, categoria_id, tematica_id))
            db.session.commit()
            return livros()
    else:
        categorias = Categoria.query.all()
        tematicas = Tematicas.query.all()
        return render_template('cadastro-livro.html', categorias = categorias, tematicas = tematicas)

@app.route('/cadastrar-categoria', methods=['POST', 'GET'])
def cadastrar_categoria():
    if request.method == 'POST':
        if "submit_button" in request.form:
            nome = request.form['categoria']
        
            categorias.append(Categoria(nome))
            categoria = Categoria(nome)
            db.session.add(categoria)
            db.session.commit()
            return indexCategorias()
    else:
        return render_template('cadastro-categoria.html')

@app.route('/cadastrar-tematica', methods=['POST', 'GET'])
def cadastrar_tematica():
    if request.method == 'POST':
        if "submit_button" in request.form:
            tema = request.form['tematica']
        
            tematicas.append(Tematicas(tema))
            tematica = Tematicas(tema)
            db.session.add(tematica)
            db.session.commit()
            return indexTematicas()
    else:
        return render_template('cadastro-tematicas.html')

@app.route('/cadastrar-titulo', methods=['POST', 'GET'])
def cadastrar_titulo():
    if request.method == 'POST':
        if "submit_button" in request.form:
            titulo = request.form['titulos']
        
            titulos.append(Titulos(titulo))
            titulo_save = Titulos(titulo)
            db.session.add(titulo_save)
            db.session.commit()
            return render_template('cadastrar-titulos.html')
    else:
        return render_template('cadastrar-titulos.html')