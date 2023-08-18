import pandas as pd
import os

ruta_archivos = r'C:\Users\David Tabares\Documents\Conversion\Reto1\Archivo xls'

dataframes = []

for filename in os.listdir(ruta_archivos):
    if filename.endswith(".xls"):
        excel_ruta_archivo = os.path.join(ruta_archivos, filename)
        df = pd.read_excel(excel_ruta_archivo)
        dataframes.append(df)

combinar_df = pd.concat(dataframes, ignore_index=True)

combinar_csv_ruta = r'C:\Users\David Tabares\Documents\Conversion\Reto1\Archivo convertido\archivo_combinado.csv'

combinar_df.to_csv(combinar_csv_ruta, index=False)


print(f'Archivos .xls convertidos y combinados en : {combinar_csv_ruta}')