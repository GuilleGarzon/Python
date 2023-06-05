# Declarar variables
sumamente_apto = 0
moderadamente_apto = 0
marginalmente_apto = 0
no_apto = 0
f = "{:.2f}"
#Arreglo
prom_temperatura = []
prom_profundidad = []
promedio_temperatura = []
promedio_profundidad = []
#Crear función para el promedio del arreglo
def calcular_promedio(arreglo):
    if len(arreglo) > 0:
        return sum(arreglo) / len(arreglo)
    return 0 
#Capturar información del teclado
num_lecturas = int(input("Ingrese Número de lecturas: "))
#Ciclo para el numero de lecturas
for i in range (num_lecturas):
    
    #Valores de entrada
    temperatura_media = input("Ingrese Temperatura media "+ str(i + 1) + ": ")
    profundidad_efectiva = input("Ingrese profundidad efectiva " + str(i + 1) + ": ")
    #Arreglo del promedio de la temperatura
    auxiliar_arreglo_temperatura = temperatura_media.split(" ")
    arreglo_temperatura = [float(elemento) for elemento in auxiliar_arreglo_temperatura]
    prom_temperatura = f.format(calcular_promedio(arreglo_temperatura))
    promedio_temperatura.append(prom_temperatura)
          
    #Arreglo promedio de la profundidad
    auxiliar_arreglo_profundidad = profundidad_efectiva.split(" ")
    arreglo_profundidad = [float(elemento) for elemento in auxiliar_arreglo_profundidad]
    prom_profundidad = f.format(calcular_promedio(arreglo_profundidad))
    promedio_profundidad.append(prom_profundidad)
    
    # Comparaciones
    if  (75.001 <= float(promedio_temperatura[i]) <= 82)  and (float(promedio_profundidad[i]) > 39.37):
        sumamente_apto += 1
    elif (82.001 <= float(promedio_temperatura[i]) <= 86 or 68.001 <= float(promedio_temperatura[i]) <= 75)  and 19.69 <= float(promedio_profundidad[i]) <= 39.37:
        moderadamente_apto += 1 
    elif (86.001 <= float(promedio_temperatura[i]) <= 90 or 64 <= float(promedio_temperatura[i]) <= 68)  and 9.84 <= float(promedio_profundidad[i]) <= 19.68:
        marginalmente_apto += 1   
    elif (float(promedio_temperatura[i]) < 64.00 or float(promedio_temperatura[i]) > 90.00)  and (float(promedio_profundidad[i]) < 9.84):
        no_apto += 1 
    elif (75.001 <= float(promedio_temperatura[i]) <= 82) and 19.69 <= float(promedio_profundidad[i]) <= 39.37:
        moderadamente_apto += 1 
    elif (75.001 <= float(promedio_temperatura[i]) <= 82) and 9.84 <= float(promedio_profundidad[i]) <= 19.68:
        marginalmente_apto += 1  
    elif (75.001 <= float(promedio_temperatura[i]) <= 82) and  (float(promedio_profundidad[i]) < 9.84):
        no_apto += 1    
    elif (82.001 <= float(promedio_temperatura[i]) <= 86 or 68.001 <= float(promedio_temperatura[i]) <= 75) and (float(promedio_profundidad[i]) > 39.37):
        moderadamente_apto += 1
    elif (82.001 <= float(promedio_temperatura[i]) <= 86 or 68.001 <= float(promedio_temperatura[i]) <= 75) and 9.84 <= float(promedio_profundidad[i]) <= 19.68:
        marginalmente_apto += 1 
    elif (82.001 <= float(promedio_temperatura[i]) <= 86 or 68.001 <= float(promedio_temperatura[i]) <= 75) and (float(promedio_profundidad[i]) < 9.84):
        no_apto += 1
    elif (86.001 <= float(promedio_temperatura[i]) <= 90 or 64 <= float(promedio_temperatura[i]) <= 68) and (float(promedio_profundidad[i]) > 39.37):
        marginalmente_apto += 1
    elif (86.001 <= float(promedio_temperatura[i]) <= 90 or 64 <= float(promedio_temperatura[i]) <= 68) and 19.69 <= float(promedio_profundidad[i]) <= 39.37:
        marginalmente_apto += 1
    elif (86.001 <= float(promedio_temperatura[i]) <= 90 or 64 <= float(promedio_temperatura[i]) <= 68) and (float(promedio_profundidad[i]) < 9.84):
        no_apto += 1        
    elif (float(promedio_temperatura[i]) < 64.00 or float(promedio_temperatura[i]) > 90.00) and (float(promedio_profundidad[i]) > 39.37):
        no_apto += 1                
    elif (float(promedio_temperatura[i]) < 64.00 or float(promedio_temperatura[i]) > 90.00) and 19.69 <= float(promedio_profundidad[i]) <= 39.37:
        no_apto += 1        
    elif (float(promedio_temperatura[i]) < 64.00 or float(promedio_temperatura[i]) > 90.00) and 9.84 <= float(promedio_profundidad[i]) <= 19.68:
        no_apto += 1
     
#Salidas    
print(*promedio_temperatura) 
print(*promedio_profundidad)
print("sumamente apto", sumamente_apto)
print("moderadamente apto", moderadamente_apto)
print("marginalmente apto", marginalmente_apto)
print("no apto", no_apto)
