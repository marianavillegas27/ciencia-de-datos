import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
import numpy as np

def prep_and_plot():
    print("Cargando la base de datos desde baselatin.csv...")
    # Cargar los datos guardados en CSV para evitar errores de objetos no soportados
    datos = pd.read_csv("baselatin.csv", low_memory=False)
    
    print("Filtrando datos para Colombia y Argentina...")
    # Filtrar país (Colombia = 170, Argentina = 32)
    latam = datos[datos['idenpa'].isin([170, 32])].copy()
    
    # Crear la columna 'pais' según el idenpa
    condiciones = [
        latam['idenpa'] == 170,
        latam['idenpa'] == 32
    ]
    valores = ["Colombia", "Argentina"]
    latam['pais'] = np.select(condiciones, valores, default="")
    
    # --- PROCESO DEL GRÁFICO ---
    # 1. Filtrar los valores válidos de la pregunta P11STGBS.A (1, 2, 3, 4)
    tabla_demo = latam[latam['P11STGBS.A'].isin([1, 2, 3, 4])].copy()
    
    # 2. Agrupar por país y nivel de satisfacción, y contar el total
    tabla_demo = tabla_demo.groupby(['pais', 'P11STGBS.A']).size().reset_index(name='total')
    
    # 3. Calcular el porcentaje respecto al total de cada país
    tabla_demo['porcentaje'] = tabla_demo['total'] / tabla_demo.groupby('pais')['total'].transform('sum') * 100
    
    # 4. Recodificar los niveles de satisfacción
    recode_dict = {
        1: "Muy satisfecho",
        2: "Más bien satisfecho",
        3: "No muy satisfecho",
        4: "Nada satisfecho"
    }
    tabla_demo['P11STGBS.A'] = tabla_demo['P11STGBS.A'].map(recode_dict)
    
    orden_x = ["Muy satisfecho", "Más bien satisfecho", "No muy satisfecho", "Nada satisfecho"]
    
    print("Generando el gráfico...")
    # 5. Configuración y creación del gráfico
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    
    colores = ["#f48fb1", "#c39bd3", "#8e44ad", "#f8c8dc"]
    
    ax = sns.barplot(
        data=tabla_demo,
        x="P11STGBS.A",
        y="porcentaje",
        hue="P11STGBS.A",
        order=orden_x,
        palette=colores,
        estimator=sum,       
        errorbar=None,
        legend=False         
    )
    
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    
    plt.title("Satisfacción con el funcionamiento de la democracia", fontweight="bold", fontsize=14)
    plt.xlabel("Nivel de satisfacción")
    plt.ylabel("Porcentaje")
    
    plt.tight_layout()
    plt.show()

# Ejecutar la visualización
if __name__ == "__main__":
    prep_and_plot()
