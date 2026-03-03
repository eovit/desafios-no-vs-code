

n1 = float(input("Digite o 1* número: ")) #aqui eu to só fazendo o comando padrão pra digitar no terminal


maior = n1 #aqui eu determino a váriavel "maior" como n1

for i in range(4): #e também falo pra máquina que ela vai ler "i" (que é número) por uma quantidade finita (range)
    
    numero = float(input(f"Digite o {i+2}* número: ")) #essa parte determina que o texto vai se repertir pela quantidade de vezes descrita em range ({i+2})
    
    if numero > maior: #se "numero" for maior (>) que "maior", transforma "numero" em "maior" 
        maior = numero

#tendo em mente que ela sempre começa a ler em 0, então eu coloco um máximo de 4, (4) na frente de range 


print("O maior número é:", maior ) #aqui eu mando a máquina te mostrar qual é o maior número, com a variável "maior"