distance = float(input('Qual a distância de sua viagem? '))

# simplefied if statement
cost = distance * 0.50 if distance <= 200 else distance * 0.45

print(f'O custo da sua viagem vai ser de R${format(cost, ".2f")}')

