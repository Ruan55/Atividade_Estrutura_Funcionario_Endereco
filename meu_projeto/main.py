from models.enums.Setor import Setor
from models.enums.Sexo import Sexo
from models.enums.UnidadeFederativa import UnidadeFederativa
from models.Funcionario import Funcionario
from models.Endereco import Endereco
import os

os.system("cls || clear")

funcionario1 = Funcionario(3123, "Ruan", "2342342", "264465", "3223", "04/08/2002", Sexo.MASCULINO, Setor.ENGENHARIA, 6565, "3333-5555", "fsasd@gmail.com", Endereco("Rua K", "5", "N/A", "33223", "Salvador", UnidadeFederativa.BAHIA))

print(funcionario1)