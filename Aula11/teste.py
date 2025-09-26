import json
import os

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "ano": self.ano}


class Biblioteca:
    def __init__(self, arquivo="biblioteca.json"):
        self.arquivo = arquivo
        self.livros = []
        self.carregar()

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.livros = [Livro(**l) for l in dados]
        else:
            self.salvar()  # cria o arquivo vazio logo de cara

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4, ensure_ascii=False)


# Teste rápido
if __name__ == "__main__":
    print("Livro salvo! Confira o arquivo biblioteca.json.")
