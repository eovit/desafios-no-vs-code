#sinceramente eu expliquei tanto na outra forma de fazer que aqui eu to com preguiça, tira foto daquele la mesmo

maior = None

for i in range(5):
    numero = float(input(f"digite o {i+1} número: "))

    if maior is None or numero > maior:
        maior = numero 

print("O maior número é:", maior)