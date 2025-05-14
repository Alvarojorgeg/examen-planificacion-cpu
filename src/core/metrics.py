from typing import List, Dict, Tuple
from core.proceso import Proceso


GanttEntry = Tuple[str, int, int]

def calcular_metricas(procesos: List[Proceso]) -> Dict[str, float]:
    tiempos_respuesta = []
    tiempos_retorno = []
    tiempos_espera = []

    for p in procesos:
        if p.tiempo_inicio is None or p.tiempo_fin is None:
            continue  # Saltar procesos no ejecutados

        respuesta = p.tiempo_inicio - p.tiempo_llegada
        retorno = p.tiempo_fin - p.tiempo_llegada
        espera = retorno - p.duracion

        tiempos_respuesta.append(respuesta)
        tiempos_retorno.append(retorno)
        tiempos_espera.append(espera)

    n = len(tiempos_respuesta)
    if n == 0:
        return {"respuesta_prom": 0, "retorno_prom": 0, "espera_prom": 0}

    return {
        "respuesta_prom": sum(tiempos_respuesta) / n,
        "retorno_prom": sum(tiempos_retorno) / n,
        "espera_prom": sum(tiempos_espera) / n
    }