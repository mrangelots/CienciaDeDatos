""" Comparar Escaladores """
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])

# Diccionarios de escaladores
escaladores = {
    "MinMax": MinMaxScaler(),
    "Standard": StandardScaler(),
    "Robust": RobustScaler(),
    "MaxAbs": MaxAbsScaler()
}

for tipo,esc in escaladores.items():
    print(f"\n--- {tipo} Scaler ---")
    print(esc.fit_transform(data))

""" Usamos MinMax cuando queremos que todos nuestros datos
    esten entre 0 y 1
    
    Usamos Standard para saber cuales valores son normales 
    y cuales de plano no lo son
    
    Usamos Robust si tenemos datos muy locos
    
    Usamos MaxABs si queremos mantener hasta los valores 0
    sin deformar tanto la estructura """