n1=int(input("Ingrese un numero"))
n2=int(input("Ingrese un numero"))
n3=int(input("Ingrese un numero"))
n4=int(input("Ingrese un numero"))
n5=int(input("Ingrese un numero"))
n6=int(input("Ingrese un numero"))
n7=int(input("Ingrese un numero"))
n8=int(input("Ingrese un numero"))
n9=int(input("Ingrese un numero"))
non=int(input("Ingrese un numero"))
#Aqui le pedimos al usuario que ingrese los numeros que se van a operar
numeros=[n1, n2, n3, n4, n5, n6, n7, n8, n9, non]
res=numeros[-1] + numeros[0]
mon=numeros[-2] + numeros[1] + numeros[2] + numeros[3] + numeros[4] + numeros[5] + numeros[6] + numeros[7]
#Aqui es donde empieza el procedimiento, agregamos las posiciones -1 y 0 para sumarlos, luego el segundo numero lo sumamos hasta el penultimo con las posiciones restantes
print(res)
print(mon)
print(numeros)
#y tan solo hacvemos print de los resultados
