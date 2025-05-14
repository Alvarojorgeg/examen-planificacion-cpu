import pytest
from proceso import Proceso
from scheduler import FCFSScheduler, RoundRobinScheduler

@pytest.fixture
def procesos_simples():
    Proceso.reset_pids()
    return [
        Proceso("P1", 4, 1),
        Proceso("P2", 3, 2),
        Proceso("P3", 2, 3)
    ]

def test_fcfs_scheduler(procesos_simples):
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(procesos_simples)

    assert gantt == [
        ("P1", 0, 4),
        ("P2", 4, 7),
        ("P3", 7, 9)
    ]

def test_round_robin_scheduler(procesos_simples):
    scheduler = RoundRobinScheduler(quantum=2)
    gantt = scheduler.planificar(procesos_simples)

    # Gantt válido pero simplificado (solo verificación básica)
    pids = [entry[0] for entry in gantt]
    assert set(pids) == {"P1", "P2", "P3"}
    assert all(isinstance(entry[1], int) and isinstance(entry[2], int) for entry in gantt)