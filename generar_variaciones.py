import pandas as pd

# Cargar el archivo Excel proporcionado
file_path = 'C:/Users/joses/Documents/ejemplo chatgpt.xlsx'  # Reemplaza con la ruta real de tu archivo
df = pd.read_excel(file_path)

# Lista de tallas para generar las variaciones
sizes = [5, 6, 7, 8, 9, 10, 11, 12]

# Inicializar una lista vacía para almacenar las nuevas filas
all_new_rows = []

# Iterar sobre todas las filas en el DataFrame original
for index, reference_row in df.iterrows():
    # Generar nuevas filas para cada talla basadas en la fila actual
    for i, size in enumerate(sizes, start=1):
        new_row = reference_row.copy()
        new_row['ID'] = None  # Se asume que el ID no es necesario, si lo es, puede ser auto-incrementado
        new_row['Tipo'] = 'variation'
        new_row['Nombre'] = f"{reference_row['Nombre']} - {size}"
        new_row['SKU'] = None  # Se asume que el SKU no es necesario para las variaciones
        new_row['Posición'] = i
        new_row['Valor(es) del atributo 1'] = str(size)
        new_row['Atributo visible 1'] = None  # Se establece como None como en el ejemplo
        all_new_rows.append(new_row)

# Crear un nuevo DataFrame a partir de las filas generadas
new_rows_df = pd.DataFrame(all_new_rows)

# Guardar el resultado en un nuevo archivo Excel
output_file = 'C:/Users/joses/Desktop/python/variaciones_generadas_todas.xlsx'  # Reemplaza con la ruta donde quieres guardar el archivo
new_rows_df.to_excel(output_file, index=False)
