from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

    def __init__(self, nome: str) -> None:
        self.nome = nome