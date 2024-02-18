def suma(a, b):
  """Suma dos números."""
  return a + b

def resta(a, b):
  """Resta dos números."""
  return a - b

def multiplicacion(a, b):
  """Multiplica dos números."""
  return a * b

def division(a, b):
  """Divide dos números."""
  if b == 0:
    return "No se puede dividir por cero."
  else:
    return a / b

def main():
  """Función principal de la calculadora."""
  while True:
    # Mostrar menú de opciones
    #print("-" * 20)
    print("-" * 20)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. esta es una linea de prueba para la opcion salir")
    print("7. otra prueba")

    # Solicitar opción al usuario
    opcion = int(input("Ingrese una opción: "))

    # Validar la opción ingresada
    if opcion not in range(1, 6):
      print("Opción no válida.")
      continue

    # Si la opción es válida, realizar la operación correspondiente
    if opcion == 1:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = suma(a, b)
      print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = resta(a, b)
      print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = multiplicacion(a, b)
      print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = division(a, b)
      print(f"El resultado de la división es: {resultado}")
    else:
      # Salir del programa
      break

if __name__ == "__main__":
  main()
