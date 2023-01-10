# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
# el método __init__. Calcular después la suma, resta, multiplicación y división.
# Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    num1=float(input("ingrese un numero entero: "))
    num2=float(input("ingrese otro numero entero: "))
    def __int__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def suma(self):
        print(self.num1+self.num2)
    def resta(self):
        print(self.num1-self.num2)
    def multiplicacion(self):
        print(self.num1*self.num2)
    def division(self):
        print(self.num1/self.num2)

resultado=Calculadora()
resultado.suma()
resultado.resta()
resultado.multiplicacion()
resultado.division()


