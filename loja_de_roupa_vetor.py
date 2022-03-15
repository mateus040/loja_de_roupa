print("Bem-Vindo ao EtecStore")

nome = input("Digite o nome do cliente: ")

valor_total_compra = 0

add_mais_produtos = 'S'

i = 0


nome_roupa = []
valor_unitario = []
quantidade = []
valor_roupa_vendida = []

while add_mais_produtos == 'S':

    nome_roupa.append(str(input("Digite o nome da roupa: ")))
    valor_unitario.append(float(input("Digite o valor unitário: ")))
    quantidade.append(int(input("Digite a quantidade: ")))


    valor_roupa_vendida.append(valor_unitario[i] * quantidade[i])
    valor_total_compra = valor_total_compra + valor_roupa_vendida[i]

    
    add_mais_produtos = str(input("Deseja Vender mais Roupa (S/N)")).upper()
    i += 1
    if (add_mais_produtos == 'N'):
        break


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
for j in range(0, i):
    print(' ')
    print("Roupa Vendida: ", nome_roupa[j])
    print("Valor Unitário: %.2f "% valor_unitario[j])
    print("Quantidade: ", quantidade[j])
    print("Valor Final: %.2f "% valor_roupa_vendida[j])
    print(' ')
   

   
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("PAGAMENTO")
print("A compra ficou em: R$ %.2f "% valor_total_compra)
pgto_cliente = float(input("Digite o valor pago pelo cliente: "))

if (pgto_cliente > valor_total_compra):
    troco = pgto_cliente - valor_total_compra
    print("Seu troco é de R$ %.2f "% troco)
else:
    if (pgto_cliente < valor_total_compra):
        print("Valor Insuficiente")
        fiado = valor_total_compra - pgto_cliente
        print("Você ficará devendo: R$ %.2f "% fiado)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Obrigado volte sempre")




