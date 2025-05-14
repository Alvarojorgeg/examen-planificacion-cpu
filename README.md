https://github.com/Alvarojorgeg/examen-planificacion-cpu

# Simulador de Planificación de CPU

Este repositorio contiene un proyecto en Python orientado a objetos para simular la planificación de procesos en un sistema operativo. Se implementan algoritmos de planificación, almacenamiento en disco y pruebas automatizadas.

Realizado por **Álvaro**, estudiante de Ingeniería Informática.

## 📁 Estructura del Proyecto

```
proyecto-scheduler/
├── src/
│   ├── proceso.py              # Clase Proceso
│   ├── scheduler.py            # FCFS y Round Robin
│   ├── repositorio.py          # Repositorio y persistencia JSON/CSV
│   ├── metrics.py              # Cálculo de métricas
│   └── main.py                 # (opcional) CLI interactivo
├── tests/
│   ├── test_proceso.py
│   ├── test_scheduler.py
│   ├── test_repositorio.py
│   └── test_metrics.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## ⚙️ Funcionalidades

- Registro de procesos con `PID`, duración y prioridad.
- Implementación de dos algoritmos de planificación:
  - **FCFS** (First-Come, First-Served)
  - **Round Robin** con quantum configurable
- Simulación con generación de diagrama de Gantt.
- Cálculo de métricas:
  - Tiempo de respuesta medio
  - Tiempo de retorno medio
  - Tiempo de espera medio
- Persistencia en archivos JSON y CSV.
- Pruebas unitarias con `pytest`.

## ▶️ Ejecución

### 1. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar pruebas
```bash
pytest
```

### 4. Ejecutar desde `main.py` (si se implementa interfaz CLI)
```bash
python src/main.py
```

## ✅ Requisitos

- Python 3.10 o superior
- `pytest` (ya incluido en `requirements.txt`)

## 📊 Ejemplo de Diagrama de Gantt
```
[("P1", 0, 4), ("P2", 4, 7), ("P3", 7, 9)]
```

## 📌 Notas

Este proyecto fue desarrollado como ejercicio práctico para reforzar conceptos de:
- Programación orientada a objetos
- Algoritmos de planificación de CPU
- Serialización de datos
- Diseño de pruebas automatizadas

---

💻 *Hecho con esfuerzo por Álvaro para la asignatura de Programación II.*
