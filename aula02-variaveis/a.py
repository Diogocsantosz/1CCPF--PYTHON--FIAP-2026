from docutils.io import Input

print("ola mundo")

print (7 + 4)
print("7 + 4")
print("7" + "4")# concatenação de strings

# comentario de 1 linha

'''
comentarios 
mútiplas 
linhas 

'''
#varíaveis
nome = "diogo"
idade = 19
peso = 85.0
print(nome, idade, peso)
print(F"ola, {nome}!")

#input -- simula forms no cmd
nome = input("digite seu nome: ")
idade = int (input("digite sua idade: "))
peso = float(input("digite seu peso: "))

print(nome, idade, peso)

# desafio

nome = input("digite seu nome")
print("boas vindas!" ,nome)

"""
dia
mês 
ano

"""
#desafio

dia = input("digite seu dia de aniversario: ")
mês = input("digite seu mês de aniversario: ")
ano = input("digite seu ano de aniversario: ")

print(dia, mês, ano )