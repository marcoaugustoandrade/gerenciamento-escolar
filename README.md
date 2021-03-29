## Configuração inicial
pipenv --three
pipenv shell
pipenv install Flask Flask-SQLAlchemy Flask-Script Flask-Migrate pymysql python-dotenv

## Migrations
python3 migrations.py db init
python3 migrations.py db migrate
python3 migrations.py db upgrade


professores (id, nome, email, senha)
disciplinas (id, nome, calculo)
alunos (id, nome, email, senha)

professores_disciplinas (id, professor_id, disciplina_id)

etapas (id, disciplina_id, descricao)
notas (id, aluno_id, etapa_id, nota)

Autenticação
Melhorar a paǵina de listagem: formulário para buscar, paginação
Logs
Módulos (Blueprint)