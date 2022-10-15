# Calculo de IMC - Índice de Massa Corporal
'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:
'''

# MENOR QUE 18,5    MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE

print("Olá!")
print("Bem vindo a Calculadora de Índice de Massa Corporal - IMC\n")

nome = (input("Qual seu nome? "))
altura = float(input("Digite sua Altura em cm: "))
peso = float(input("Digite seu Peso em kg: "))

imc = peso / (altura / 100)**2

print("\n")

print(nome, " seu índice de Massa Corporal é: %.4f" % imc)

if imc < 18.5:
    print("Sua classificação é de Magreza")

elif imc >= 18.5 and imc < 24.9:
    print("Sua classificação é Normal")

elif imc >= 25.0 and imc < 29.9:
    print("Sua classificação é de Sobrepeso I")

elif imc >= 29.9 and imc < 30.0:
    print("Sua classificação é de Sobrepeso II")

else:
    print("Sua classificação é de Sobrepeso Grave III")

print("\n")

print("Obrigado por utilizar nosso aplicativo. Volte sempre!")
