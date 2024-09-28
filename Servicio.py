import subprocess
import time
import psutil

def checar_Proceso(nombre_Proceso):
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == nombre_Proceso:
            return True
    return False

def iniciar_Proceso(ruta_Proceso):
    subprocess.Popen(ruta_Proceso)

def parar_Proceso(nombre_Proceso):
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == nombre_Proceso:
            proceso.kill()

if __name__ == '__main__':
    nombre_Proceso = 'Adivinanza.exe'  
    ruta_Proceso = r'F:\2024A\Estatus\dist\Adivinanza.exe'  

    while True:
        if not checar_Proceso(nombre_Proceso):
            iniciar_Proceso(ruta_Proceso)
        else:
            parar_Proceso(nombre_Proceso)

        time.sleep(5)  