""" Codificación de Variables Categóricas """
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df = pd.DataFrame ({
    'color': ['rojo', 'azul', 'verde', 'rojo', 'verde'],
    'talla': ['S', 'M', 'L', 'S', 'M']
})
# Codificación por etiquetas 
le = LabelEncoder()
dfLabel = df.copy()
dfLabel['color_label'] = le.fit_transform(df['color'])

# One Hot-Encoding
dfDummies = pd.get_dummies(df,columns=['color'])

# One Hot-Encoding con sklearn
ohe = OneHotEncoder(sparse_output=False) 
col_encoded = ohe.fit_transform(df[['color']])

# Mostramos los resultados
print(f"Codificación por etiqueta:\n{dfLabel}")
print(f"Hot-Encoding:\n{dfDummies}")
print(f"Hot-Encoding con sklearn:\n{col_encoded}")
