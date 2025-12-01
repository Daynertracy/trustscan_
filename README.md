# TRUSTSCAN – Sistema Inteligente de Avaliação de Sites, Produtos e Confiabilidade Online

O **TRUSTSCAN** é um sistema completo desenvolvido em Python, estruturado com princípios sólidos de **POO (Programação Orientada a Objetos)**, oferecendo um conjunto de ferramentas para análise de segurança de sites, cadastro e autenticação de usuários, e busca simulada de produtos por imagem.

Este projeto inclui:

* **API completa com FastAPI**
* **Sistema de Login e Registro** com criptografia *bcrypt*
* **Banco de Dados** estruturado com SQLAlchemy (ORM)
* **Analisador de Sites** com verificação de:

  * Certificado SSL
  * Informações WHOIS
  * Índice automático de confiabilidade
* **Busca por imagem** (IA simulada)
* **Arquitetura modular** dividida em camadas (models, services, controllers)
* Aplicação dos pilares da POO:

  * **Abstração**: Interfaces e classes base organizadas
  * **Encapsulamento**: Acesso seguro a atributos e métodos internos
  * **Herança**: Serviços que expandem comportamentos reutilizáveis
  * **Polimorfismo**: Implementações flexíveis entre serviços da aplicação

---

## 🚀 Objetivo do Projeto

O TRUSTSCAN foi criado com foco em oferecer uma API moderna capaz de:

* Ajudar usuários a identificarem sites suspeitos
* Centralizar avaliações de segurança online
* Simular busca de produtos utilizando imagem
* Demonstrar um exemplo real de arquitetura limpa usando **Python + OOP + FastAPI**

---

## 🧱 Estrutura do Projeto

O projeto é dividido em módulos independentes conforme boas práticas de engenharia de software:

```
trustscan/
│── app.py                # Arquivo principal da API
│── models/               # ORM e tabelas do banco
│── services/             # Regras de negócio
│── controllers/          # Rotas e endpoints
│── core/                 # Configurações gerais
│── utils/                # Funções auxiliares
└── README.md             # Este arquivo
```

---

## 🔐 Autenticação e Segurança

O sistema utiliza o **Passlib (bcrypt)** para hashing seguro de senha.
Todas as operações sensíveis usam validações internas de segurança e proteção de dados.

---

## 🛠 Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* SQLAlchemy ORM
* Passlib (bcrypt)
* Uvicorn
* WhoIs / SSL

---

## ▶️ Como Executar o Projeto

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute a aplicação:

```bash
uvicorn app:app --reload
```

3. Acesse a documentação automática da API:

```
http://localhost:8000/docs
```

---

## 📌 Status

O projeto está funcional e estruturado para expansão. Pode ser integrado com:

* IA real para reconhecimento de imagem
* Dashboard frontend
* Sistema de relatórios
* Autenticação JWT

---

## 🏁 Contribuições

Sinta-se à vontade para sugerir melhorias ou solicitar novos módulos!

---

**TRUSTSCAN — Sua segurança digital começa aqui.** 🔒
