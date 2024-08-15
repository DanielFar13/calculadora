from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

def main():
    while True:
        print("¿Qué operación quieres realizar?")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        operacion = input("Selecciona un número (1-5): ")
        
        if operacion == '5':
            print("¡Haga algo, nos esforzamos!")
            break
        
        if operacion in ['1', '2', '3', '4']:
            num1 = float(input("Dame el primer número: "))
            num2 = float(input("Dame el segundo número: "))
            
            if operacion == '1':
                resultado = sumar(num1, num2)
            elif operacion == '2':
                resultado = restar(num1, num2)
            elif operacion == '3':
                resultado = multiplicar(num1, num2)
            elif operacion == '4':
                resultado = dividir(num1, num2)
                
            print("El resultado es:", resultado)
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
        
        continuar = input("¿Te gustaría continuar? (si/no): ").strip().lower()
        if continuar != 'si':
            print("¡Gracias profe, ponganos 100 o lo hackeamos!")
            break

if __name__ == "__main__":
    main()
