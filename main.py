from colorama import init, Fore, Style
from alumno_a.funciones import mostrar_menu, ver_tareas, añadir_tarea
from alumno_b.funciones import marcar_completada, eliminar_tarea, despedida
import os

# Menu funcional
init()

def main():
    fichero = "tareas.txt"
    if not os.path.exists(fichero):
        open(fichero, 'w').close()
        print(Fore.YELLOW + f"Archivo '{fichero}' creado correctamente.")
    
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
