# Importar la libreria pandas, que es fundamental para el analisis de datos.
import pandas as pd

# Define la ruta del archivo CSV que contiene los datos.
# Si el archivo esta en el mismo directorio que el script basta con poner el nombre del archivo.
# path = 'C:/Users/andre/OneDrive/Escritorio/Bootcamp_IA_MINTIC/Sesión 10/One_Retail.csv'
path = 'Online_Retail.csv'

# Lee el archivo CSV usando la funcion read_csv de pandas.
# Se especifica la codificacion 'latin1' para manejar caracteres especiales.
retail_data = pd.read_csv(path, encoding='latin1')

# Muestra el tipo de variable retail_data para confirmar que es un DataFrame de pandas.
# Un dataframe es una estructura de datos bidimensional similar a a una tabla.
print(type(retail_data))

print(retail_data)
