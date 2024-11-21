inicio = input("#####Notas##### \n\n ¿Qué quieres hacer? \n\n 1.- Calcular mi nota del trimestre\n 2.- Funcion de la aplicación \n (Selecciona dependiendo del número)\n")

if inicio == "1":
    cantidad = input("¿Cuántas notas tienes que calcular? : ")
    cantidad = int(cantidad)
    if cantidad >= 4 or cantidad <= 1:
        print("La aplicacion no funciona :()")

    elif cantidad == 2:
        x = input("Dime la primera nota: ")
        x = float(x)
        y = input("Dime la segunda nota: ")
        y = float(y)
        porcentaje = input("¿Cuánto cuentan estos dos exámenes en la evaluación (en %)? : ")
        porcentaje = float(porcentaje) 
        
        calculoNota = (x + y) / 2
        
        calculoTerminado = calculoNota * (porcentaje / 100)
        
        if calculoNota >= 5:
            print(f"Aquí tienes tus resultados : \n Nota final : {calculoNota} \n Aportación en la evaluación : {calculoTerminado}")
            print("🎊🎊 Felicidades, espero que pases unas buenas vacaciones! 🎊🎊")
            input("Presiona enter para salir")
        elif calculoNota < 5:
            print(f"Aquí tienes tus resultados : \n Nota final : {calculoNota} \n Aportación en la evaluación : {calculoTerminado}")
            print("Tendrás que estudiar un poco mas 😢")
            input("Presiona enter para salir")
    elif cantidad == 3:
        x = input("Dime la primera nota: ")
        x = float(x)
        y = input("Dime la segunda nota: ")
        y = float(y)
        z = input("Dime la tercera nota: ")
        z = float(z)

        porcentaje = input("¿Cuánto cuentan estos exámenes en la evaluación (en %)? : ")
        porcentaje = float(porcentaje) 
        
        calculoNota = (x + y + z) / 3
        
        calculoTerminado = calculoNota * (porcentaje / 100)
        
        if calculoNota >= 5:
            print(f"Aquí tienes tus resultados : \n Nota final : {calculoNota} \n Aportación en la evaluación : {calculoTerminado}")
            print("🎊🎊 Felicidades, espero que pases unas buenas vacaciones! 🎊🎊")
            input("Presiona enter para salir")
        elif calculoNota < 5:
            print(f"Aquí tienes tus resultados : \n Nota final : {calculoNota} \n Aportación en la evaluación : {calculoTerminado}")
            print("Tendrás que estudiar un poco mas 😢")
            input("Presiona enter para salir")

elif inicio == "2":
    print("La función de la aplicación es la siguiente : \n Calcularemos tus notas dependiendo si son 2 o 3 notas a calcular, si son mayores de estas te tendrás que buscar otra aplicación gordo sidoso \n Te daremos la nota final y lo que aportará a tu evaluación :)")
    input("Presiona enter para salir")