class Proceso:
    _pids_existentes = set()  # Clase para verificar unicidad de PID

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if pid in Proceso._pids_existentes:
            raise ValueError(f"El PID '{pid}' ya existe.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if not isinstance(prioridad, int):
            raise ValueError("La prioridad debe ser un número entero.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad

        # Atributos adicionales
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0  # simplificación
        self.tiempo_inicio = None
        self.tiempo_fin = None

        Proceso._pids_existentes.add(pid)

    def __repr__(self):
        return (f"Proceso(pid={self.pid}, duracion={self.duracion}, prioridad={self.prioridad}, "
                f"restante={self.tiempo_restante}, inicio={self.tiempo_inicio}, fin={self.tiempo_fin})")

    @classmethod
    def reset_pids(cls):
        """Resetea los PID existentes. Útil para pruebas unitarias."""
        cls._pids_existentes.clear()
