from src.gui.interface import InterfazPlanificador
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    app = InterfazPlanificador(root)
    root.mainloop()