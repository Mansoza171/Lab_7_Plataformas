import os
import sys
import time
import psutil
import matplotlib.pyplot as plt

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def monitor_process(ejecutable, duracion_monitoreo, log_file):
    start_time = time.time()

    # Inicializar el archivo de registro
    with open(log_file, 'a') as file:
        file.write("Tiempo CPU Memoria\n")

    while is_process_running(ejecutable):
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time <= duracion_monitoreo:
            process_pid = int(os.popen(f"pgrep -o {ejecutable}").read().strip())
            process = psutil.Process(process_pid)
            cpu_percent = process.cpu_percent(interval=1)
            mem_percent = process.memory_percent()

            with open(log_file, 'a') as file:
                file.write(f"{elapsed_time} {cpu_percent} {mem_percent}\n")

        else:
            break

    # Generar la gráfica con Matplotlib
    data = {'Tiempo': [], 'CPU': [], 'Memoria': []}
    with open(log_file, 'r') as file:
        next(file)  # Saltar la primera línea (encabezado)
        for line in file:
            tiempo, cpu, memoria = map(float, line.split())
            data['Tiempo'].append(tiempo)
            data['CPU'].append(cpu)
            data['Memoria'].append(memoria)

    if data['Tiempo']:
        plt.plot(data['Tiempo'], data['CPU'], label='CPU')
        plt.plot(data['Tiempo'], data['Memoria'], label='Memoria')
        plt.title(f'Consumo de CPU y Memoria de {ejecutable}')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Porcentaje')
        plt.legend()
        plt.savefig('grafica.png')
        plt.close()

        print("El monitoreo ha finalizado. Ver gráfico en 'grafica.png'.")
    else:
        print("No se registraron datos para generar la gráfica.")

if __name__ == "__main__":
    # Comprobar si se proporciona el nombre del ejecutable como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_ejecutable>")
        sys.exit(1)

    ejecutable = sys.argv[1]
    duracion_monitoreo = 60  # Duración predeterminada del monitoreo en segundos
    log_file = "monitoring.log"

    monitor_process(ejecutable, duracion_monitoreo, log_file)
