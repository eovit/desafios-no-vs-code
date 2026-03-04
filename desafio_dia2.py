numero = (float(input("Digite 1* número: ")))

maior = numero 

for i in range(2):
    
    numero = float(input(f"Digite o {i+2}* número: "))

    if numero > maior:
        maior = numero 

print("O maior número é:", maior)
