num1=30
num2=0

try:
    resultado = num1/num2
except ZeroDivisionError:
    print("Error en el programa")

finally:
    print("Yo siempre aparezco")