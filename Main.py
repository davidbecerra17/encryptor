#===============================================#
# Programación logica y funcional               #
# Proyecto final: Encryptor                     #
# Desarrollador: David Enrique Becerra Ramirez  #
#===============================================#

#System libs
import os
import sys
import glob

#Custom libs
from src.IOHandler import read, save
from src.EncryptHandler import decrypt, encrypt
from src.PrologHandler import prolog_to_text, text_to_prolog

print("Encryptor")

class Main:

    def __init__(self) -> None:
        self.Menu()

    def Menu(self):
        self.Limpiar()

        menu_options = {
            1: 'Nuevo Mensaje',
            2: 'Abrir Mensaje',
            3: 'Salir',
        }

        for key in menu_options.keys():
            print(key,'--',menu_options[key])

        option = int(input('>> '))

        if option == 1:
            self.Nuevo_Mensaje()
        elif option == 2:
            self.Abrir_Mensaje()
        else:
            sys.exit

    def Nuevo_Mensaje(self):
        self.Limpiar()
        message = input("Ingrese el mensaje: ")
        password = input("Ingrese una contraseña: ")
        filename = input("Ingrese el nombre del archivo: ")
        message = encrypt(message,password)
        message = text_to_prolog(message)
        save(filename,message)
        self.Menu()


    def Abrir_Mensaje(self):
        self.Limpiar()
        print("Mensajes guardados")
        saved_files = glob.glob('Database/*.pl')
        for i in range(len(saved_files)):
            print(i + 1,'--',saved_files[i])
        option = int(input('>> '))
        choosen_file = saved_files[option-1]
        message_list = read(choosen_file)
        message = prolog_to_text(message_list)
        password = input("Ingrese la contraseña: ")
        message = decrypt(message,password)
        input("Mensaje: " + str(message) + "\nIngrese cualquier tecla para continuar")
        self.Menu()

    def Limpiar(self):
        os.system('cls')

main = Main()