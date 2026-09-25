# Exercício 2 — Tratamento de Dados de Sensor IoT

import pandas as pd
import numpy as np

leituras_iot = {
    'sensor_id': ['S1', 'S2', 'S1', 'S3', 'S2'],
    'timestamp': ['2026-03-17 10:00:00', '17/03/2026 10:00', '2026-03-17 10:00:00',
                  '2026-03-17 10:01:00', '2026-03-17 10:02:00'],
    'temperatura_c': ['24.5 C', '850.0 C', '24.5 C', None, '-10.2 C'],
    'pressao_bar': ['1.01', '1.05', '1.01', '0.98', '0.00']
}
df_raw = pd.DataFrame(leituras_iot)


def transform_iot_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()

    #Remove duplicados exatos pela chave composta (sensor_id, timestamp)
    df_clean = df_clean.drop_duplicates(subset=['sensor_id', 'timestamp'], keep='first')

    #Padroniza o timestamp para datetime (aceita formatos BR e ISO)
    df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce', dayfirst=True)
    df_clean = df_clean.dropna(subset=['timestamp'])  # descarta timestamps inválidos

    #Limpa a temperatura: remove o sufixo " C" e converte para float
    def clean_temp(val):
        if pd.isna(val):
            return np.nan
        return float(str(val).replace('C', '').strip())

    df_clean['temperatura_c'] = df_clean['temperatura_c'].apply(clean_temp)

    #Preenche nulos de temperatura com a mediana do próprio sensor
    df_clean['temperatura_c'] = df_clean.groupby('sensor_id')['temperatura_c'] \
        .transform(lambda x: x.fillna(x.median()))
    #Se o sensor não tiver nenhuma leitura válida a mediana também fica nula,descarta
    df_clean = df_clean.dropna(subset=['temperatura_c'])

    #Converte a pressão para float
    df_clean['pressao_bar'] = df_clean['pressao_bar'].astype(float)

    #Filtra outliers irreais: temperatura entre -20°C e 100°C, pressão > 0.5 bar
    df_clean = df_clean[
        (df_clean['temperatura_c'].between(-20, 100)) &
        (df_clean['pressao_bar'] > 0.5)
    ]

    return df_clean.reset_index(drop=True)


if __name__ == '__main__':
    df_final = transform_iot_data(df_raw)
    print(df_final.to_string(index=False))