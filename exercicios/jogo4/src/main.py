# O que é um Tuple:
# Tuple: Coleçao de dados que estao ordenados e sao inalteraveis, usado para armazenar dados relacionados (mini struct ou mini classe)


def main():
    voos = []
    voo = ("Numero", "origem", "destino", "hora partida")
    print("Bem-vindo ao grande software da TAP")
    print("Pretende adicionar um voo?")
    resposta = input()
    if resposta == "S":
        num = int(input("Digite um numero: "))
        origem = input("Digite a origem: ")
        destino = input("Digite o destino")
        hora = input("Digite a hora de partida")
        novo_voo = (num, origem, destino, hora)
        voos.append(novo_voo)
    else:
        print("ok")

    for voo in voos:
        print(f"{voo[0]},{voo[1]},{voo[2]},{voo[3]}")


if __name__ == "__main__":
    main()
