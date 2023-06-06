#Funcion que permite convertir el dato de cadena a su verdadero tipo
def convertir_dato(dato):
    #Intentar convertir el valor a numero entero
    try: 
        dato_r = int(dato)
    #Error controlado
    except:
        #Intentar convertir el valor a numero decimal
        try:
            dato_r = float(dato)
        #Error controlado
        except:
            #Intenta verificar los valores
            dato_r = dato
    return dato_r                       
#Funcion para convertir el arreglo en sus datos reales
def convertir_arreglo(matriz):
    for i in range(len(matriz)):
        matriz[i] = convertir_dato(matriz[i])
    return matriz
#Cantidad de daos a leer por filas
num_lecturas = int(input("Ingrese número de lecturas: "))
# Declarar variables
sumamente = 0
moderadamente = 0
marginalmente = 0
no = 0
#Arreglos
matriz_temperatura = []
matriz_profundidad = []
matriz_mayor = []
matriz_menor = []
#Ciclo de lectura
for i in range (num_lecturas):
    temperatura_media = input("Ingrese temperatura media " + str(i + 1) + ": ")
    auxiliar_arreglo_temperatura = temperatura_media.split(" ")
    arreglo_temperatura= convertir_arreglo(auxiliar_arreglo_temperatura)
    matriz_temperatura.append(arreglo_temperatura)
for i in range(num_lecturas):
    profundidad_efectiva = input("Ingrese Profundidad efectiva " + str(i + 1) + ": ")
    auxiliar_arreglo_profundidad = profundidad_efectiva.split(" ")
    arreglo_profundidad= convertir_arreglo(auxiliar_arreglo_profundidad)
    matriz_profundidad.append(arreglo_profundidad)
