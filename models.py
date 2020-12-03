from app import db
from sqlalchemy.dialects.postgresql import JSON

class Book(db.Model):
  __tablename__ = 'books'

  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String())
  autor = db.Column(db.String())
  ano = db.Column(db.String())
  editora = db.Column(db.String())
  categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
  categoria = db.relationship('Categoria')
  tematica_id = db.Column(db.Integer, db.ForeignKey('tematicas.id'))
  tematica = db.relationship('Tematicas')
  pode_alugar = db.Column(db.Boolean, default = True)
  alugado = db.Column(db.Boolean, default = True)

  def __init__(self, autor, titulo, ano, editora, pode_alugar, alugado, categoria_id, tematica_id):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.editora = editora
    self.pode_alugar = pode_alugar
    self.alugado = alugado
    self.categoria_id = categoria_id
    self.tematica_id = tematica_id

class Usuarios(db.Model):
  __tablename__= 'usuarios' 

  id = db.Column(db.Integer, primary_key=True)
  usuario = db.Column(db.String())
  senha = db.Column(db.String())   

  def __init__(self, usuario, senha):
    self.usuario = usuario
    self.senha = senha

class Categoria(db.Model):
  __tablename__='categoria'

  id = db.Column(db.Integer, primary_key=True)
  categoria = db.Column(db.String())

  def __init__(self, name):
    self.categoria = name

class Tematicas(db.Model):
  __tablename__='tematicas'

  id = db.Column(db.Integer, primary_key=True)
  tematica = db.Column(db.String())

  def __init__(self, tema):
    self.tematica = tema
  
class Titulos(db.Model):
  __tablename__='titulos'

  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String())

  def __init__(self, titulo):
    self.titulo = titulo
  


