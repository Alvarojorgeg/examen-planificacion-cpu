import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from core.proceso import Proceso
from core.repositorio import RepositorioProcesos
from core.scheduler import FCFSScheduler, RoundRobinScheduler
from core.metrics import calcular_metricas

class InterfazPlanificador:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Planificación de CPU")
        self.root.geometry("700x500")

        self.repo = RepositorioProcesos()

        self.crear_widgets()

    def crear_widgets(self):
        # Marco superior para formulario
        frame_form = ttk.LabelFrame(self.root, text="Registrar Proceso")
        frame_form.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_form, text="PID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_pid = ttk.Entry(frame_form)
        self.entry_pid.grid(row=0, column=1)

        ttk.Label(frame_form, text="Duración:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_duracion = ttk.Entry(frame_form)
        self.entry_duracion.grid(row=0, column=3)

        ttk.Label(frame_form, text="Prioridad:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_prioridad = ttk.Entry(frame_form)
        self.entry_prioridad.grid(row=0, column=5)

        btn_agregar = ttk.Button(frame_form, text="Agregar Proceso", command=self.agregar_proceso)
        btn_agregar.grid(row=0, column=6, padx=10)

        # Tabla de procesos
        self.tree = ttk.Treeview(self.root, columns=("duracion", "prioridad"), show="headings")
        self.tree.heading("duracion", text="Duración")
        self.tree.heading("prioridad", text="Prioridad")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def agregar_proceso(self):
        pid = self.entry_pid.get()
        try:
            duracion = int(self.entry_duracion.get())
            prioridad = int(self.entry_prioridad.get())
            proceso = Proceso(pid, duracion, prioridad)
            self.repo.agregar(proceso)
            self.tree.insert('', 'end', iid=pid, values=(duracion, prioridad))
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.entry_pid.delete(0, tk.END)
            self.entry_duracion.delete(0, tk.END)
            self.entry_prioridad.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = InterfazPlanificador(root)
    root.mainloop()