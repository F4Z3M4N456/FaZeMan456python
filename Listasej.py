f1 = [1,3,2,1]
f2 = [3,2,5,4]
f3 = [6,7,7,5]

#Tarea 1: Comprobar que todas las listas tienen el mismo largo


#Tarea 2: Sumar el primer y el ultimo numero de cada variable
#Ejemplo: 20

#Tarea 3: Sumar todos los numeros que esten en la lista que no sean el primero y el último. 
#Ejemplo: 26


#Tarea #4: Restar los resultados obtenidos de las tareas 2 y 3 
#Ejemplo: 20-26


#Tarea 5: Mostrar el resultado.
#Ejemplo: -6

x=len(f1)
y=len(f2)
z=len(f3)

if x == y and x == z:
  print("Las listas tienen el mismo largo")

d=(f1[0]) + (f1[-1])
e=(f2[0]) + (f2[-1])
t=(f3[0]) + (f3[-1])
l= res = (d+e+t)
print(res)

v=sum(f1)+sum(f2)+sum(f3)
j=res=(v-d-e-t)
print(res)

q=l-j
print(q)
