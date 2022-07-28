speed = float(input('Qual é a velocidade atual do carro? '))

if speed > 80:
    print('MULTADO! Vocẽ excedeu o limite permitido que é de 80km/h')
    ticket = (speed - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(ticket))

print('Tenha um bom dia! Dirija com segurança!')

