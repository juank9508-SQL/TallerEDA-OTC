

import pandas as pd
import numpy as np 

df = pd.read_csv("pharmacy_otc_sales_data.csv")

print(df.head(2)) 

#print(df.shape) #muestra columnas y filas 

print(f"datos faltantes o nulos", df.isnull().sum())   #muestra datos faltanes, en este caso no hay

print(f"datos duplicados" ,df.duplicated().sum())
df_ordenado= df.sort_values(by="Country")
#print(df[df["Country"] == "USA"])

print(df_ordenado)

#Pregunta 1, Sacar promedio de ventas por pais
Promedio_ventas= df.groupby("Country")["Amount ($)"].mean().round(2)
print(f'este es el promedio de ventas por ' , Promedio_ventas)
#Pregunta 2, Producto mas vendido
producto_mas_vendido= df.groupby("Product")["Boxes Shipped"].sum().sort_values(ascending=False).head(1)
print(f'Este es el producto mas vendido {producto_mas_vendido.index[0]}, con {producto_mas_vendido.values[0]} Unidades' )

#Pregunta 3, Producto menos vendido
producto_menos_vendido= df.groupby("Product")["Boxes Shipped"].sum().sort_values(ascending=True).head(1)
print(f'este es el producto menos vendido: {producto_menos_vendido.index[0]} con {producto_menos_vendido.values[0]} unidades')
#Pregunta 4, Top seller
top_seller= df.groupby("Sales Person")["Amount ($)"].sum().head(1)
print (f'Este es el top seller', top_seller)
#pregunta 5, mes con mayores ventas
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Month Name"] = df["Date"].dt.strftime("%B")
Mes_mayor_ventas =df.groupby("Month Name")["Amount ($)"].sum().sort_values(ascending=False).head(1)
print(f'Este es el mes con mayor ventas', Mes_mayor_ventas)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




# Crear columna de meses
df["Mes"] = df["Date"].dt.strftime("%B")

# Agrupar ventas por mes
df_line = df.groupby("Mes")["Amount ($)"].sum().reset_index()

# Orden correcto de meses
orden_meses = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Ordenar meses
df_line["Mes"] = pd.Categorical(
    df_line["Mes"],
    categories=orden_meses,
    ordered=True
)

df_line = df_line.sort_values("Mes")

# Crear gráfico
plt.figure(figsize=(10,4))

sns.lineplot(
    data=df_line,
    x="Mes",
    y="Amount ($)",
    marker="o"
)

# Etiquetas de ventas
for i, txt in enumerate(df_line["Amount ($)"]):
    plt.text(
        df_line["Mes"].iloc[i],
        df_line["Amount ($)"].iloc[i],
        round(txt,2),
        ha='left',
        va='bottom'
    )

# Títulos
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")

plt.grid()

plt.show()





