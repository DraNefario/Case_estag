# Sistema de Gerenciamento de Usuários e Métricas

Sistema web em Flask para gerenciamento de usuários e métricas, com autenticação e controle de acesso por roles.

---

## Funcionalidades

- Autenticação de usuários (login/logout).  
- Controle de roles (ex: admin / usuário normal).  
- Listagem e filtragem de métricas com paginação.  
- Proteção de rotas sensíveis via login e roles.  
- Senhas armazenadas de forma segura (hash).

---

## Tecnologias

- Python 3.x  
- Flask  
- Flask-Login  
- SQLAlchemy  
- Pandas  
- Banco de dados compatível com SQLAlchemy (SQLite, PostgreSQL ou MySQL)

---

## Instalação

1. Clone o repositório:  
```bash
git clone <https://github.com/DraNefario/Case_estag>
cd <Case_estag>
```

2.Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
---

## Configuração

Configure o banco de dados em app/models/db.py (variável SQLALCHEMY_DATABASE_URI).

Ajuste SECRET_KEY no arquivo app/__init__.py para produção.

---

## Como Rodar

```bash
# Linux/macOS
export FLASK_APP=app/run.py
flask run

# Windows
set FLASK_APP=app/run.py
flask run
```
Acesse: http://localhost:8080/

---

## Estrutura de Pastas
```bash
Case_Estag/
├─ app/
│  ├─ controllers/      # Lógica de rotas
│  ├─ models/           # Modelos de banco de dados
│  ├─ statiic/          # CSS
│  ├─ templates/        # HTML
│  ├─ utils/            # Funções utilitárias (decorators, criação de DB)
│  └─ __init__.py       # Cria a aplicação Flask
└─ run.py               # Arquivo principal para rodar a aplicação
```

---
## Usuários
- Role "admin": acesso completo às métricas e funcionalidades.

- Role "user": acesso limitado, algumas colunas sensíveis não aparecem.

---
## Notas de Segurança

- Senhas são armazenadas com hash (Werkzeug).

- Rotas protegidas com @login_required.

- Controle de acesso via has_role.









