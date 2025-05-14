import pytest
from proceso import Proceso

def test_creacion_proceso_valido():
    Proceso.reset_pids()
    p = Proceso("P1", 5, 1)
    assert p.pid == "P1"
    assert p.duracion == 5
    assert p.prioridad == 1
    assert p.tiempo_restante == 5
    assert p.tiempo_inicio is None

def test_pid_duplicado():
    Proceso.reset_pids()
    Proceso("P1", 5, 1)
    with pytest.raises(ValueError):
        Proceso("P1", 3, 2)

def test_duracion_invalida():
    Proceso.reset_pids()
    with pytest.raises(ValueError):
        Proceso("P2", 0, 1)

def test_prioridad_invalida():
    Proceso.reset_pids()
    with pytest.raises(ValueError):
        Proceso("P3", 5, "alta")