# calculadora.py - HU-1
# Versión inicial: operaciones básicas y historial en memoria

def mostrar_menu():
    print("\n=== CALCULADORA BÁSICA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Ver historial")
    print("6. Salir")

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return "Error: División por cero" if b == 0 else a / b

def main():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))
            except ValueError:
                print("⚠ Ingresa números válidos.")
                continue

            if opcion == "1":
                resultado = sumar(num1, num2)
                operacion = f"{num1} + {num2} = {resultado}"
            elif opcion == "2":
                resultado = restar(num1, num2)
                operacion = f"{num1} - {num2} = {resultado}"
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                operacion = f"{num1} * {num2} = {resultado}"
            else:
                resultado = dividir(num1, num2)
                operacion = f"{num1} / {num2} = {resultado}"

            print("Resultado:", resultado)
            historial.append(operacion)

        elif opcion == "5":
            print("\n=== HISTORIAL ===")
            if historial:
                for i, h in enumerate(historial, start=1):
                    print(f"{i}. {h}")
            else:
                print("No hay operaciones registradas.")
        elif opcion == "6":
            print("Adiós 👋")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

