
import tkinter as tk
from tkinter import messagebox
import random

class JuegoBatalla:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalla Épica ⚔️")
        self.DD = 90  # Vida PC
        self.EE = 100 # Vida Usuario
        self.i = 3    # Ataques fuertes PC
        self.j = 3    # Ataques fuertes Usuario

        self.crear_interfaz()

    def crear_interfaz(self):
        self.info_label = tk.Label(self.root, text="¡Presiona el botón para iniciar el turno!", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.vida_label = tk.Label(self.root, text=self.obtener_texto_vida(), font=("Arial", 12))
        self.vida_label.pack()

        self.boton_turno = tk.Button(self.root, text="🎲 Iniciar Turno", command=self.turno)
        self.boton_turno.pack(pady=10)

        self.frame_ataques = tk.Frame(self.root)
        self.boton_lanza = tk.Button(self.frame_ataques, text="🗡️ Lanzar Lanza (-10)", command=lambda: self.atacar_usuario("A"))
        self.boton_sable = tk.Button(self.frame_ataques, text="⚔️ Usar Sable (-15)", command=lambda: self.atacar_usuario("B"))

    def obtener_texto_vida(self):
        return f"Vida PC 🖥️: {self.DD}     Vida Usuario 👤: {self.EE}\nSables restantes ⚔️: {self.j}"

    def turno(self):
        if self.DD <= 0 or self.EE <= 0:
            return

        turno = random.randint(1, 2)
        if turno == 1:
            # Turno de la PC
            ataque = random.randint(1, 2)
            if ataque == 1:
                self.EE -= 10
                mensaje = "💥 La PC te ataca con una lanza (-10)"
            elif ataque == 2 and self.i > 0:
                self.EE -= 15
                self.i -= 1
                mensaje = "💥 La PC te ataca con un sable (-15)"
            else:
                self.EE -= 10
                mensaje = "💥 La PC te ataca con una lanza (-10)"
            messagebox.showinfo("Ataque de la PC", mensaje)
        else:
            # Turno del Usuario: mostrar botones
            self.info_label.config(text="¡Tu turno! Selecciona tu ataque:")
            self.frame_ataques.pack(pady=10)
            self.boton_lanza.pack(side="left", padx=5)
            self.boton_sable.pack(side="left", padx=5)
            return

        self.actualizar_estado()

    def atacar_usuario(self, tipo):
        if tipo == "A":
            self.DD -= 10
            mensaje = "💥 Atacaste con lanza (-10)"
        elif tipo == "B":
            if self.j > 0:
                self.DD -= 15
                self.j -= 1
                mensaje = f"💥 Atacaste con sable (-15)\n⚔️ Sables restantes: {self.j}"
            else:
                messagebox.showwarning("Sin sables", "¡Ya no tienes sables!")
                return
        messagebox.showinfo("Tu ataque", mensaje)

        self.frame_ataques.pack_forget()
        self.actualizar_estado()

    def actualizar_estado(self):
        self.vida_label.config(text=self.obtener_texto_vida())
        if self.DD <= 0 or self.EE <= 0:
            ganador = "EL USUARIO 👤" if self.EE > self.DD else "LA PC 🖥️"
            messagebox.showinfo("Fin del Juego", f"🏆 ¡El ganador es {ganador}!")
            self.boton_turno.config(state="disabled")
        else:
            self.info_label.config(text="¡Presiona el botón para iniciar el turno!")

root = tk.Tk()
juego = JuegoBatalla(root)
root.mainloop()
