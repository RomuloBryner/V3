ruta = "datosok.txt"   
with open(ruta, mode = "a", encoding = "utf-8") as fichero: 

    for i in range(10):
        print("1. Registrar un nombre. \n2. Buscar datos. \n3. Editar un dato. \n4. Salir.")
        Caso = input()  
        if Caso == "1" :
            
                print("Escriba su cedula: ")
                Cedula = input()
                print("Escriba su nombre: ")
                Nombre = input()
                print("Escriba sus apellidos: ")
                Apellidos = input()
                print("Escriba su Edad: ")
                Edad = input()
                Guardar = "Y"
                if Guardar == "Y":
                    fichero.write("Cedula   ")
                    fichero.write("Nombres   ")
                    fichero.write("Apellidos   ")
                    fichero.write("Edad   ")
                    fichero.write("\n")
                    fichero.write(Cedula)
                    fichero.write("   ,")
                    fichero.write(Nombre)
                    fichero.write("   ,")
                    fichero.write(Apellidos)
                    fichero.write("   ,")
                    fichero.write(Edad)
                    fichero.write("\n")
                    fichero.write("\n")                    
                    print("Guardado!")
                               
        elif Caso == "2" :
            print("Escriba el dato que desea buscar:")
            Dato = input()           
            archivo = open("datosok.txt", "r")             
            flag = 0
            index = 0            
            for line in archivo:  
                index += 1                 
                if Dato in line:                  
                  flag = 1
                  break                      
            if flag == 0: 
               print('El dato: ', Dato , 'no se encontro.') 
            else: 
               print('El dato: ', Dato, 'Se encontro en la linea', index,'\n', line)  
            archivo.close()
        
        elif Caso == "3":
            print("Escriba el dato que desea editar: ")
            Dato2 = input()          
            archivo = open("datosok.txt", "r")             
            flag = 0
            index = 0            
            for line in archivo:  
                index += 1                 
                if Dato2 in line:                  
                  flag = 1
                  break                      
            if flag == 0: 
               print('El dato: ',Dato2 , 'no se encontro.') 
            else: 
               print('El dato: ',Dato2, 'Se encontro en la linea', index,'\n', line)
            
               print("Desea remplazar o eliminarlos datos de la linea?", line)
               print('1.Remplazar\n2.Eliminar')
               Si = input()
               if Si == "1":
                   f = open('datosok.txt', 'r')
                   lines = f.readlines()
                   print("Escriba su cedula: ")
                   Cedula = input()
                   print("Escriba su nombre: ")
                   Nombre = input()
                   print("Escriba sus apellidos: ")
                   Apellidos = input()
                   print("Escriba su Edad: ")
                   Edad = input()
                   Total = (Cedula, Nombre, Apellidos, Edad,'\n\n')
                   lines[index - 1] = (str(Total))

                   f = open('datosok.txt', 'w')
                   Escribir = f.writelines(lines)
                   f.close()
               elif Si == "2":
                   f = open('datosok.txt', 'r')
                   lines = f.readlines()
                   Total = ('\n\n')
                   lines[index - 1] = (str(Total))
                   lines[index - 2] = (str(Total))

                   f = open('datosok.txt', 'w')
                   Escribir = f.writelines(lines)
                   f.close()
                
                   
               archivo.close()
                      
        
        elif Caso == "4":
            break
            
    input()