import tkinter as tk
from tkinter import messagebox, ttk
import os

def volver_ventana_principal():
    messagebox.showinfo("Página Principal", "Redirigiendo a Página Principal")
    ventana.quit()
    ventana.destroy()
    os.system("python BarrabacesFC/Vistas/principal.py")
    
    # Configuración de la ventana principal.
ventana = tk.Tk()
ventana.title("Control de Usuarios - Barrabases FC")
ventana.geometry("600x400")
    
    # Etiqueta de título
titulo = tk.Label(ventana, text="Elija tipo de usuario", font=("Arial", 16, "bold"))
titulo.pack(pady=10)
    
    # Frame para selección de operación
frame_operacion = tk.Frame(ventana)
frame_operacion.pack(pady=10)
    
    # Botones de operación (Ingresar, Modificar, Eliminar)
operacion = tk.StringVar()
btn_ingresar = tk.Radiobutton(frame_operacion, text="Ingresar", variable=operacion, value="Ingresar", indicatoron=0, width=10, font=("Arial", 12), bg="#66B2FF")
btn_modificar = tk.Radiobutton(frame_operacion, text="Modificar", variable=operacion, value="Modificar", indicatoron=0, width=10, font=("Arial", 12), bg="#66B2FF")
btn_eliminar = tk.Radiobutton(frame_operacion, text="Eliminar", variable=operacion, value="Eliminar", indicatoron=0, width=10, font=("Arial", 12), bg="#66B2FF")
    
btn_ingresar.grid(row=0, column=0, padx=5)
btn_modificar.grid(row=0, column=1, padx=5)
btn_eliminar.grid(row=0, column=2, padx=5)
    
    # Frame para selección de usuario
frame_usuario = tk.Frame(ventana)
frame_usuario.pack(pady=10)
    
    # Botones de usuario (Profesor, Alumno, Apoderado)
tipo_usuario = tk.StringVar()
btn_profesor = tk.Radiobutton(frame_usuario, text="Profesor", variable=tipo_usuario, value="Profesor", indicatoron=0, width=10, font=("Arial", 12), bg="#D1B2FF")
btn_alumno = tk.Radiobutton(frame_usuario, text="Alumno", variable=tipo_usuario, value="Alumno", indicatoron=0, width=10, font=("Arial", 12), bg="#D1B2FF")
btn_apoderado = tk.Radiobutton(frame_usuario, text="Apoderado", variable=tipo_usuario, value="Apoderado", indicatoron=0, width=10, font=("Arial", 12), bg="#D1B2FF")
    
btn_profesor.grid(row=0, column=0, padx=5)
btn_alumno.grid(row=0, column=1, padx=5)
btn_apoderado.grid(row=0, column=2, padx=5)
    
    # Frame para el formulario dinámico
frame_formulario = tk.Frame(ventana, bd=1, relief="solid", padx=10, pady=10)
frame_formulario.pack(pady=10, fill="x", padx=10)
    
    # Etiquetas y entradas dinámicas (inicialmente ocultas)
labels = ["Rut", "Nombre", "Dirección", "Año de nacimiento", "Año de incorporación"]
entradas = []
    
for label_text in labels:
    frame = tk.Frame(frame_formulario)
    frame.pack(fill="x", pady=5)
        
    label = tk.Label(frame, text=f"{label_text}:")
    label.pack(side="left")
        
    entry = tk.Entry(frame, width=40)
    entry.pack(side="right", padx=5)
        
    entradas.append(entry)
    
    # Campos adicionales para "Alumno"
frame_adicional_alumno = tk.Frame(frame_formulario)
    
label_posicion = tk.Label(frame_adicional_alumno, text="Posición:")
combo_posicion = ttk.Combobox(frame_adicional_alumno, values=["Delantero", "Mediocampista", "Defensa", "Portero"])
    
label_apoderado = tk.Label(frame_adicional_alumno, text="Apoderado:")
combo_apoderado = ttk.Combobox(frame_adicional_alumno)
    
label_profesor = tk.Label(frame_adicional_alumno, text="Profesor:")
combo_profesor = ttk.Combobox(frame_adicional_alumno)
    
label_posicion.grid(row=0, column=0, sticky="w", pady=5)
combo_posicion.grid(row=0, column=1, padx=5)
label_apoderado.grid(row=1, column=0, sticky="w", pady=5)
combo_apoderado.grid(row=1, column=1, padx=5)
label_profesor.grid(row=2, column=0, sticky="w", pady=5)
combo_profesor.grid(row=2, column=1, padx=5)
    
    # Función para actualizar el formulario según el tipo de usuario
def actualizar_formulario(*args):
    # Ocultar campos adicionales de alumno
    frame_adicional_alumno.pack_forget()
        
    if tipo_usuario.get() == "Alumno":
        frame_adicional_alumno.pack(fill="x", pady=5)
    
# Cambio en selección de usuario con la función de actualización
tipo_usuario.trace_add("write", actualizar_formulario)
    
    # Botón para confirmar la operación
btn_confirmar = tk.Button(ventana, text="Ingresar", bg="#66CCFF", font=("Arial", 12, "bold"))
btn_confirmar.pack(pady=10)

    
ventana.mainloop()

# Ejecutar el código de control de usuarios
control_usuarios()