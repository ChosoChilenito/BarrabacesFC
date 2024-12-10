import tkinter as tk
from tkinter import messagebox, ttk
import os

ventana = tk.Tk()
ventana.title("Entrenamiento - Barrabases FC")
ventana.geometry("600x700")
ventana.config(bg="#1c1f33")

titulo = tk.Label(ventana, text="Entrenamiento", font=("Arial", 24, "bold"), bg="#1c1f33", fg="white")
titulo.pack(pady=10)