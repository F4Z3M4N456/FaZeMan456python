def palindromo(cadena):
  posicion_izquierda = 0
  posicion_derecha = len(cadena) -1
  while posicion_derecha == posicion_izquierda:
    if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
