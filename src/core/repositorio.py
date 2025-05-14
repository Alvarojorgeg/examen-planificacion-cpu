import json
import csv
from typing import List
from proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self._procesos = []

    def agregar(self, proceso: Proceso):
        if any(p.pid == proceso.pid for p in self._procesos):
            raise ValueError(f"Ya existe un proceso con PID '{proceso.pid}'")
        self._procesos.append(proceso)

    def eliminar(self, pid: str):
        self._procesos = [p for p in self._procesos if p.pid != pid]

    def obtener(self, pid: str) -> Proceso:
        for p in self._procesos:
            if p.pid == pid:
                return p
        raise ValueError(f"No existe un proceso con PID '{pid}'")

    def listar(self) -> List[Proceso]:
        return self._procesos

    def guardar_json(self, ruta: str):
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump([self._to_dict(p) for p in self._procesos], f, indent=4)

    def cargar_json(self, ruta: str):
        from proceso import Proceso
        Proceso.reset_pids()  # <--- Limpieza antes de cargar
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        self._procesos = [self._from_dict(d) for d in datos]

    def guardar_csv(self, ruta: str):
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for p in self._procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, ruta: str):
        from proceso import Proceso
        Proceso.reset_pids()  # <--- Limpieza antes de cargar
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            self._procesos = [
                Proceso(row['pid'], int(row['duracion']), int(row['prioridad']))
                for row in reader
            ]

    def _to_dict(self, proceso: Proceso):
        return {
            'pid': proceso.pid,
            'duracion': proceso.duracion,
            'prioridad': proceso.prioridad
        }

    def _from_dict(self, data: dict) -> Proceso:
        return Proceso(data['pid'], data['duracion'], data['prioridad'])
