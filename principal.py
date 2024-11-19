import tkinter as tk
import os
from tkinter import messagebox

# Funciones de cada sección
def volver_ventana_principal():
    messagebox.showinfo("Página Principal", "Redirigiendo a Página Principal") #Ventana emergente de información
    ventana.quit()
    ventana.destroy()
    os.system("python BarrabacesFC/Vistas/principal.py")

def abrir_control_usuarios():
    messagebox.showinfo("Control de Usuarios", "Redirigiendo a Control de Usuarios") #Ventana emergente de información
    ventana.quit()  # Detener el mainloop de la ventana de login.
    ventana.destroy()  # Cerrar la ventana de login.
    os.system("python BarrabacesFC/Vistas/control_usuarios.py")  # Abrir la ventana principal como un nuevo proceso.

def abrir_lista_alumnos():
    messagebox.showinfo("Lista de Alumnos", "Redirigiendo a Lista de Alumnos") #Ventana emergente de información
    ventana.quit()  # Detener el mainloop de la ventana de login.
    ventana.destroy()  # Cerrar la ventana de login.
    os.system("python BarrabacesFC/Vistas/listado_alumnos.py")  # Abrir la ventana principal como un nuevo proceso.

def abrir_contactos():
    messagebox.showinfo("Contactos", "Redirigiendo a Contactos") #Ventana emergente de información
    ventana.quit()  # Detener el mainloop de la ventana de login.
    ventana.destroy()  # Cerrar la ventana de login.
    os.system("python BarrabacesFC/Vistas/contactos.py")  # Abrir la ventana principal como un nuevo proceso.

def abrir_ranking():
    messagebox.showinfo("Ranking", "Redirigiendo a Ranking") #Ventana emergente de información
    ventana.quit()  # Detener el mainloop de la ventana de login.
    ventana.destroy()  # Cerrar la ventana de login.
    os.system("python BarrabacesFC/Vistas/ranking.py")  # Abrir la ventana principal como un nuevo proceso.

def abrir_entrenamiento():
    messagebox.showinfo("Entrenamiento", "Redirigiendo a Entrenamiento") #Ventana emergente de información
    ventana.quit()  # Detener el mainloop de la ventana de login.
    ventana.destroy()  # Cerrar la ventana de login.
    os.system("python BarrabacesFC/Vistas/entrenamiento.py")  # Abrir la ventana principal como un nuevo proceso.

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Barrabases FC")
ventana.geometry("600x400")
ventana.config(bg="#1c1f33")  # Color de fondo similar al diseño

# Título principal
titulo = tk.Label(ventana, text="BARRABASES FC", font=("Arial", 24, "bold"), bg="#1c1f33", fg="white")
titulo.pack(pady=10)

# Contenedor para las secciones principales
frame_secciones = tk.Frame(ventana, bg="#1c1f33")
frame_secciones.pack(pady=20)

# Botones de las secciones
boton_control_usuarios = tk.Button(frame_secciones, text="CONTROL DE USUARIOS", font=("Arial", 12, "bold"), 
command=abrir_control_usuarios, bg="#3b4fe4", fg="white", width=20)

boton_control_usuarios.grid(row=0, column=0, padx=10, pady=10)

boton_lista_alumnos = tk.Button(frame_secciones, text="LISTA DE ALUMNOS", font=("Arial", 12, "bold"), 
command=abrir_lista_alumnos, bg="#324f6b", fg="white", width=20)

boton_lista_alumnos.grid(row=0, column=1, padx=10, pady=10)

boton_contactos = tk.Button(frame_secciones, text="CONTACTOS", font=("Arial", 12, "bold"), 
command=abrir_contactos, bg="#3b4fe4", fg="white", width=20)

boton_contactos.grid(row=1, column=0, padx=10, pady=10)

boton_ranking = tk.Button(frame_secciones, text="RANKING", font=("Arial", 12, "bold"), 
command=abrir_ranking, bg="#324f6b", fg="white", width=20)

boton_ranking.grid(row=1, column=1, padx=10, pady=10)

# Botón de entrenamiento en la parte inferior
boton_entrenamiento = tk.Button(ventana, text="ENTRENAMIENTO", font=("Arial", 12, "bold"), 
command=abrir_entrenamiento, bg="#2a2f49", fg="white", width=20)

boton_entrenamiento.pack(pady=10)

ventana.mainloop()