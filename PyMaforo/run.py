import serial
import time

import os

clear = lambda: os.system('cls')
serial_port = 'COM4'
baudrate = 115200
go = True

def _ConnectToArduino():     
    arduino = serial.Serial(serial_port, baudrate, timeout=.1)
    time.sleep(2) #give the connection two seconds to settle
    return arduino

def _sendData(arduino,option):
    try:
        with arduino:
            arduino.write(option.encode()) #read the data from the arduino
    except:
        print("Failed to connect on")


# Iniciamos la función
while go:
    print("< ================================= >")
    print("Proyecto PySemaforo - Inicio")
    print("MENU")
    print("1. Ver Semaforos")
    print("0. Cerrar")
    option = input("Ingrese la opción: ");

    if option == '1':
        clear()
        print("< ================================= >")
        print("Proyecto PySemaforo - Semaforos")
        print("MENU")
        print("1. Area 201")
        print("2. Volver")
        option2 = input("Ingrese la opción: ");
        if option2 == '1':
            clear()
            print("< ================================= >")
            print("Proyecto PySemaforo - Area 201")
            print("MENU")
            print("1. Dar Paso")
            print("2. Dar Paso con Prioridad")
            print("3. Volver")
            option3 = input("Ingrese la opción: ");
            if option3 == '1':
                clear()
                print("Inicializando Función Dar Paso")
                _sendData(_ConnectToArduino(),'A')
            elif option3 == '2':
                clear()
                print("Inicializando Función Dar Paso con Prioridad")
                _sendData(_ConnectToArduino(),'B')
            else:
                print("Opción incorrecta, intente nuevamente.")
        elif option2 == '2':
            print("Listo")
        else:
            print("Opción incorrecta, intente nuevamente.")
    elif option == '0':
        clear()
        print("El sistema se cerrará en:")
        for i in [3,2,1]:
                print(i)
                time.sleep(0.5)
        time.sleep(2)
        print("Sistema cerrado correctamente :V")
        go = False
    else:
        print("Opción incorrecta, intente nuevamente.")
    


