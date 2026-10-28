# PVD Bonus com desconto por idade, valor , quantidade e cupom

compras = []

print("---Bem-vindo ao PDV(bônus)!---")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    valor = float(input("Digite o valor da compra: R$ "))

    if valor == 0:
        break

    if valor <0:
        print("Valor inválido. Tente novamente.")
        continue

    idade = int(input("Digite a idade do cliente: "))

    if idade < 0:
        print("Idade inválida. Tente novamente.")
        continue

    quantidade = int(input("Digite a quantidade de produtos: "))

    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue

    cupom = input("Digite o cupom de desconto (ou pressione Enter para nenhum): ").strip().upper()

    valor_final = valor


    # 20% de desconto se tiver 65 anos ou mais
    if idade >= 65:
        valor_final *= 0.8

    # 10% de desconto se o valor for maior que 100
    if valor_final > 100:
        valor_final *= 0.9

    # bônus 1: mais de 3 itens ganha 5% extra
    if quantidade > 3:
        valor_final = valor_final * 0.95

    # bônus 2: cupom de fidelidade ganha 10% extra
    if cupom == "FIDELIDADE10":
        valor_final = valor_final * 0.9
    elif cupom != "":
        print("Cupom inválido, ignorando.")
        cupom = ""
 
    valor_final = round(valor_final, 2)
 
    print(f"Valor final: R$ {valor_final:.2f}\n")
 
    compras.append({"valor": valor, "idade": idade, "quantidade": quantidade, "cupom": cupom, "final": valor_final})


    qtd = len(compras)
    total_bruto = 0
    total_final = 0

    for c in compras:
        total_bruto += c["valor"]
        total_final += c["final"]

    total_desconto = total_bruto - total_final

    print("\nResumo das compras:")
    print(f"Quantidade de compras: {qtd}")
    print(f"Total bruto: R$ {total_bruto:.2f}")
    print(f"Total com desconto: R$ {total_final:.2f}")
    print(f"Total de desconto concedido: R$ {total_desconto:.2f}")

    arquivo = open("resump.txt", "w", encoding="utf-8")
    arquivo.write("Resumo das compras:\n")

    numero = 1
    for c in compras:
        arquivo.write(f"Compra {numero}: Valor: R$ {c['valor']:.2f}, Idade: {c['idade']}, Quantidade: {c['quantidade']} itens, Cupom: {c['cupom']}, Valor final: R$ {c['final']:.2f}\n")
        numero += 1

    arquivo.write(f"\nQuantidade de compras: {qtd}\n")
    arquivo.write(f"Total bruto: R$ {total_bruto:.2f}\n")
    arquivo.write(f"Total com desconto: R$ {total_final:.2f}\n")
    arquivo.write(f"Total de desconto concedido: R$ {total_desconto:.2f}\n")
    arquivo.close()

    print("\nResumo das compras salvo em 'resumo.txt'.")