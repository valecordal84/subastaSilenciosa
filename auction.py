ofertas = {}

def ofertaMaxima(ofertaDict):
    ganador = ""
    ofertaAlta = 0
    for ofertante in ofertaDict:
        precio = ofertaDict[ofertante]
        if precio > ofertaAlta:
            ofertaAlta = precio 
            ganador = ofertante
            
    print(f"El ganador es {ganador} con una oferta de ${ofertaAlta}")

continuar = True
while continuar:
    nombre= input("Cual es tu nombre?: ")
    precio = int(input("Cual es tu oferta?: "))
    ofertas [nombre] = precio 
    continuar = input ("Hay mas ofertas? Escribe 'si' o 'no'. \n ").lower()
    
    if continuar == "no":
        continuar = False
        ofertaMaxima(ofertas)
    elif continuar == "si":
        print("\n" * 20 ) 
 

