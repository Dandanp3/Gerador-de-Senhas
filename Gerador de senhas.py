import string
import random

lestras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
spec_caracteres = "!@#$%&*()^"
tod_caracteres = letras_maiusculas + lestras_minusculas + numeros + spec_caracteres
tamanho = 10

continuar = 'S'
while continuar == 'S':
    senha = "".join(random.sample(tod_caracteres, tamanho))
    print(f"Senha gerada: {senha}")

    continuar = str(input('Deseja gerar outra? [S/N]: ')).strip().upper()