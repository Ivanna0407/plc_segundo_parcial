#https://replit.com/join/oprxsqpugb-ivannamartinez2
#Ivanna Martínez de Alba A00573772
#Entrada de varibales
cantidad=int(input("¿Cuál es la cantidad del prestamo? "))
tasa=int(input("¿Cuál es la tasa de interés anual en porcentage? "))
plazo=int(input("¿Cuál es el plazo de tu préstamo en años?"))
#Condicionales 
if (tasa<=5 and plazo<=5):
  print("Tu prestamo de",cantidad,"pesos es de bajo riesgo")
elif(tasa>5 or plazo>5):
  print("Tu prestamo de",cantidad,"pesos es de riesgo moderado")
else:
  print("Tu prestamo de",cantidad,"pesos es de alto riesgo")
