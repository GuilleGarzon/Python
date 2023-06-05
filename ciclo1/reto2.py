num_lecturas = int(input("Ingrese número de lecturas: ")) 
#Declarar variables
contador = 0
sumamente_apto = 0
moderadamente_apto = 0
marginalmente_apto = 0
no_apto = 0
suma_temperatura = 0
suma_profundidad = 0
#Crear ciclo
while contador < num_lecturas:
    temperaturamedia = float(input("Ingrese Temperatura media " + str(contador + 1) + ": "))
    profundidadefectiva = float(input("Ingrese Profundidad efectiva " + str(contador + 1) + ": "))
    if  (76 <= temperaturamedia <= 82)  and (profundidadefectiva > 39.37):
        sumamente_apto += 1
    elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75)  and 19.69 <= profundidadefectiva <= 39.37:
        moderadamente_apto += 1     
    elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68)  and 9.84 <= profundidadefectiva <= 19.68:
        marginalmente_apto += 1     
    elif (temperaturamedia < 64 or temperaturamedia > 90)  and (profundidadefectiva < 9.84):
        no_apto += 1    
    elif (76 <= temperaturamedia <= 82) and 19.69 <= profundidadefectiva <= 39.37:
        moderadamente_apto += 1
    elif (76 <= temperaturamedia <= 82) and 9.84 <= profundidadefectiva <= 19.68:
        marginalmente_apto += 1   
    elif (76 <= temperaturamedia <= 82) and  (profundidadefectiva < 9.84):
        no_apto += 1       
    elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and (profundidadefectiva > 39.37):
        moderadamente_apto += 1
    elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and 9.84 <= profundidadefectiva <= 19.68:
        marginalmente_apto += 1 
    elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and (profundidadefectiva < 9.84):
        no_apto += 1
    elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and (profundidadefectiva > 39.37):
        marginalmente_apto += 1
    elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and 19.69 <= profundidadefectiva <= 39.37:
        marginalmente_apto += 1
    elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and (profundidadefectiva < 9.84):
        no_apto += 1
    elif (temperaturamedia < 64 or temperaturamedia > 90) and (profundidadefectiva > 39.37):
        no_apto += 1
    elif (temperaturamedia < 64 or temperaturamedia > 90) and 19.69 <= profundidadefectiva <= 39.37:
        no_apto += 1
    elif (temperaturamedia < 64 or temperaturamedia > 90) and 9.84 <= profundidadefectiva <= 19.68:
        no_apto += 1
    #Crear acumulador
    suma_temperatura = suma_temperatura + temperaturamedia
    suma_profundidad = suma_profundidad + profundidadefectiva    
    #Realizar incremento del contador    
    contador += 1
f = "{:.2f}"
#Salidas    
print("Promedio de temperatura media: ", f.format(suma_temperatura/num_lecturas))
print("Promedio de profundidad efectiva: ", f.format(suma_profundidad/num_lecturas))    
print("Sumamente Apto ", sumamente_apto)
print("Moderadamente Apto ", moderadamente_apto)
print("Marginalmente Apto ", marginalmente_apto)
print("No Apto ", no_apto)