from colorama import Fore, Style

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    # TODO: Implementar
    pass

def ver_tareas(fichero):
    """Muestra todas las tareas numeradas."""
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        
        if not lineas:
            print(f"{Fore.BLUE}No hay tareas en el fichero.{Style.RESET_ALL}")
            return

        i = 1
        for l in lineas:
            secciones = l.split('|')
            tarea = secciones[1].strip()

            if secciones[0] == '1':
                print(f"{i}. {Fore.CYAN}[ ]{Style.RESET_ALL} {tarea}")
            else:
                print(f"{i}. {Fore.GREEN}[✓]{Style.RESET_ALL} {tarea}")

            i += 1

    except FileNotFoundError:
        print(f"{Fore.RED}El archivo no existe todavía.{Style.RESET_ALL}")


def añadir_tarea(fichero):
    """Añade una nueva tarea al fichero."""
    # TODO: Implementar
    pass