preco_normal = float(input("Digite o preço normal do produto: R$ "))

print("\nFORMAS DE PAGAMENTO:")
print("[ 1 ] À vista no dinheiro ou cheque (15% de desconto)")
print("[ 2 ] À vista no cartão (8% de desconto)")
print("[ 3 ] Em até 2x no cartão (Preço normal)")
print("[ 4 ] 3x ou mais no cartão (25% de juros)")

opcao = int(input("\nQual é a opção de pagamento? "))

if opcao == 1:
    preco_final = preco_normal * 0.85
    print(f"Pagamento à vista no dinheiro/cheque recebeu 15% de desconto.")
elif opcao == 2:
    preco_final = preco_normal * 0.92
    print(f"Pagamento à vista no cartão recebeu 8% de desconto.")
elif opcao == 3:
    preco_final = preco_normal
    parcela = preco_final / 2
    print(f"Pagamento em 2x sem juros. Valor da parcela: R$ {parcela:.2f}")
elif opcao == 4:
    preco_final = preco_normal * 1.25
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = preco_final / total_parcelas
    print(f"Pagamento em {total_parcelas}x com 25% de juros.")
    print(f"Valor da parcela: R$ {parcela:.2f}")
else:
    preco_final = preco_normal
    print("Opção inválida de pagamento. Preço normal aplicado.")

print(f"O produto que custava R$ {preco_normal:.2f} vai custar R$ {preco_final:.2f} no final.")
