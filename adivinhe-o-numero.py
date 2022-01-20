print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = 42
total_de_tentativas = 3
for rodada in range (1, total_de_tentativas+1):
    print('Rodada {} de {}' .format(rodada, total_de_tentativas))
    chute_do_usuario = input('Digite o seu número ')
    print('Você digitou o número:', chute_do_usuario, sep=' ')
    chute = int(chute_do_usuario)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    if(acertou):
        print('Você acertou')
    elif(maior):
        print('Você errou, seu chute foi maior que o número secreto')
    else:
        print('Você errou, seu chute foi menor que o número secreto')
    print('Fim de jogo!')
