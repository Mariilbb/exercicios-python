# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que leia o nome e escreva o escolhido

from random import choice

nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")

lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)

print(f"O aluno escolhido foi: {escolhido}")


