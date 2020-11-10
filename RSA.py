'''
Matematica Discreta - Seccion 10
Bryann Alfaro
Diego Arredondo
Oscar Saravia

Catedratico: Mario Castillo '''

'''
Referencias:
https://www.comparitech.com/blog/information-security/rsa-encryption/
https://www.youtube.com/watch?v=4zahvcJ9glg
https://www.youtube.com/watch?v=KS169C845aU
https://www.di-mgt.com.au/rsa_alg.html
'''

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

#Encriptacion utilizando la formula : c = m^e%N
def encriptar(e, N, mensaje):
    llaveP = ""

    for i in mensaje:
        m = ord(i)
        
        llaveP += str(pow(m,e,N)) + " "
    return llaveP

#Desencriptacion utilizando la formula : m = c^d%N
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
    print("Te recomendamos esta llave: ")
    print("Llave publica: 5,82919")
    print("Llave privada: 16469,82919")
    print("Escoge una opcion: ")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3 Salir de ejecucion")
    print("------------------------------------------------------")
    print("")

    
    opcion = int(input())
    
    if(opcion==1):
        print("Encrypt process........\n")
        m = input("Mensaje: ")
        llavePublica= input("Ingresa la llave publica de la forma e,n:  ")


        partes= llavePublica.split(",")
        
        #Ingreso de ambos parametros
        while(len(partes)==1):
            print("Error, falta un parametro")
            llavePublica= input("Ingresa la llave publica de la forma e,n:  ")
            partes= llavePublica.split(",")

        #Valor minimo de n con base a tabla ASCII
        while(int(partes[1])<126):
            print("Error de longitud N")
            llavePublica= input("Ingresa la llave publica (e,n):  ")
            partes= llavePublica.split(",")
        
        #Llamado a la encriptacion
        encriptadoM = encriptar(int(partes[0]),int(partes[1]), m)
        print("")
        print("----------------------------------------")
        print("Encriptacion: ",encriptadoM)
        print("----------------------------------------")
        print("")


    elif(opcion==2):
       
        print("Decrypt process......")
        m2 = input("Ingrese el mensaje a desencriptar: ")
        llavePrivada = input("Ingrese la llave privada de la forma d,n: ")
        
        partesPrivada = llavePrivada.split(",")

        #Ingreso de ambos parametros
        while(len(partesPrivada)==1):
            print("Error")
            llavePrivada= input("Ingresa la llave privada de la forma d,n:  ")
            partesPrivada = llavePrivada.split(",")

        #Valor minimo de n con base a tabla ASCII
        while(int(partesPrivada[1])<126):
            print("Error")
            llavePrivada= input("Ingresa la llave privada (d,n):  ")
            partes= llavePrivada.split(",")
        
        
        #Llamado a la desencriptacion
        desencriptadoM = desencriptar(int(partesPrivada[0]),int(partesPrivada[1]), m2)
        print("")
        print("---------------------------------")
        print("Desencriptacion: ",desencriptadoM)
        print("---------------------------------")
        print("")
    
    else:
        print("Gracias por confiar en nosotross")
        bandera = False
