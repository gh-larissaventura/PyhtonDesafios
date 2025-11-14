while True:
    n = int(input("Digite um número: "))

    antecessor = n - 1
    sucessor = n + 1

    print(f"Analisando o valor {n}, seu antecessor é {antecessor} e o sucessor é {sucessor}.")

    continuar = input("Quer testar outro número? [S/N] ").strip().upper()

    if continuar == "N":
        print("Encerrando o programa. Até mais!")
        break


