from translate import Translator
x = Translator(from_lang="english",to_lang="pt-br")
trad = x.translate(str(input("Informe o que vai ser traduzido: \n")))
print(trad)
while True:
    y = int(input("\nQuer continuar traduzindo? Aperte 1 para (Sim) e 0 para (Não): "))
    if y == 1:
        x = Translator(from_lang="english", to_lang="pt-br")
        trad = x.translate(str(input("\nInforme o que vai ser traduzido: \n")))
        print(trad)
    else:
        break
