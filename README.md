# Sistema de Cadastro de Livros da Biblioteca

Este projeto é um sistema de cadastro de livros utilizando Python com interface gráfica (GUI) e armazenamento no Firebase.

## Estrutura do Projeto

- `telas/`: Contém os arquivos relacionados às telas da interface gráfica do usuário.
- `venv/`: Ambiente virtual para gerenciamento de dependências do projeto.
- `config.py`: Arquivo de configuração do firebase.
- `firebase_service.py`: Contém os serviços para interação com o Firebase.
- `main.py`: Arquivo principal para iniciar a aplicação.
- `README.md`: Documentação do projeto.
- `requirements.txt`: Lista de dependências do projeto.
- `.gitignore`: Arquivo para ignorar arquivos desnecessários no versionamento.
- `LICENSE`: Arquivo de licença do projeto.

## Requisitos

- Python 3.x
- Conta no Firebase

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/biblioteca.git
   cd biblioteca
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o Firebase:
   - Crie um projeto no Firebase.
   - Adicione um banco de dados Firestore.
   - Baixe o arquivo de configuração `google-services.json` e coloque-o na pasta `src/database/`.

5. Criar e configurar um projeto no Firebase
   - Acesse Firebase Console.
- Clique em "Criar um projeto" e siga as instruções.
- No menu lateral, vá até Build > Firestore Database.
- Clique em Criar banco de dados e selecione o modo produção ou teste conforme sua necessidade.
- No menu lateral, vá até Configurações do projeto (ícone ⚙️).
- Vá até a aba Contas de serviço e clique em Gerar nova chave privada.
- Um arquivo JSON será baixado (google-services.json).
- Mova esse arquivo para a pasta do projeto: src/database/.
  
6️.  Configurar o arquivo config.py
No arquivo `config.py`, adicione as credenciais do Firebase:

```python
import pyrebase 

firebaseConfig = {
    'apiKey': "AIzaSyCcKoowTWge7vtVIkSsT_Dj13fHXZM3_zs",
    'authDomain': "sistemasdistribuidos-e8eaf.firebaseapp.com",
    'databaseURL': "https://sistemasdistribuidos-e8eaf-default-rtdb.firebaseio.com",
    'projectId': "sistemasdistribuidos-e8eaf",
    'storageBucket': "sistemasdistribuidos-e8eaf.firebasestorage.app",
    'messagingSenderId': "34064682324",
    'appId': "1:34064682324:web:61ebb87c80e40748edccc1"
}
```

# 📸 Telas do Sistema

Esta seção apresenta as telas principais do **Sistema de Cadastro de Livros da Biblioteca**, descrevendo suas funcionalidades e incluindo imagens ilustrativas.

---

## 🖥️ Tela de Login

### 📌 Descrição:
A tela de login permite que os usuários entrem no sistema utilizando um **e-mail e senha cadastrados**.

### 🔹 Funcionalidades:
- Campo para **e-mail**.
- Campo para **senha**.
- Botão **Entrar** para autenticação.
- Botão **Cadastrar-se** para novos usuários.

### 🖼️ Imagem:
![Tela de Login](https://github.com/seu-usuario/biblioteca/blob/main/assets/login.png)

---

## 📝 Tela de Cadastro

### 📌 Descrição:
A tela de cadastro permite a criação de uma nova conta no sistema.

### 🔹 Funcionalidades:
- Campos para **e-mail** e **senha**.
- Botão **Cadastrar** para concluir o registro.

### 🖼️ Imagem:
![Tela de Cadastro](https://github.com/seu-usuario/biblioteca/blob/main/assets/cadastro.png)

---

## ✏️ Tela de Edição de Livro

### 📌 Descrição:
A tela de edição permite que o usuário **modifique** as informações de um livro previamente cadastrado.

### 🔹 Funcionalidades:
- Campos para **título**, **autor**.
- Botão **Salvar alterações** para atualizar os dados.
- Botão **Excluir livro** para remover do banco de dados.

### 🖼️ Imagem:
![Tela de Edição](https://github.com/seu-usuario/biblioteca/blob/main/assets/edicao.png)

---

## 🔍 Tela de Pesquisa de Livro

### 📌 Descrição:
A tela de pesquisa permite que o usuário **busque** por livros cadastrados na biblioteca.

### 🔹 Funcionalidades:
- Botão **Pesquisar** para buscar os resultados.
- Lista de livros correspondentes à busca.

### 🖼️ Imagem:
![Tela de Pesquisa](https://github.com/seu-usuario/biblioteca/blob/main/assets/pesquisa.png)

---


## Execução

Para iniciar a aplicação, execute:
```bash
python src/app.py
```

## Contribuidores

Luis Eduardo Silva Brito
Francisco Aparício
Victor Macêdo


## Licença

Este projeto está sob a licença MIT.
