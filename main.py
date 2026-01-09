from colorama import init, Fore, Style
from alumno_a.funciones import mostrar_menu, ver_tareas, añadir_tarea
from alumno_b.funciones import marcar_completada, eliminar_tarea, despedida
import os

# Menu funcional
init()

def main():

    fichero = input("Introduce la ruta completa del archivo (incluye el nombre y .txt): ")

    if os.path.exists(fichero):
        print(Fore.GREEN + "El archivo ya existe en esa ruta." + Style.RESET_ALL)
    else:
        try:
            open(fichero, "w").close()
            print(Fore.YELLOW + f"Archivo creado en: {fichero}" + Style.RESET_ALL)
        except:
            print(Fore.RED + "No se pudo crear el archivo. Revisa la ruta." + Style.RESET_ALL)

    
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            ver_tareas(fichero)
        elif opcion == 2:
            añadir_tarea(fichero)
        elif opcion == 3:
            marcar_completada(fichero)
        elif opcion == 4:
            eliminar_tarea(fichero)
        elif opcion == 5:
            despedida()
            break 


main()
