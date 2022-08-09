#Menu de mcdonalds be like:
#Final boss incoming
a1=1
numerodeordenesrecibidas=0
sinl=0
sint=0
sinte=0
combo=0
sincombo=0
papas=0
aros=0
porcentajesinl=0
porcentajesincomb=0
porcentajecombo=0
porcentajepapa=0
porcentajearo=0
#declaramos contadores para que se sumen cada vez que se cumplan las condiciones(con o sin papas)
while a1 != "fin":
  a9=str(input("Tomando orden, seleccione lo que desea en su hamburguesa escriba 1 para comenzar"))
  hamburguesa = ["Torta de carne", "Torta de carne extra", "Tocino", "Lechuga", "Tomate", "Cebolla", "Mayonesa", "Mostaza", "Ketchup"]
  acompanamientos=["Papas", "Aros de cebolla"]
  bebidas=["CocaCola", "Sprite", "Pepsi", "7Up"]
  if a9 == "1":
    n=int(input(hamburguesa[0]))
    k=int(input(hamburguesa[1]))
    q=int(input(hamburguesa[2]))
    f=int(input(hamburguesa[3]))
    u=int(input(hamburguesa[4]))
    r=int(input(hamburguesa[5]))
    d=int(input(hamburguesa[6]))
    v=int(input(hamburguesa[7]))
    c=int(input(hamburguesa[8]))
  m1=str(input("La hamburguesa esta lista, desea acompanamientos?"))
  #esta parte en resumen, es la creacion de listas para poder acceder a los elementos dentro de ellas luego, ademas de asignarles posicion para que hagan un print uno por uno los elementos
  numerodeordenesrecibidas=numerodeordenesrecibidas+1
  if m1== "1":
    n1=int(input(acompanamientos[0]))
    n2=int(input(acompanamientos[1]))
    m5=str(input("Desea agregar bebida?"))
    if m5 == "1":
      f1=int(input(bebidas[0]))
      f2=int(input(bebidas[1]))
      f3=int(input(bebidas[2]))
      f4=int(input(bebidas[3]))
  print("esta seria la orden final:")
  #las otras 2 listas a las cuales buscamos acceder luego, al ser los acompanamientos, tendran que ser precisos porque si se seleccionan, tendran que aumentar los contadores
  o=ordenfinal=[n, k, q, f, u, r, d, v, c , n1, n2, f1, f2, f3, f4]
  print(o)
  if f == 0:
    sinl = sinl+1
  if u == 0:
    sint = sint+1
  if k ==0:
    sinte=sinte+1
  if n1 or n2 == 0 and f1 or f2 or f3 or f4 == 0:
    sincombo=sincombo+1
  else:
   combo=combo+1
  if n1 == 1:
    papas=papas+1
  if n2 == 1:
    aros =aros+1
  #esta parte es para ver las ordenes que disponen de ciertos elementos especificos como el numero de tortas extra
  a1=str(input("Desea tomar otra orden?"))
else:
 print("A continuacion, tendra los detalles de su orden")
porcentajesinl= (sinl*100/numerodeordenesrecibidas)
porcentajesint= (sint*100/numerodeordenesrecibidas)
porcentajesinte= (sinte*100/numerodeordenesrecibidas)
porcentajesincomb= (sincombo*100/numerodeordenesrecibidas)
porcentajecombo= (combo*100/numerodeordenesrecibidas)
porcentajepapa= (papas*100/numerodeordenesrecibidas)
porcentajearo= (aros*100/numerodeordenesrecibidas)
ff=str(input("Ingrese su Usuario"))
print(porcentajesinl)
print(porcentajesint)
print(porcentajesinte)
print(porcentajesincomb)
print(porcentajecombo)
print(porcentajepapa)
print(porcentajearo)
print(" muchas gracias ",ff,"tenga un buen dia")
#la parte final, donde se ingresa el usuario, tambien cumple la funcion de hacer trigger a el print que muestra el porcentaje de las ordenes que disponen de los elementos seleccionados
