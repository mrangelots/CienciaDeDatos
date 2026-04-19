""" Feature Engineering """

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame ({
    'precio_total': [1000, 1500, 800, 2500],
    'num_prendas': [5, 10, 4, 15],
    'fecha_recibido': pd.to_datetime(['2026-04-01', '2026-04-02', '2026-04-03', '2026-04-04']),
    'fecha_entrega': pd.to_datetime(['2026-04-03', '2026-04-05', '2026-04-03', '2026-04-07'])
})

# Precio por prenda (Ratio)
df['costoXprenda'] = df['precio_total'] / df['num_prendas']

# Días de servicio (Diferencia)
df['dias_espera'] = (df['fecha_entrega'] - df['fecha_recibido']).dt.days

# Más de 8 prendas ¿Es un pedido grande? (Indicador)
df['pedido_grande'] = np.where(df['num_prendas'] > 8,1,0)

# Polynomial Features 
x = df[['precio_total', 'num_prendas']]

poly = PolynomialFeatures(degree=2, include_bias=False)
xPoly = poly.fit_transform(x)

df_Poly = pd.DataFrame(xPoly, columns=poly.get_feature_names_out(['precio_total', 'num_prendas']))

# Extraer componente de tiempo
df['mes_entrega'] = df['fecha_entrega'].dt.month
df['dia_semana_entrega'] = df['fecha_entrega'].dt.day_name()
df['es_fin_de_semana'] = np.where(df['fecha_entrega'].dt.weekday >= 5, 1, 0)

# Mostramos los resultados

print(f"Ratio:\n{df['costoXprenda']}")
print(f"Diferencia:\n{df['dias_espera']}")
print(f"Indicador:\n{df[['num_prendas', 'pedido_grande']]}")
print(f"Polynomial:\n{df_Poly.head()}")
print(f"DataTime:\n{df[['fecha_entrega', 'mes_entrega', 'dia_semana_entrega', 'es_fin_de_semana']]}")
