Este projeto faz parte de uma atividade acadêmica com o objetivo de estudar e comparar diferentes ORMs do mercado. Esta implementação utiliza **FastAPI** e **SQLAlchemy** (Python) para construir um sistema de gerenciamento de usuários e perfis.

O sistema consiste em um CRUD completo de Usuários, implementando as seguintes regras obrigatórias estabelecidas na atividade:

- [x] **Relacionamento 1:1** (Usuário → Perfil).
- [x] **CRUD completo** de Usuário (Criar, Ler, Atualizar e Deletar).
- [x] Ao criar o usuário, o sistema permite **criar o perfil junto** na mesma requisição (Nested Insert).
- [x] **Validação de Email:** Não é permitido cadastrar um email duplicado no banco de dados.
- [x] **Listagem Conjunta:** Ao listar os usuários, os dados do perfil associado são trazidos na mesma resposta.

- **Python 3**
- **FastAPI:** Framework web moderno e de alta performance.
- **SQLAlchemy:** ORM (Object-Relational Mapper) robusto para manipulação do banco de dados.
- **Pydantic:** Para validação de dados e tipagem estática (Type Hints).
- **SQLite:** Banco de dados relacional leve e embutido (dispensa instalação de servidores externos).
- **Uvicorn:** Servidor ASGI para rodar a aplicação.

Siga os passos abaixo para rodar a API na sua máquina.

### 1. Clonar ou baixar o repositório
Abra o terminal na pasta onde deseja salvar o projeto.

### 2. Criar e ativar o ambiente virtual (Recomendado)
Para isolar as dependências do projeto, crie um ambiente virtual:
```bash
python -m venv venv

### Liberar Sistema

Set-ExecutionPolicy Unrestricted -Scope Process

### Ative o ambiente 

.\venv\Scripts\activate

### Rodar o servidor

uvicorn main:app --reload

