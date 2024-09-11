from models.enums.Setor import Setor
from models.enums.Sexo import Sexo
from models.Endereco import Endereco
import os

os.system("cls || clear")

class Funcionario:
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, datanascimento: str, sexo: Sexo, setor: Setor, salario: float, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.datanascimento = datanascimento
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"\n Id: {self.id}"
               f"\n Nome: {self.nome}"
               f"\n Cpf: {self.cpf}"
               f"\n Rg: {self.rg}"
               f"\n Matricula: {self.matricula}"
               f"\n Data de Nascimento: {self.datanascimento}"
               f"\n Sexo: {self.sexo.value}"
               f"\n Setor: {self.setor.value}"
               f"\n Salário: {self.salario}"
               f"\n Telefone: {self.telefone}"
               f"\n Email: {self.email}"
               f"\n Endereço: {self.endereco}")
    
    