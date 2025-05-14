from proceso import Proceso
from metrics import calcular_metricas

def test_metricas_simples():
    Proceso.reset_pids()
    p1 = Proceso("P1", 4, 1)
    p2 = Proceso("P2", 3, 1)
    p3 = Proceso("P3", 2, 1)

    # Simulamos ejecución FCFS
    p1.tiempo_inicio, p1.tiempo_fin = 0, 4
    p2.tiempo_inicio, p2.tiempo_fin = 4, 7
    p3.tiempo_inicio, p3.tiempo_fin = 7, 9

    metricas = calcular_metricas([p1, p2, p3])

    assert metricas['respuesta_prom'] == (0 + 4 + 7) / 3
    assert metricas['retorno_prom'] == (4 + 7 + 9) / 3
    assert metricas['espera_prom'] == ((4-4) + (7-3) + (9-2)) / 3
