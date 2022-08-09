#Este programa crea columnas segun lo pida el usuario

anashe=int(input("Ingrese la cantidad de columnas"))
print("Patrones seeesh")
for x in range (0, anashe):
  for y in range (0, x+1):
    print( "# ", end="")
  print() 
  #Realmente es muy simple, nada mas se debe crear un contador y un rango que pida al usuario de 0 a cuantos numeros creara la columna, luego de esto nada mas hay que colocar un print que nos diga que es lo que queremos mostrar, en este caso= #
