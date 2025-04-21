# 🔐 Sistema de Cadastro e Login com SQLAlchemy

Este projeto em Python simula um sistema de cadastro e autenticação de usuários. Utiliza SQLite como banco de dados e SQLAlchemy como ORM (Object Relational Mapper), além de aplicar criptografia nas senhas com o módulo `hashlib`.

---

## 📁 Estrutura do Projeto

📂 cadastro-login-sqlalchemy  
│  
├── models.py          # Definição da tabela Pessoa  
├── controller.py      # Regras de negócio (Cadastro e Login)  
├── main.py            # Interface em linha de comando (CLI)  
├── projeto2.db        # Banco de dados SQLite gerado automaticamente  
└── README.md          # Documentação do projeto  

---

## 🧠 Tecnologias Utilizadas

- Python 3.12.5  
- SQLAlchemy  
- SQLite  
- Programação Orientada a Objetos (POO)  
- Criptografia com hashlib (SHA256)  

---

## 📌 Classes Modeladas

### 🧍 Pessoa  
```python
Pessoa(id: int, nome: str, email: str, senha: str)
```

---

## 🛠️ Funcionalidades

- ✅ Cadastro de usuários com validações
- ✅ Verificação de e-mails já cadastrados
- ✅ Criptografia de senha com SHA256
- ✅ Login de usuário com autenticação segura
- ✅ Mensagens de erro específicas para facilitar a usabilidade

---

## 🧪 Exemplos de Uso

### ✅ Cadastrar novo usuário:
```python
resultado = ControllerCadastro.cadastrar("Maria", "maria@email.com", "senha123")
```

### ✅ Fazer login:
```python
resultado = ControllerLogin.login("maria@email.com", "senha123")
```

### 📋 Interface de Menu no `main.py`
```bash
==========[Menu]==========
Digite 1 para cadastro
Digite 2 para Logar
Digite 3 para sair
```

---

## 💡 Validações Aplicadas

- Nome: entre 3 e 50 caracteres
- Email: até 200 caracteres
- Senha: entre 6 e 100 caracteres
- Email deve ser único no banco

---

## ⚙️ Melhorias Futuras

- Criar interface gráfica com Tkinter ou Web com Flask
- Implementar confirmação de e-mail
- Adicionar recuperação de senha
- Incluir testes automatizados
- Expandir funcionalidades com níveis de acesso

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. **(Opcional) Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install sqlalchemy
```

4. **Execute o projeto:**
```bash
python main.py
```
