import os
import sys
import time

def check_and_restart_process(process_name, command):
    try:
        while True:
            # Verificar si el proceso está en ejecución
            if any(process_name in line for line in os.popen("pgrep -fl " + process_name)):
                print(f"El proceso {process_name} está en ejecución.")
            else:
                print(f"El proceso {process_name} no está en ejecución. Reiniciando...")
                os.system(command)

            # Tiempo de espera para la próxima verificación
            time.sleep(30)

    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
        sys.exit(0)

if __name__ == "__main__":
    # Comprobar si se proporcionan el nombre del proceso y el comando como argumentos
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_del_proceso> <comando_de_ejecucion>")
        sys.exit(1)

    nombre_proceso = sys.argv[1]
    comando_ejecucion = sys.argv[2]

    check_and_restart_process(nombre_proceso, comando_ejecucion)
