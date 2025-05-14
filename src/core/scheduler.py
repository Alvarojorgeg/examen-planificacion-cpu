from abc import ABC, abstractmethod
from typing import List, Tuple
from core.proceso import Proceso

# Tipo de entrada del diagrama de Gantt
GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt = []

        for proceso in procesos:
            proceso.tiempo_inicio = tiempo_actual
            tiempo_final = tiempo_actual + proceso.duracion
            proceso.tiempo_fin = tiempo_final
            gantt.append((proceso.pid, tiempo_actual, tiempo_final))
            tiempo_actual = tiempo_final

        return gantt

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser mayor a 0")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt = []
        cola = procesos.copy()

        while any(p.tiempo_restante > 0 for p in cola):
            for proceso in cola:
                if proceso.tiempo_restante > 0:
                    if proceso.tiempo_inicio is None:
                        proceso.tiempo_inicio = tiempo_actual
                    tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
                    gantt.append((proceso.pid, tiempo_actual, tiempo_actual + tiempo_ejecucion))
                    proceso.tiempo_restante -= tiempo_ejecucion
                    tiempo_actual += tiempo_ejecucion
                    if proceso.tiempo_restante == 0:
                        proceso.tiempo_fin = tiempo_actual

        return gantt
