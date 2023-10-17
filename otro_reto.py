#https://replit.com/join/euzfrflmmq-ivannamartinez2
#¯\_(ツ)_/¯
grasa=float(input("¿Cuánta grasa tiene tu alimento?, en gramos por porción"))
azucar=float(input("¿Cuánta azucar tiene tu alimento?, en gramos por porción"))
sodio=float(input("¿Cuánto sodio tiene tu alimento?, en miligramos por porción"))
if(grasa<=5 and azucar<=10):
  print("Tu alimento es bajo en azucar y grasa")
elif(sodio<=100):
  print("Tu alimento es bajo en sodio")
else:
  print("Considera advertencias nutricionales")
