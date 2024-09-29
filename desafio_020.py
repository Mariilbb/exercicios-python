# Um professor quer sortear a ordem de apresentação de trabalho de seus 4 alunos. Leia o nome dos alunos e mostre a ordem sorteada

from random import shuffle

nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print(f"A ordem dos alunos escolhidos foi: {lista}")