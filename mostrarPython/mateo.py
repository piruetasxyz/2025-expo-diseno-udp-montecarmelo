import subprocess
import os
import time

# --- Configuración ---

# ¡IMPORTANTE! 
# Ajusta la resolución de tus monitores aquí.
MONITOR_1_RES = (1080, 1920)  # (ancho, alto) del Monitor 1
MONITOR_2_RES = (1080, 1920)  # (ancho, alto) del Monitor 2

# Coordenadas (x, y) de la esquina superior izquierda de cada monitor
# Monitor 1 (principal)
MONITOR_1_POS = (0, 0)
# Monitor 2 (a la derecha del 1)
# La 'x' es el ancho del Monitor 1. La 'y' es 0.
MONITOR_2_POS = (MONITOR_1_RES[0], 0) # e.g., (1920, 0)

# Rutas (usando tu usuario de la conversación anterior)
base_dir = "/home/discusiones01/2025-expo-diseno-udp-montecarmelo"
video1_path = os.path.join(base_dir, "data/placeholder.mp4")
video2_path = os.path.join(base_dir, "data/placeholder.mp4")

# Opciones de VLC para modo "kiosk" (fullscreen simulado)
vlc_options = [              # Sin controles en pantalla (OSD)
    '--loop',                  # Repetir el video indefinidamente
    '--no-video-title-show',   # No mostrar el título   
    '--video-filter=transform',  
    '--transform-type=-180',             
    '--no-video-deco',         # ¡CLAVE: Sin bordes ni título de ventana!
    '--video-on-top'           # (Opcional) Asegura que la ventana esté encima
]

# --- Ejecución ---

def launch_vlc(video_path, x, y, width, height):
    """
    Lanza una instancia de VLC en una posición y tamaño específicos,
    creando un efecto de "fullscreen" en ese monitor.
    """
    if not os.path.exists(video_path):
        print(f"Error: No se encuentra el video en {video_path}")
        return None
        
    command = [
        'vlc',
        video_path,
        f'--video-x={x}',
        f'--video-y={y}',
        f'--width={width}',
        f'--height={height}'
    ] + vlc_options
    
    print(f"Lanzando: {' '.join(command)}")
    # Popen ejecuta el comando en un proceso separado
    return subprocess.Popen(command)

# --- Lanzar Videos ---

# Lanzar video 1 en Monitor 1
proc1 = launch_vlc(video1_path, 
                   MONITOR_1_POS[0], MONITOR_1_POS[1], 
                   MONITOR_1_RES[0], MONITOR_1_RES[1])

# Pequeña pausa para que los procesos no compitan por los recursos
time.sleep(0.5) 

# Lanzar video 2 en Monitor 2
proc2 = launch_vlc(video2_path, 
                   MONITOR_2_POS[0], MONITOR_2_POS[1], 
                   MONITOR_2_RES[0], MONITOR_2_RES[1])

print("\nVideos lanzados en modo 'kiosk'.")
print("Este script se quedará corriendo para mantener vivos los procesos.")
print("Presiona Ctrl+C en esta terminal para detener ambos videos.")

try:
    # Mantenemos el script principal vivo
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Si el usuario presiona Ctrl+C
    print("\nCerrando procesos de VLC...")
    if proc1:
        proc1.terminate() # Pide amablemente a VLC que se cierre
    if proc2:
        proc2.terminate()
    print("Listo.")