palavra=("Cavalo")
for i in range(len(palavra)):
    letra=input("Digite uma letra")
    if letra in palavra[0] or letra in palavra[1] or letra in palavra[2] or letra in palavra[3] or letra in palavra[4] or letra in palavra[5]:
        print("tem")
    else:
        print("Não tem")


