import os
import sys

def get_process_info(process_id):
    try:
        # Obtener información del proceso
        process_info = os.popen(f"ps -p {process_id} -o comm=,pid=,ppid=,user=,%cpu=,%mem=,stat=").read().strip()
        
        # Obtener path ejecutable
        executable_path = os.readlink(f"/proc/{process_id}/exe")

        # Verificar si la información y el path son válidos
        if not process_info or not executable_path:
            print(f"ID {process_id} no encontrado")
            sys.exit(1)

        # Extraer información
        process_name, process_pid, parent_pid, user, cpu_usage, mem_usage, status = process_info.split()

        # Imprimir la información
        print(f"Nombre del proceso: {process_name}")
        print(f"ID del proceso: {process_pid}")
        print(f"Parent process ID: {parent_pid}")
        print(f"Usuario propietario: {user}")
        print(f"Porcentaje de CPU: {cpu_usage}%")
        print(f"Consumo de memoria: {mem_usage}%")
        print(f"Estado: {status}")
        print(f"Path del ejecutable: {executable_path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Comprobar si se proporciona el ID del proceso como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <ID de proceso>")
        sys.exit(1)

    process_id = sys.argv[1]
    get_process_info(process_id)
