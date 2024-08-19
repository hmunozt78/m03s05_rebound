#permito el uso de comandos del sistema operativo
from os import system

while True:
    #Limpio la pantalla
    system("cls")

    #Inicializo variables locales
    resultado = int(1)
    contador = int()

    #Pido el numero, y tomo lectura de teclado
    valor=int(input("ingrese el numero del que desea factorial :"))
    #x=int(1)
    for x in range(valor):
        contador+=1
        resultado = resultado * contador

    print(resultado)

    #Pido informacion di desea otro calculo y lo paso a minusculas para la comparacion
    otraVez=input("Desea otro calculo? (S = Si, Cualquier otro = NO)").lower()

    if otraVez != "s":
        print("Hasta Pronto")
        break

    
