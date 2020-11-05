'''
Matematica Discreta - Seccion 10
Bryann Alfaro
Diego Arredondo
Oscar Saravia

Catedratico > Mario Castillo '''


bandera = True


def encriptar(e, N, mensaje):
    llaveP = ""

    for i in mensaje:
        m = ord(i)
        
        llaveP += str(pow(m,e,N)) + " "
    return llaveP

def desencriptar(d, N, encriptado):
    mensajeDesencriptado = ""

    partes = encriptado.split()
    for j in partes:
        if j:
            
            c = int(j)
            
            mensajeDesencriptado += chr(pow(c,d,N))+ ""
            
    return mensajeDesencriptado


while bandera:

    print("RSA - UVG - CYPHER")
    print("Tus llaves son: Publica 13, Privada 37 N = 143")
    print("Escoge una opcion: ")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3 Salir de ejecucion")
    
    opcion = int(input())
    
    if(opcion==1):
        print("Encrypt process........")
        m = input("Mensaje: ")
        llavePublica= input("Ingresa la llave publica: ")

        p= 11
        q = 13
        d = 37
        N = 143
        e= 13
        encriptadoM = encriptar(e,N, m)
        print("Encriptacion: ",encriptadoM)
        
    
    elif(opcion==2):
        d = 37
        N = 143
        print("Decrypt process......")
        m2 = input("Ingrese el mensaje a desencriptar: ")
        llavePrivada = input("Ingrese la llave privada: ")
        desencriptadoM = desencriptar(d,N, m2)
        print("Desencriptacion: ",desencriptadoM)
    
    else:
        print("Gracias por confiar en nosotross")
        bandera = False
