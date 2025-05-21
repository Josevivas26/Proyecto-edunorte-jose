import pywhatkit
import tkinter as tk

def send_message():
    phone_number = phone_entry.get()
    message = "Prueba de Python"
    time_hour = 11
    time_minute = 12
    waiting_time_to_send = 30
    close_tab = True
    waiting_time_to_close = 2
    
    if phone_number:
        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
    else:
        result_label.config(text="Por favor, ingresa un número válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Enviar Mensaje por WhatsApp")

# Crear y ubicar elementos de la interfaz
tk.Label(root, text="Número de teléfono:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

send_button = tk.Button(root, text="Enviar Mensaje", command=send_message)
send_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
