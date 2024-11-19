def volver_ventana_principal():
    messagebox.showinfo("Página Principal", "Redirigiendo a Página Principal")
    ventana.quit()
    ventana.destroy()
    os.system("python BarrabacesFC/Vistas/principal.py")