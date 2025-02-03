import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida os json
def extrair_dados(pasta: str) -> pd.DataFrame:
  arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
  df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
  df_total = pd.concat(df_list, ignore_index=True)
  return df_total

# uma funcao que transforma
def calcular_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
  df["Total"] = df["Quantidade"] * df["Venda"]
  return df

# uma funcao que da load em csv ou parquet
def carregar_dados(formato_saida: list, df: pd.DataFrame):
  for formato in formato_saida:
    if formato == 'csv':
      df.to_csv("dados.csv")
    if formato == 'parquet':
      df.to_parquet("dados.parquet")

# uma funcao para rodar a pipeline de dados
def pipeline_calcular_vendas_consolidadas(pasta_arquivo: str, formato_saida: list):
  data_frame = extrair_dados(pasta_arquivo)
  data_frame_calculado = calcular_total_vendas(data_frame)
  carregar_dados(formato_saida, data_frame_calculado)