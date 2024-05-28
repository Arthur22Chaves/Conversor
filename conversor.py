#faça um sistema de conversão de °celsius - °Kelvin
#Temperatura-kelvin = Temperatura-celsius + 273,15
print('Conversor de temperatura')
celsius = 1
kelvin = 2
Opçao = int(input("informe a opção 1 para converter para celsius ou opção 2 para kelvin. "))
print (f'Você escolheu a opção {Opçao}°.')
temperatura = float(input("Digite a temperatura: ")) 

#condição
if Opçao == 1 :
    temperatura = kelvin - 273.15
    print (f'{temperatura} ° Celsius')
elif Opçao == 2 :
    temperatura = temperatura + 273.15
    print (f'{temperatura} ° kelvin')
else:
    print ('Opção Inválida!')