print("Bienvenidos al entrenamiento con python, vamos a disfrutar al maximo esta sesion")

"""
    Descuento en una compra
    Si compras mas de $1000 obtienes un descuento del 20%
    Pide el monto de la compra y muestra el precio final
"""
# Pedir datos por tecldo al usuario int (entero) float (decimales) str (cadena de caracteres) bool (boleano unos o ceros)

compra = float(input("digite elvalor de su compra: "))
# si compras mas de $1000 obtienes un descuento del 20%
# siempre que la salida tenga mas de un camino de resolucion, debo implementar condicionales
# operadores combinados
# operadores de asignacion =, operadores aritmeticos + - * /, operadores logicos and y, or o, not

if compra > 1000:
    descuento = compra * 0.2
    compra -= descuento
    print(f"El descuento es de {descuento}, y el total a pagar es: {compra}")
