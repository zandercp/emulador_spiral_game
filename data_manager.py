# data_manager.py
# Gerencia o carregamento e salvamento do estado do jogo e histórico de partidas em arquivos JSON.

import json
import os

class DataManager:
    def __init__(self, estado_jogo_path, historico_partidas_path):
        self.estado_jogo_path = estado_jogo_path
        self.historico_partidas_path = historico_partidas_path
        # Assegura a criação dos arquivos JSON se eles não existirem.
        self._create_file_if_not_exists(estado_jogo_path, {"jogador": {}, "labirinto": {}})
        self._create_file_if_not_exists(historico_partidas_path, {"partidas": []})

    def _create_file_if_not_exists(self, filepath, default_data):
        # Cria um arquivo com dados padrão se o arquivo não existir.
        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                json.dump(default_data, file, indent=4)

    def save_game_state(self, data):
        with open(self.estado_jogo_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_game_state(self):
        try:
            with open(self.estado_jogo_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Retorna estado padrão se o arquivo não existir (deve ser raro após a inicialização).
            return {"jogador": {}, "labirinto": {}}

    def save_historico_partidas(self, partidas):
        with open(self.historico_partidas_path, 'w') as file:
            json.dump({"partidas": partidas}, file, indent=4)

    def load_historico_partidas(self):
        try:
            with open(self.historico_partidas_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Retorna uma lista vazia de partidas se o arquivo não existir.
            return {"partidas": []}
