temperaturamedia = float(input("Digite la temperatura media anual: "))
profundidadefectiva = float(input("Digite la profundidad efectiva del suelo (pulgadas): "))
if  (76 <= temperaturamedia <= 82)  and (profundidadefectiva > 39.37):
    print("El entorno es: Sumamente Apto")
elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75)  and 19.69 <= profundidadefectiva <= 39.37:
    print("El entorno es: Moderadamente Apto")     
elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68)  and 9.84 <= profundidadefectiva <= 19.68:
    print("El entorno es: Marginalmente Apto")     
elif (temperaturamedia < 64 or temperaturamedia > 90)  and (profundidadefectiva < 9.84):
    print("El entorno es: No Apto")    
elif (76 <= temperaturamedia <= 82) and 19.69 <= profundidadefectiva <= 39.37:
    print("El entorno es: Moderadamente Apto")
elif (76 <= temperaturamedia <= 82) and 9.84 <= profundidadefectiva <= 19.68:
    print("El entorno es: Marginalmente Apto")   
elif (76 <= temperaturamedia <= 82) and  (profundidadefectiva < 9.84):
    print("El entorno es: No Apto")       
elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and (profundidadefectiva > 39.37):
    print("El entorno es: Moderadamente Apto")
elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and 9.84 <= profundidadefectiva <= 19.68:
    print("El entorno es: Marginalmente Apto") 
elif (83 <= temperaturamedia <= 86 or 69 <= temperaturamedia <= 75) and (profundidadefectiva < 9.84):
    print("El entorno es: No Apto")
elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and (profundidadefectiva > 39.37):
    print("El entorno es: Marginalmente Apto")
elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and 19.69 <= profundidadefectiva <= 39.37:
    print("El entorno es: Marginalmente Apto")
elif (87 <= temperaturamedia <= 90 or 64 <= temperaturamedia <= 68) and (profundidadefectiva < 9.84):
    print("El entorno es: No Apto")
elif (temperaturamedia < 64 or temperaturamedia > 90) and (profundidadefectiva > 39.37):
    print("El entorno es: No Apto")
elif (temperaturamedia < 64 or temperaturamedia > 90) and 19.69 <= profundidadefectiva <= 39.37:
    print("El entorno es: No Apto")
elif (temperaturamedia < 64 or temperaturamedia > 90) and 9.84 <= profundidadefectiva <= 19.68:
    print("El entorno es: No Apto")