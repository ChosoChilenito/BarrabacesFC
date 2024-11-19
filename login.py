import tkinter as tk
from tkinter import messagebox
import os # Permite interactuar con el sistema operativo

# Función de autenticación
def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    # Verificar credenciales
    if usuario == "admin" and contrasena == "1234": # Usuario y contraseña fija
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        ventana.quit()  # Detener la ventana de login.
        ventana.destroy()  # Cerrar la ventana de login.
        os.system("python BarrabacesFC/Vistas/principal.py")  # Abrir la ventana principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Marcador de posición
def on_entry_click(entry, placeholder):
    if entry.get() == placeholder: # Verifica si el texto actual del entry es igual al marcador de posición.
        entry.delete(0, tk.END) # Si es igual, elimina todo el texto del entry.
        entry.config(fg="white") 

def on_focusout(entry, placeholder):
    if entry.get() == "": # Verifica si el texto actual del entry está vacío.
        entry.insert(0, placeholder) # Si está vacío, inserta nuevamente el marcador de posición.
        entry.config(fg="grey") 


# Crear la ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de Sesión - Barrabases FC")
ventana.geometry("500x600")
ventana.config(bg="#1c1f33")

# Título
titulo = tk.Label(ventana, text="BARRABASES FC", font=("Arial", 24, "bold"), bg="#1c1f33", fg="white")
titulo.pack(pady=30)

# Campo de nombre de usuario
entry_usuario = tk.Entry(ventana, font=("Arial", 14), width=25, justify="center")
entry_usuario.insert(0, "NOMBRE DE USUARIO")
entry_usuario.config(fg="grey", bg="#3b4fe4", relief="flat")
entry_usuario.bind("<FocusIn>", lambda event: on_entry_click(entry_usuario, "NOMBRE DE USUARIO"))
entry_usuario.bind("<FocusOut>", lambda event: on_focusout(entry_usuario, "NOMBRE DE USUARIO"))
entry_usuario.pack(pady=15)

# Campo de contraseña
entry_contrasena = tk.Entry(ventana, font=("Arial", 14), width=25, justify="center")
entry_contrasena.insert(0, "CONTRASEÑA")
entry_contrasena.config(fg="grey", bg="#324f6b", relief="flat")
entry_contrasena.bind("<FocusIn>", lambda event: on_entry_click(entry_contrasena, "CONTRASEÑA"))
entry_contrasena.bind("<FocusOut>", lambda event: on_focusout(entry_contrasena, "CONTRASEÑA"))
entry_contrasena.pack(pady=15)

# Botón de ingresar
boton_ingresar = tk.Button(ventana, text="INGRESAR", font=("Arial", 14, "bold"), command=iniciar_sesion,
width=15, bg="white", fg="#1c1f33", relief="flat")

boton_ingresar.pack(pady=30)

ventana.mainloop()