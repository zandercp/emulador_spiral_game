# characters.py
# Define as classes e funcionalidades relacionadas aos personagens do jogo.

class Personagem:
    def __init__(self, nome, tipo, dados_de_vida):
        self.nome = nome
        self.tipo = tipo
        self.dados_de_vida = dados_de_vida
        self.inventario = []

    def adicionar_ao_inventario(self, item):
        self.inventario.append(item)

# Esta função pode ser expandida para incluir lógica específica de criação de personagens,
# habilidades especiais, etc.
def criar_personagem(nome, tipo, dados_de_vida):
    return Personagem(nome, tipo, dados_de_vida)
