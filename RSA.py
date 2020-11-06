'''
Matematica Discreta - Seccion 10
Bryann Alfaro
Diego Arredondo
Oscar Saravia

Catedratico > Mario Castillo '''



print("__    __  __     __   ______    ______   _______   __      __  _______   ________ ")
print("/  |  /  |/  |   /  | /      \  /      \ /       \ /  \    /  |/       \ /        |")
print("$$ |  $$ |$$ |   $$ |/$$$$$$  |/$$$$$$  |$$$$$$$  |$$  \  /$$/ $$$$$$$  |$$$$$$$$/ ")
print("$$ |  $$ |$$ |   $$ |$$ | _$$/ $$ |  $$/ $$ |__$$ | $$  \/$$/  $$ |__$$ |   $$ |   ")
print("$$ |  $$ |$$  \ /$$/ $$ |/    |$$ |      $$    $$<   $$  $$/   $$    $$/    $$ |   ")
print("$$ |  $$ | $$  /$$/  $$ |$$$$ |$$ |   __ $$$$$$$  |   $$$$/    $$$$$$$/     $$ |   ")
print("$$ \__$$ |  $$ $$/   $$ \__$$ |$$ \__/  |$$ |  $$ |    $$ |    $$ |         $$ |   ")
print("$$    $$/    $$$/    $$    $$/ $$    $$/ $$ |  $$ |    $$ |    $$ |         $$ |   ")
print(" $$$$$$/      $/      $$$$$$/   $$$$$$/  $$/   $$/     $$/     $$/          $$/    ")


                                                                                   
                                                                                   


bandera = True

#Maximo comun divisor usando el Algoritmo de Euclides
def mcd(a,b):
    while b!=0:
        a = a/b
        b = a%b
        
    return a

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
    print("------------------------------------------------------")
    print("")

    #print(mcd(5,3))
    
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
        print("")
        print("----------------------------------------")
        print("Encriptacion: ",encriptadoM)
        print("----------------------------------------")
        print("")


    
    elif(opcion==2):
        d = 37
        N = 143
        print("Decrypt process......")
        m2 = input("Ingrese el mensaje a desencriptar: ")
        llavePrivada = input("Ingrese la llave privada: ")
        desencriptadoM = desencriptar(d,N, m2)
        print("")
        print("---------------------------------")
        print("Desencriptacion: ",desencriptadoM)
        print("---------------------------------")
        print("")
    
    else:
        print("Gracias por confiar en nosotross")
        bandera = False
