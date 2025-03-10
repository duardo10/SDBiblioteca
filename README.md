# Sistema de Cadastro de Livros da Biblioteca

Este projeto é um sistema de cadastro de livros utilizando Python com interface gráfica (GUI) e armazenamento no Firebase.

## Estrutura do Projeto

- `src/gui/`: Contém a interface gráfica do usuário.
- `src/database/`: Contém a configuração e serviços para interação com o Firebase.
- `src/models/`: Contém os modelos de dados.
- `src/controllers/`: Contém a lógica de controle para operações CRUD.
- `src/app.py`: Arquivo principal para iniciar a aplicação.

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