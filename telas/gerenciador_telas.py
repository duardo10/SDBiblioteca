# gerenciador_telas.py - Gerencia a troca de telas sem criar importações circulares

def get_tela_login():
    from telas.login import tela_login
    return tela_login

def get_tela_cadastro():
    from telas.cadastro import tela_cadastro
    return tela_cadastro

def get_tela_principal():
    from telas.principal import tela_principal
    return tela_principal

def get_tela_cadastro_livro():
    from telas.cadastro_livro import tela_cadastro_livro
    return tela_cadastro_livro

def get_tela_editar_livro():
    from telas.editar_livro import tela_editar_livro
    return tela_editar_livro

def get_tela_pesquisar_livros():
    from telas.pesquisar_livros import tela_pesquisar_livros
    return tela_pesquisar_livros
