'''Atividade: Notas
➔ O QUE FAZER?
● Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 
verificações e a média dos exercícios que fazem parte da avaliação.
Calcular a média de aproveitamento, usando a fórmula:
○ MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
● A atribuição de conceitos obedece a tabela ao lado
Ao fim, informar:
● O conceito do aluno e; 
● Se ele foi aprovado (A, B, C) ou reprovado (D, E)

Média Conceito
>9,0 A
7,5 e < 9,0 B
6,0 e < 7,5 C
4,0 e < 6,0 D
< 4,0 '''

while ("sair" != "sim"):

    print()
    print("-"*40)
    id_num = int(input("Digite o número de identificação: "))
    print()
    nota1 = float(input("Digite a primeira nota: "))
    print()
    nota2 = float(input("Digite a segunda nota: "))
    print()
    nota3 = float(input("Digite a terceira nota: "))
    print()
    me = float(input("Digite a media dos exercícios: "))
    print()
    ma = (nota1 + (nota2 * 2) + (nota3 * 3) + me )/7
    print("-"*40)
    print()
    if (ma > 9):
        print("ID: {:.0f}, Nota {:.2f}, Media (A), aprovado.".format(id_num, ma))
        sair = input("Deseja sair? sim ou não")
        
    elif (ma >= 7.5 and ma < 9):
        print("ID: {:.0f}, Nota {:.2f}, Media (B), aprovado.".format(id_num, ma))
        sair = input("Deseja sair? sim ou não")
        
    elif (ma >= 6 and ma < 7.5):
        print("ID: {:.0f}, Nota {:.2f}, Media (C), aprovado.".format(id_num, ma))
        print("Deseja sair? sim ou não.")
        sair = input()
    elif (ma >= 4 and ma < 6):
        print("ID: {:.0f}, Nota {:.2f}, Media (D), reprovado.".format(id_num, ma))
        print("Deseja sair? sim ou não.")
        sair = input()
        
    elif (ma >= 4 and ma < 6):
        print("ID: {:.0f}, Nota {:.2f}, Media (D), reprovado.".format(id_num, ma))
        print("Deseja sair? sim ou não.")
        sair = input()
        
    else:
        print("Erro: Digite as notas de 0 a 10.")
        print("Deseja sair? sim ou não.")
        sair = input()