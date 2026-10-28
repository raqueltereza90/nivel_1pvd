#PDV simples com desconto por idade e por valor da compra

compras = []

print("Bem-vindo ao PDV!")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    #pede o valor
    valor =float(input("Digite o valor da compra: R$ "))

    if valor == 0:
        break

    if valor <0:
        print("Valor inválido. Tente novamente.")
        continue

    #pede a idade
    idade = int(input("Digite a idade do cliente: "))

    if idade < 0:
        print("Idade inválida. Tente novamente.")
        continue

    #calcula o desconto de 20% se tiver 65 anos ou mais
    valor_final = valor
    if idade >=65:
        valor_final = valor_final * 0.8


    #calcula o desconto de 10% se o valor for maior que 100
    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)

    print(f"Valor final da compra: R$ {valor_final:.2f}\n")

    compras.append({"valor": valor, "idade": idade, "valor_final": valor_final})

qtd=len(compras)
total_bruto = 0
total_final = 0

for c in compras:
    total_bruto += c["valor"]
    total_final += c["valor_final"] 

total_desconto = total_bruto - total_final

print("\nResumo das compras:")
print(f"Quantidade de compras: {qtd}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total com desconto: R$ {total_final:.2f}")
print(f"Total de desconto concedido: R$ {total_desconto:.2f}")

