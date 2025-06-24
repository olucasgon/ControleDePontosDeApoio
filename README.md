# 🛰️ API de Controle de Pontos de Apoio

Sistema RESTful desenvolvido para o gerenciamento de Pontos de Apoio, Pessoas, e seus respectivos registros de entrada e saída. Ideal para monitoramento logístico, situações de emergência ou controle de acesso a estruturas de apoio em campo.

---

## 📌 Funcionalidades

- 📍 **Pontos de Apoio**
  - Cadastro com localização (latitude, longitude) e capacidade
  - Listagem, edição e remoção
- 👤 **Pessoas**
  - Registro de dados pessoais com validações (e-mail, CPF, etc)
  - Relacionamento com registros de entrada/saída
- 🕒 **Registro de Entradas e Saídas**
  - Armazena horário de entrada e saída
  - Relacionado a uma pessoa e um ponto de apoio
- 🔎 **Filtros e Buscas**
  - Busca por nome, CPF, datas e localizações específicas
- 🛡️ **Validações completas**
  - Dados obrigatórios
  - Formatos corretos
  - Respostas padronizadas em caso de erro

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia         | Descrição                                |
|--------------------|--------------------------------------------|
| 🐍 Python + Flask  | Framework web leve e eficiente             |
| 📦 Flask-RESTful   | Para construção de APIs REST               |
| 📄 Marshmallow     | Validação e serialização de dados          |
| 🐘 PostgreSQL      | Banco de dados relacional robusto          |
| 🐍 SQLAlchemy      | ORM para facilitar acesso ao banco         |
| 📘 Swagger + Flask-APISpec | Documentação automática da API   |

---

## 🛠️ Como Rodar Localmente

1. **Clone o projeto**
   ```bash
   git clone https://github.com/olucasgon/ControleDePontosDeApoio
   cd ControleDePontosDeApoio
   
