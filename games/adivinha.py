import random


def jogar():
    nome = input("Digite seu nome:  ")
    espaço = "***********************"
    print(espaço)

    print("Ola Bem-vindo " , nome)
    print(espaço)

    nivel = int(input("Qual seu nivel 1(easy) 2(medium) 3(hard) ?"))
    print(espaço)
    if(nivel == 1):
        total_tentativas = 9

    elif(nivel == 2):
        total_tentativas = 6

    if(nivel == 3):
        total_tentativas = 3

    else: 
        total_tentativas = 1

    pontos = 1000

    tentativa = 1


    for rodada in range(1, total_tentativas + 1):

        print("tentativa {} de {}".format(tentativa, total_tentativas))

        
        numero_random = random.randrange(1, 101)
        chute = input("Digite seu chute de 1 a 100: ")
        numero_chutado = int(chute)
        print(espaço)

        if(chute < 1 or chute > 100):
            print("digite um numero entre 1 e 100")
            continue


        print("Seu chute foi:" , chute , " e está:")
        print(espaço)

        if(numero_chutado == numero_random):
            valor = "acertou e seus pontos foram {}".format(pontos)
            print(valor)
            print(espaço)
            break
            pass

        else:
            
            if(numero_chutado < numero_random):
                valor = "Errado, chute menor que numero random"
                print(valor)
                print(espaço)
                pass
            
            elif(numero_chutado > numero_random):
                valor = "Errado ,chute maior que numero random"
                print(valor)
                print(espaço)
                pass

            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_random, pontos))
            
            pontos_perdidos = abs(numero_chutado - numero_random)
            pontos = pontos - pontos_perdidos

        tentativa = tentativa + 1

if(__name__ == "__main__"):
    jogar()