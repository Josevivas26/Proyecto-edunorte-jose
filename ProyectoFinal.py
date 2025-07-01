import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import seaborn as sns
import threading
import time
import hashlib

# ===============================
# AUTENTICACIÓN CON GOOGLE SHEETS
# ===============================
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(
    r'C:\Users\HP-18\Desktop\ProyectoFinal\inventario-zapateria-credenciales.json',
    scopes=scope
)
client = gspread.authorize(creds)
sheet = client.open("Inventario Zapatería").sheet1

# ====================
# LECTURA DE DATOS
# ====================
def cargar_datos():
    records = sheet.get_all_records()
    df = pd.DataFrame(records)
    df["Marca_Modelo"] = df["Marca"] + " - " + df["Modelo"]
    df["ValorTotal"] = df["Cantidad"] * df["Precio"]
    valor_total_por_modelo = df.groupby("Marca_Modelo")["ValorTotal"].sum()
    cantidad_por_modelo = df.groupby("Marca_Modelo")["Cantidad"].sum()
    df["Marca_Modelo_Valor"] = df["Marca_Modelo"].apply(lambda mm: f"{mm} (${int(valor_total_por_modelo[mm]):,})")
    df["Marca_Modelo_Cantidad"] = df["Marca_Modelo"].apply(lambda mm: f"{mm} ({cantidad_por_modelo[mm]})")
    return df

# ====================
# ESTILO Y COLORES
# ====================
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8')
colors = sns.color_palette("husl", 10)  # Paleta de colores más moderna
button_color = "#4e79a7"  # Azul profesional
hover_color = "#f28e2b"   # Naranja para hover
active_color = "#e15759"  # Rojo para activar

# ====================
# FUNCIONES DE GRÁFICAS
# ====================
def plot1(ax):
    ax.clear()
    sns.barplot(data=df, x="ValorTotal", y="Categoría", hue="Marca_Modelo_Valor", 
                ax=ax, palette=colors, width=0.8, dodge=True, edgecolor=".2", linewidth=0.5)
    ax.set_title("Valor Total por Categoría (Marca - Modelo)", fontsize=14, pad=20)
    ax.set_xlabel("Valor Total (COP)", fontsize=12)
    ax.set_ylabel("Categoría", fontsize=12)
    ax.legend(title="Marca - Modelo", bbox_to_anchor=(1.05, 1), loc='upper left', 
              frameon=True, framealpha=0.9)
    plt.tight_layout()

def plot2(ax):
    ax.clear()
    sns.barplot(data=df, x="Cantidad", y="Categoría", hue="Marca_Modelo_Cantidad", 
                ax=ax, palette=colors, width=0.8, dodge=True, edgecolor=".2", linewidth=0.5)
    ax.set_title("Cantidad por Categoría (Marca - Modelo)", fontsize=14, pad=20)
    ax.set_xlabel("Cantidad", fontsize=12)
    ax.set_ylabel("Categoría", fontsize=12)
    ax.legend(title="Marca - Modelo", bbox_to_anchor=(1.05, 1), loc='upper left',
              frameon=True, framealpha=0.9)
    plt.tight_layout()

def plot3(ax):
    ax.clear()
    sns.barplot(data=df, x="Talla", y="Cantidad", hue="Marca_Modelo_Cantidad", 
                ax=ax, palette=colors, width=0.8, edgecolor=".2", linewidth=0.5)
    ax.set_title("Cantidad por Talla y Modelo", fontsize=14, pad=20)
    ax.set_xlabel("Talla", fontsize=12)
    ax.set_ylabel("Cantidad", fontsize=12)
    ax.legend(title="Marca - Modelo", bbox_to_anchor=(1.05, 1), loc='upper left',
              frameon=True, framealpha=0.9)
    plt.tight_layout()

def plot4(ax):
    ax.clear()
    sns.barplot(data=df, x="Cantidad", y="Color", hue="Marca_Modelo_Cantidad", 
                ax=ax, palette=colors, width=0.8, edgecolor=".2", linewidth=0.5)
    ax.set_title("Cantidad por Color y Modelo", fontsize=14, pad=20)
    ax.set_xlabel("Cantidad", fontsize=12)
    ax.set_ylabel("Color", fontsize=12)
    ax.legend(title="Marca - Modelo", bbox_to_anchor=(1.05, 1), loc='upper left',
              frameon=True, framealpha=0.9)
    plt.tight_layout()

plots = [plot1, plot2, plot3, plot4]

# ====================
# ACTUALIZAR PLOT
# ====================
def update_plot():
    global df
    plots[plot_index[0]](ax)
    fig.canvas.draw_idle()

# ====================
# REFRESCO AUTOMÁTICO
# ====================
def get_df_hash(df):
    return hashlib.md5(pd.util.hash_pandas_object(df, index=True).values).hexdigest()

def auto_refresh(interval=3):
    global df
    while True:
        time.sleep(interval)
        new_df = cargar_datos()
        new_hash = get_df_hash(new_df)
        if new_hash != last_hash[0]:
            df = new_df
            last_hash[0] = new_hash
            update_plot()

# ====================
# FUNCIONES DE BOTONES
# ====================
def next_plot(event):
    plot_index[0] = (plot_index[0] + 1) % len(plots)
    update_plot()

def prev_plot(event):
    plot_index[0] = (plot_index[0] - 1) % len(plots)
    update_plot()

def save_plot(event):
    filename = f"grafica_{plot_index[0]+1}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    print(f"Gráfica guardada como {filename}")

# ====================
# VENTANA PRINCIPAL
# ====================
fig, ax = plt.subplots(figsize=(16, 9))
plt.subplots_adjust(left=0.1, right=0.7, bottom=0.15)
plot_index = [0]
last_hash = [None]
df = cargar_datos()
plots[plot_index[0]](ax)
last_hash[0] = get_df_hash(df)

# Configuración de botones
button_style = {
    'color': 'white',
    'backgroundcolor': button_color,
    'hovercolor': hover_color,
    'labelcolor': 'white',
    'fontsize': 12,
    'borderwidth': 0.5,
    'borderradius': 4
}

# Crear botones
ax_save = plt.axes([0.7, 0.05, 0.21, 0.06])
ax_prev = plt.axes([0.7, 0.12, 0.1, 0.06])
ax_next = plt.axes([0.81, 0.12, 0.1, 0.06])

b_save = Button(ax_save, 'GUARDAR GRÁFICO', **button_style)
b_save.on_clicked(save_plot)

b_prev = Button(ax_prev, 'ANTERIOR ◄', **button_style)
b_prev.on_clicked(prev_plot)

b_next = Button(ax_next, 'SIGUIENTE ►', **button_style)
b_next.on_clicked(next_plot)

# Mejorar el hover de los botones
for btn in [b_save, b_prev, b_next]:
    btn.hovercolor = hover_color
    btn.color = button_color
    btn.label.set_fontweight('bold')

# Lanzar hilo de refresco
threading.Thread(target=lambda: auto_refresh(3), daemon=True).start()

plt.show()