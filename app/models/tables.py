from app import db
from flask_login import UserMixin

class Professor(db.Model, UserMixin):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(200), nullable=False)

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymouse(self):
        return False

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def __repr__(self):
        return '<Professor %s>' % self.nome


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    calculo = db.Column(db.String(20), nullable=False, default="soma")


class ProfessorDisciplina(db.Model):
    __tablename__ = 'professores_disciplinas'

    # id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), primary_key=True)


class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(200), nullable=False)


class Etapa(db.Model):
    __tablename__ = 'etapas'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))
    descricao = db.Column(db.String(200), nullable=False)


class Nota(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'))
    etapa_id = db.Column(db.Integer, db.ForeignKey('etapas.id'))
    nota = db.Column(db.Float, nullable=False)