import tkinter as tk  # Importa la biblioteca Tkinter para crear interfaces gráficas.
from tkinter import messagebox  # Importa el módulo messagebox para mostrar cuadros de diálogo.
import os  # Permite interactuar con el sistema operativo, como ejecutar comandos externos.

# Función de autenticación
def iniciar_sesion():
    # Obtiene el texto ingresado en el campo de usuario.
    usuario = entry_usuario.get()
    # Obtiene el texto ingresado en el campo de contraseña.
    contrasena = entry_contrasena.get()
    
    # Verificar credenciales
    if usuario == "admin" and contrasena == "1234":  # Comprueba si las credenciales coinciden con las predeterminadas.
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")  # Muestra un cuadro de mensaje indicando éxito.
        ventana.quit()  # Detiene la ejecución del bucle principal de la ventana actual.
        ventana.destroy()  # Cierra la ventana de login.
        os.system("python Vistas/principal.py")  # Ejecuta el archivo principal de la aplicación.
    else:
        # Si las credenciales no coinciden, muestra un mensaje de error.
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para manejar el marcador de posición al hacer clic en el campo de entrada.
def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:  # Verifica si el contenido del campo es igual al marcador de posición.
        entry.delete(0, tk.END)  # Borra el contenido del campo si coincide con el marcador de posición.
        entry.config(fg="white")  # Cambia el color del texto del campo a blanco.

# Función para restaurar el marcador de posición al perder el foco.
def on_focusout(entry, placeholder):
    if entry.get() == "":  # Verifica si el campo está vacío.
        entry.insert(0, placeholder)  # Restaura el marcador de posición si el campo está vacío.
        entry.config(fg="grey")  # Cambia el color del texto del campo a gris.

# Crear la ventana principal de inicio de sesión
ventana = tk.Tk()  # Crea una instancia de la ventana principal de Tkinter.
ventana.title("Inicio de Sesión - Barrabases FC")  # Establece el título de la ventana.
ventana.geometry("500x600")  # Define el tamaño de la ventana en píxeles.
ventana.config(bg="#1c1f33")  # Cambia el color de fondo de la ventana.

# Título principal de la aplicación
titulo = tk.Label(
    ventana,  # Asocia el título con la ventana principal.
    text="BARRABASES FC",  # Texto del título.
    font=("Arial", 24, "bold"),  # Fuente, tamaño y estilo del texto.
    bg="#1c1f33",  # Color de fondo del título.
    fg="white"  # Color del texto del título.
)
titulo.pack(pady=30)  # Empaqueta el título en la ventana con un margen vertical de 30 píxeles.

# Campo para ingresar el nombre de usuario
entry_usuario = tk.Entry(
    ventana,  # Asocia el campo con la ventana principal.
    font=("Arial", 14),  # Fuente y tamaño del texto.
    width=25,  # Ancho del campo en caracteres.
    justify="center"  # Centra el texto dentro del campo.
)
entry_usuario.insert(0, "NOMBRE DE USUARIO")  # Establece el marcador de posición inicial.
entry_usuario.config(fg="grey", bg="#3b4fe4", relief="flat")  # Configura colores y estilo visual del campo.
entry_usuario.bind("<FocusIn>", lambda event: on_entry_click(entry_usuario, "NOMBRE DE USUARIO"))  # Llama a `on_entry_click` al obtener el foco.
entry_usuario.bind("<FocusOut>", lambda event: on_focusout(entry_usuario, "NOMBRE DE USUARIO"))  # Llama a `on_focusout` al perder el foco.
entry_usuario.pack(pady=15)  # Empaqueta el campo con un margen vertical de 15 píxeles.

# Campo para ingresar la contraseña
entry_contrasena = tk.Entry(
    ventana,  # Asocia el campo con la ventana principal.
    font=("Arial", 14),  # Fuente y tamaño del texto.
    width=25,  # Ancho del campo en caracteres.
    justify="center"  # Centra el texto dentro del campo.
)
entry_contrasena.insert(0, "CONTRASEÑA")  # Establece el marcador de posición inicial.
entry_contrasena.config(fg="grey", bg="#324f6b", relief="flat")  # Configura colores y estilo visual del campo.
entry_contrasena.bind("<FocusIn>", lambda event: on_entry_click(entry_contrasena, "CONTRASEÑA"))  # Llama a `on_entry_click` al obtener el foco.
entry_contrasena.bind("<FocusOut>", lambda event: on_focusout(entry_contrasena, "CONTRASEÑA"))  # Llama a `on_focusout` al perder el foco.
entry_contrasena.pack(pady=15)  # Empaqueta el campo con un margen vertical de 15 píxeles.

# Botón para iniciar sesión
boton_ingresar = tk.Button(
    ventana,  # Asocia el botón con la ventana principal.
    text="INGRESAR",  # Texto mostrado en el botón.
    font=("Arial", 14, "bold"),  # Fuente, tamaño y estilo del texto.
    command=iniciar_sesion,  # Función llamada al hacer clic en el botón.
    width=15,  # Ancho del botón en caracteres.
    bg="white",  # Color de fondo del botón.
    fg="#1c1f33",  # Color del texto del botón.
)
boton_ingresar.pack(pady=30)  # Empaqueta el botón con un margen vertical de 30 píxeles.

# Inicia el bucle principal de la interfaz gráfica
ventana.mainloop()  # Mantiene la ventana abierta y responde a las interacciones del usuario.