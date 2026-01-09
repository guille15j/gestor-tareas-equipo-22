from colorama import Fore, Style
import os

def marcar_completada(fichero):
    """Marca una tarea como completada."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "=== MARCAR TAREA COMO COMPLETADA ===")
    print(Fore.CYAN + "=" * 40)
    
    try:
        if not os.path.exists(fichero):
            print(Fore.MAGENTA + "No hay tareas registradas.")
            input(Fore.CYAN + "Presiona Enter para continuar...")
            return
        
        with open(fichero, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        if not lineas:
            print(Fore.MAGENTA + "No hay tareas registradas.")
            input(Fore.CYAN + "Presiona Enter para continuar...")
            return
        
        print(Fore.WHITE + "LISTA DE TAREAS:")
        tareas = []
        for i, linea in enumerate(lineas, 1):
            linea = linea.strip()
            if '|' in linea:
                estado, texto = linea.split('|', 1)
                tareas.append({'numero': i, 'estado': estado, 'texto': texto})
                
                if estado == '1':
                    print(Fore.GREEN + f"  {i:2d}. [✓] {texto}")
                else:
                    print(Fore.YELLOW + f"  {i:2d}. [ ] {texto}")
        
        try:
            num_input = input(Fore.WHITE + "Número de tarea a marcar como completada (0 para cancelar): " + Style.RESET_ALL)
            
            if num_input == '0':
                print(Fore.BLUE + "Operación cancelada.")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return
            
            num = int(num_input)
            
            if num < 1 or num > len(tareas):
                print(Fore.RED + f"Error: El número {num} está fuera del rango (1-{len(tareas)})")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return
        
            tarea_seleccionada = tareas[num-1]
            
            if tarea_seleccionada['estado'] == '1':
                print(Fore.YELLOW + f"La tarea '{tarea_seleccionada['texto']}' ya está completada.")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return

            nuevas_lineas = []
            for i, linea in enumerate(lineas):
                linea = linea.strip()
                if '|' in linea:
                    estado, texto = linea.split('|', 1)
                    if i == num - 1: 
                        nuevas_lineas.append(f"1|{texto}")
                    else:
                        nuevas_lineas.append(f"{estado}|{texto}")
            
            with open(fichero, 'w', encoding='utf-8') as file:
                file.write('\n'.join(nuevas_lineas) + '\n')
            
            print(Fore.GREEN + f"Tarea '{tarea_seleccionada['texto']}' marcada como COMPLETADA!")
            print(Fore.GREEN + "   ¡Buen trabajo! ")
            
        except ValueError:
            print(Fore.RED + "\Error: Debes ingresar un número válido")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")
    
    except Exception as e:
        print(Fore.RED + f"Error al procesar las tareas: {e}")
    
    input(Fore.CYAN + "\nPresiona Enter para continuar...")
    pass

def eliminar_tarea(fichero):
    """Elimina una tarea del fichero."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "=== ELIMINAR TAREA ===")
    print(Fore.CYAN + "=" * 40)
    
    try:
        # Verificar si el archivo existe
        if not os.path.exists(fichero):
            print(Fore.MAGENTA + "No hay tareas registradas.")
            input(Fore.CYAN + "Presiona Enter para continuar...")
            return
        
        with open(fichero, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        if not lineas:
            print(Fore.MAGENTA + "No hay tareas registradas.")
            input(Fore.CYAN + "Presiona Enter para continuar...")
            return
        
        print(Fore.WHITE + "LISTA DE TAREAS:")
        tareas = []
        for i, linea in enumerate(lineas, 1):
            linea = linea.strip()
            if '|' in linea:
                estado, texto = linea.split('|', 1)
                tareas.append({'numero': i, 'estado': estado, 'texto': texto})
                
                if estado == '1':
                    print(Fore.GREEN + f"  {i:2d}. [✓] {texto}")
                else:
                    print(Fore.YELLOW + f"  {i:2d}. [ ] {texto}")
        
        print(Fore.CYAN + "\n" + "-" * 40)
        print(Fore.RED + "ADVERTENCIA: Esta acción no se puede deshacer")
        print(Fore.CYAN + "-" * 40)
        
        try:
            num_input = input(Fore.WHITE + "Número de tarea a ELIMINAR (0 para cancelar): " + Style.RESET_ALL)
            
            if num_input == '0':
                print(Fore.BLUE + "Operación cancelada.")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return
            
            num = int(num_input)
            
            if num < 1 or num > len(tareas):
                print(Fore.RED + f"Error: El número {num} está fuera del rango (1-{len(tareas)})")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return
            
            tarea_a_eliminar = tareas[num-1]
            print(Fore.YELLOW + f"¿Estás seguro de eliminar esta tarea?")
            if tarea_a_eliminar['estado'] == '1':
                print(Fore.GREEN + f"  [{num}] [✓] {tarea_a_eliminar['texto']}")
            else:
                print(Fore.YELLOW + f"  [{num}] [ ] {tarea_a_eliminar['texto']}")
            
            confirmar = input(Fore.RED + "\nEscribe 'SI' para confirmar eliminación: " + Style.RESET_ALL)
            
            if confirmar.upper() != 'SI':
                print(Fore.BLUE + "Eliminación cancelada.")
                input(Fore.CYAN + "Presiona Enter para continuar...")
                return
            
            nuevas_lineas = []
            for i, linea in enumerate(lineas):
                linea = linea.strip()
                if '|' in linea:
                    estado, texto = linea.split('|', 1)
                    if i != num - 1:  
                        nuevas_lineas.append(f"{estado}|{texto}")
            
            with open(fichero, 'w', encoding='utf-8') as file:
                if nuevas_lineas:  
                    file.write('\n'.join(nuevas_lineas) + '\n')
                else:
                    file.write('')  # Archivo vacío si no quedan tareas
            
            print(Fore.GREEN + f"¡Tarea '{tarea_a_eliminar['texto']}' ELIMINADA correctamente!")
            print(Fore.GREEN + f" Tareas restantes: {len(nuevas_lineas)}")
            
        except ValueError:
            print(Fore.RED + "xError: Debes ingresar un número válido")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")
    
    except Exception as e:
        print(Fore.RED + f"Error al procesar las tareas: {e}")

    input(Fore.CYAN + "Presiona Enter para continuar...") 
    pass

def despedida():
    """Muestra mensaje de despedida."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.CYAN + "╔══════════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.YELLOW + "                GESTOR DE TAREAS v1.0                " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠══════════════════════════════════════════════════════╣")
    print(Fore.CYAN + "║" + Fore.MAGENTA + "       ¡Gracias por usar nuestro programa!         " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.MAGENTA + "        Esperamos que te haya sido útil.           " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠══════════════════════════════════════════════════════╣")
    print(Fore.CYAN + "║" + Fore.WHITE + "                 EQUIPO DE DESARROLLO                " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "        • Alumno A - Funcionalidades básicas         " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "        • Alumno B - Funciones de modificación       " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠══════════════════════════════════════════════════════╣")
    print(Fore.CYAN + "║" + Fore.YELLOW + "            ¡Hasta la próxima!                    " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════════════╝")
    
    print(Fore.CYAN + "\n" + "═" * 55)
    print(Fore.WHITE +Fore.YELLOW + "Fecha de desarrollo: Diciembre 2025 - Enero 2026")
    print(Fore.WHITE +Fore.GREEN + "Lenguaje: Python 3.x")
    print(Fore.WHITE +Fore.MAGENTA + "Librerías: Colorama")
    
    print(Fore.YELLOW + "           ¡PROGRAMA FINALIZADO!")
    print(Fore.RED + Style.RESET_ALL)
    
    import time
    time.sleep(1)
    pass