# Recorrido de parejas
for i in range(num_lecturas):
    m = len(matriz_temperatura[i])    
    sumamente_apto = 0
    moderadamente_apto = 0
    marginalmente_apto = 0
    no_apto = 0
    for j in range(m):
        # Comparaciones
        if  (75.001 <= (matriz_temperatura[i][j]) <= 82)  and ((matriz_profundidad[i][j]) > 39.37):
            sumamente += 1
            sumamente_apto += 1            
        elif (82.001 <= (matriz_temperatura[i][j]) <= 86 or 68.001 <= (matriz_temperatura[i][j]) <= 75)  and 19.69 <= (matriz_profundidad[i][j]) <= 39.37:
            moderadamente += 1 
            moderadamente_apto += 1            
        elif (86.001 <= (matriz_temperatura[i][j]) <= 90 or 64 <= (matriz_temperatura[i][j]) <= 68)  and 9.84 <= (matriz_profundidad[i][j]) <= 19.68:
            marginalmente += 1   
            marginalmente_apto += 1            
        elif ((matriz_temperatura[i][j]) < 64.00 or (matriz_temperatura[i][j]) > 90.00)  and ((matriz_profundidad[i][j]) < 9.84):
            no += 1 
            no_apto += 1            
        elif (75.001 <= (matriz_temperatura[i][j]) <= 82) and 19.69 <= (matriz_profundidad[i][j]) <= 39.37:
            moderadamente += 1 
            moderadamente_apto += 1            
        elif (75.001 <= (matriz_temperatura[i][j]) <= 82) and 9.84 <= (matriz_profundidad[i][j]) <= 19.68:
            marginalmente += 1  
            marginalmente_apto += 1        
        elif (75.001 <= (matriz_temperatura[i][j]) <= 82) and  ((matriz_profundidad[i])[j] < 9.84):
            no += 1
            no_apto += 1                
        elif (82.001 <= (matriz_temperatura[i][j]) <= 86 or 68.001 <= (matriz_temperatura[i][j]) <= 75) and ((matriz_profundidad[i][j]) > 39.37):
            moderadamente += 1
            moderadamente_apto += 1            
        elif (82.001 <= (matriz_temperatura[i][j]) <= 86 or 68.001 <= (matriz_temperatura[i][j]) <= 75) and 9.84 <= (matriz_profundidad[i][j]) <= 19.68:
            marginalmente += 1
            marginalmente_apto += 1             
        elif (82.001 <= (matriz_temperatura[i][j]) <= 86 or 68.001 <= (matriz_temperatura[i][j]) <= 75) and ((matriz_profundidad[i][j]) < 9.84):
            no += 1
            no_apto += 1            
        elif (86.001 <= (matriz_temperatura[i][j]) <= 90 or 64 <= (matriz_temperatura[i][j]) <= 68) and ((matriz_profundidad[i][j]) > 39.37):
            marginalmente += 1
            marginalmente_apto += 1            
        elif (86.001 <= (matriz_temperatura[i][j]) <= 90 or 64 <= (matriz_temperatura[i][j]) <= 68) and 19.69 <= (matriz_profundidad[i][j]) <= 39.37:
            marginalmente += 1
            marginalmente_apto += 1            
        elif (86.001 <= (matriz_temperatura[i][j]) <= 90 or 64 <= (matriz_temperatura[i][j]) <= 68) and ((matriz_profundidad[i][j]) < 9.84):
            no += 1
            no_apto += 1                    
        elif ((matriz_temperatura[i][j]) < 64.00 or (matriz_temperatura[i][j]) > 90.00) and ((matriz_profundidad[i][j]) > 39.37):
            no += 1
            no_apto += 1                         
        elif ((matriz_temperatura[i][j]) < 64.00 or (matriz_temperatura[i][j]) > 90.00) and 19.69 <= (matriz_profundidad[i][j]) <= 39.37:
            no += 1
            no_apto += 1                   
        elif ((matriz_temperatura[i][j]) < 64.00 or (matriz_temperatura[i][j]) > 90.00) and 9.84 <= (matriz_profundidad[i][j]) <= 19.68:
            no += 1
            no_apto += 1           
    #Comparativa para escoger categoria mas repetida y se agrega a la matriz_mayor
    if sumamente_apto >= moderadamente_apto and sumamente_apto >= marginalmente_apto and sumamente_apto >= no_apto:        
        matriz_mayor.append("sumamente apto")        
    elif moderadamente_apto >= sumamente_apto and moderadamente_apto >= marginalmente_apto and moderadamente_apto >= no_apto:               
        matriz_mayor.append("moderadamente apto") 
    elif marginalmente_apto >= sumamente_apto and marginalmente_apto >= moderadamente_apto and marginalmente_apto >= no_apto:        
        matriz_mayor.append("marginalmente apto")       
    else:        
        matriz_mayor.append("no apto")
                 
    #Comparativa para escoger categoria menos repetida, e ignorar si la categoría tiene 0 y se agrega a la matriz_menor.
    if sumamente_apto <= moderadamente_apto and sumamente_apto <= marginalmente_apto and sumamente_apto <= no_apto:
        if sumamente_apto <= 0:
            if moderadamente_apto <= marginalmente_apto and moderadamente_apto <= no_apto:
                if moderadamente_apto <= 0:
                    if marginalmente_apto <= no_apto:
                        matriz_menor.append("marginalmente apto")
                    else:
                        matriz_menor.append("no apto")    
                else:
                    matriz_menor.append("moderadamente apto")
            elif marginalmente_apto <= moderadamente_apto and marginalmente_apto <= no_apto:
                if marginalmente_apto <= 0:
                    if moderadamente_apto <= no_apto:
                        matriz_menor.append("moderadamente apto")
                    else:
                        matriz_menor.append("no apto")     
                else:
                    matriz_menor.append("marginalmente apto")
            elif no_apto <= moderadamente_apto and no_apto <= marginalmente_apto:
                if no_apto <= 0:
                    if moderadamente_apto <= marginalmente_apto:
                        matriz_menor.append("moderadamente apto")
                    else:
                        matriz_menor.append("marginalmente apto")    
                else:    
                    matriz_menor.append("no apto")    
        else:    
            matriz_menor.append("sumamente apto")       
    elif moderadamente_apto <= sumamente_apto and moderadamente_apto <= marginalmente_apto and moderadamente_apto <= no_apto:  
        if moderadamente_apto <= 0:
            if sumamente_apto <= marginalmente_apto and sumamente_apto <= no_apto:
                if sumamente_apto <= 0:
                    if marginalmente_apto <= no_apto:
                        matriz_menor.append("marginalmente apto")
                    else:
                        matriz_menor.append("no apto")    
                else:
                    matriz_menor.append("sumamente apto")
            elif marginalmente_apto <= sumamente_apto and marginalmente_apto <= no_apto:
                if marginalmente_apto <= 0:
                    if sumamente_apto <= no_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("no apto")
                else:                
                    matriz_menor.append("marginalmente apto")
            elif no_apto <= sumamente_apto and no_apto <= marginalmente_apto:
                if no_apto <= 0:
                    if sumamente_apto <= marginalmente_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("marginalmente apto")    
                else:
                    matriz_menor.append("no apto")        
        else:                    
            matriz_menor.append("moderadamente apto")         
    elif marginalmente_apto <= sumamente_apto and marginalmente_apto <= moderadamente_apto and marginalmente_apto <= no_apto:       
        if marginalmente_apto <= 0:
            if sumamente_apto <= moderadamente_apto and sumamente_apto <= no_apto:
                if sumamente_apto <= 0:
                    if moderadamente_apto <= no_apto:
                        matriz_menor.append("moderadamente apto")
                    else:
                        matriz_menor.append("no apto")    
                else:
                    matriz_menor.append("sumamente apto")
            elif moderadamente_apto <= sumamente_apto and moderadamente_apto <= no_apto:
                if moderadamente_apto <= 0:
                    if sumamente_apto <= no_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("no apto")    
                else:
                    matriz_menor.append("moderadamente apto")
            elif no_apto <= sumamente_apto and no_apto <= moderadamente_apto:
                if no_apto <= 0:
                    if sumamente_apto <= moderadamente_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("moderadamente apto")    
                else:    
                    matriz_menor.append("no apto")
        else:
            matriz_menor.append("marginalmente apto")    
    elif no_apto <= sumamente_apto and no_apto <= moderadamente_apto and no_apto <= marginalmente_apto:
        if no_apto <= 0:
            if sumamente_apto <= moderadamente_apto and sumamente_apto <= marginalmente_apto:
                if sumamente_apto <= 0:
                    if moderadamente_apto <= marginalmente_apto:
                        matriz_menor.append("moderadamente apto")
                    else:
                        matriz_menor.append("marginalmente apto")    
                else:
                    matriz_menor.append("sumamente apto")
            elif moderadamente_apto <= sumamente_apto and moderadamente_apto <= marginalmente_apto:
                if moderadamente_apto <= 0:
                    if sumamente_apto <= marginalmente_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("marginalmente apto")    
                else:    
                    matriz_menor.append("moderadamente apto") 
            elif marginalmente_apto <= sumamente_apto and marginalmente_apto <= moderadamente_apto:
                if marginalmente_apto <= 0:
                    if sumamente_apto <= moderadamente_apto:
                        matriz_menor.append("sumamente apto")
                    else:
                        matriz_menor.append("moderadamente apto")    
                else:
                    matriz_menor.append("marginalmente apto")       
        else:    
            matriz_menor.append("no apto")        
#Salidas esperadas          
matriz_resultante = no, marginalmente, moderadamente, sumamente  
print(*matriz_resultante)
print()
print(",".join(str(x) for x in matriz_mayor))
print()
print(",".join(str(x) for x in matriz_menor))
