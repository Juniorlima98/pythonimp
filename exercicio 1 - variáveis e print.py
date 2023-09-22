
coca_qtd = 150
pepsi_qtd = 130
valor_unt_coca = 1.50
valor_unt_pepsi = 1.50
custo_loja = 2500.00


faturamento_coca = coca_qtd * valor_unt_coca
faturamento_pepsi = pepsi_qtd * valor_unt_pepsi
custo_loja = 2500
lucro_loja = faturamento_coca + faturamento_pepsi - custo_loja

print ("O faturamento da venda de Pepsi esse mês foi :", faturamento_pepsi)
print ("O faturamento da venda de Coca esse mês foi :", faturamento_coca)
print ("O faturamento liquido da loja esse mês foi de :", lucro_loja)


print("teste alteração")