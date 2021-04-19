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


# O que foi feito
* Configuração, .env
* Templates, arquivos estáticos
* Models, migrations, seed
* Inserção de professores
* Alteração de professores
* Exclusão de professores + modal de confirmação
* Pesquisa de professores + filtro + paginação
* Autenticação: login + logout + verificação

# TODO:
* [x] Logs
* [x] Recuperação de dados
* Models que tem regras de negócio
* Esqueci a senha (SMTP)

* Models que são somente CRUD
* Verificar a pesquisa com filtro e paginação
* Perfil
* Módulos
