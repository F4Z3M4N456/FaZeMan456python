valor=str(input("ingrese un valor"))
objetos=[]
while valor != "FIN" :
  valor=str(input("ingrese un valor")) 
  objetos.append(valor)
objetos.remove ("FIN")
print(objetos)
