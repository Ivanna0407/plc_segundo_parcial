#Ivanna Martínez de Alba A00573772
dia=input("Dime el día de la semana en minusculas ")
hora=float(input("Dime la hora actual en formato de 24 horas "))
tarea=input("Dime el tipo de tarea. Puede ser estudio,descanso,deportes o trabajo ")
if(hora>1 and hora<=5):
  print("Debes estar dormido")
elif(hora>5 and hora<14):
  print("Debes estar en clase")
elif(hora>18 and hora<22 and tarea=="descanso"):
  print("Además de tomar una siesta puedes comenzar a realizar tus tareas")
elif(hora>18 and hora<22 and dia=="sábado" or dia=="domingo"):
    print("Puedes ver una película")
elif(hora>14 and hora<20 and dia=="lunes" or dia=="miércoles" or dia=="jueves"):
    print("Puedes ir al gimnasio")
elif(hora>13 and hora<15 and dia=="martes" or dia=="jueves"):
    print("Espero que estes comiendo algo nutritivo")
elif(hora>14 and hora<22):
  print("Puedes hacer tareas")
