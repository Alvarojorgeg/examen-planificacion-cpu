import os
import tempfile
from proceso import Proceso
from repositorio import RepositorioProcesos

def test_agregar_y_listar():
    Proceso.reset_pids()
    repo = RepositorioProcesos()
    p = Proceso("P1", 5, 1)
    repo.agregar(p)
    assert len(repo.listar()) == 1

def test_pid_duplicado_repo():
    Proceso.reset_pids()
    repo = RepositorioProcesos()
    repo.agregar(Proceso("P1", 4, 1))
    try:
        repo.agregar(Proceso("P1", 6, 2))
    except ValueError:
        assert True
    else:
        assert False

def test_guardar_y_cargar_json():
    Proceso.reset_pids()
    repo = RepositorioProcesos()
    repo.agregar(Proceso("P1", 5, 1))
    repo.agregar(Proceso("P2", 3, 2))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        ruta = tmp.name
    repo.guardar_json(ruta)

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json(ruta)
    assert len(nuevo_repo.listar()) == 2
    os.remove(ruta)

def test_guardar_y_cargar_csv():
    Proceso.reset_pids()
    repo = RepositorioProcesos()
    repo.agregar(Proceso("P1", 5, 1))
    repo.agregar(Proceso("P2", 3, 2))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        ruta = tmp.name
    repo.guardar_csv(ruta)

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_csv(ruta)
    assert len(nuevo_repo.listar()) == 2
    os.remove(ruta)