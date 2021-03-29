from app import db
from app.models.tables import Professor
import bcrypt

senha_plana = "SuportE99"
senha_encriptada = bcrypt.hashpw(senha_plana.encode('UTF-8'), bcrypt.gensalt())

p1 = Professor(nome="Marco Andrade", email="marco.andrade@ifro.edu.br", senha=senha_encriptada)
p2 = Professor(nome="Maria Oliveira", email="maria.olivera@ifro.edu.br", senha=senha_encriptada)
p3 = Professor(nome="Eduardo Silva", email="eduardo.silva@ifro.edu.br", senha=senha_encriptada)
p4 = Professor(nome="José Silva", email="jose.silva@ifro.edu.br", senha=senha_encriptada)
p5 = Professor(nome="Julia Oliveira", email="julia.oliveira@ifro.edu.br", senha=senha_encriptada)
p6 = Professor(nome="José Teixeira", email="jose.teixeira@ifro.edu.br", senha=senha_encriptada)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)

db.session.commit()