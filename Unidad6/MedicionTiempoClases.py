import time
from reader import feed

class TimerError(Exception):
    """Custom exception for Timer class"""
    pass

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
    #Comienza un nuevo temporizador
        if self._start_time is not None:
            raise TimerError(f"El tiempo está corriendo. Usa .stop() para parar esto")
        self._start_time = time.perf_counter()

    def stop(self):
    #Detiene el tiempo y lo reporta
        if self._start_time is None:
            raise TimerError(f"El tiempo no está corriendo. Usa .start() para comenzarlo")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Tiempo: {elapsed_time:0.4f} segundos")
    
def main():
    # Print the latest tutorial from Real Python
    """Imprime el último tutorial de Python"""
    tic = time.perf_counter()
    try:
        tutorial = feed.get_article(0)
    except Exception as e:
        print(f"Error al obtener el artículo: {e}")
        return
    toc = time.perf_counter()
    print(f"El tutorial ha sido descargado en {toc - tic:0.4f} segundos")

    print(tutorial)

if __name__ == "__main__":
    main()