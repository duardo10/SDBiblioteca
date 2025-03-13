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