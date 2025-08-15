import pandas as pd
import numpy as np
import time

# Lendo a base
df = pd.read_csv("C:/Users/thiag/estudo_python_lideranca/data/base_estudos.csv")
df['timestamp'] = df['timestamp'].astype('datetime64[ns]')

cutoff = df['timestamp'].max() - pd.Timedelta(days=30)
# cutoff traz o máximo de data do dataset - 30 dias
# print(df.head())

# Função para medir a memória
def medir_memoria(df, label):
    mem_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"Memória utilizada ({label}): {mem_mb:.2f} MB")
    return mem_mb

# Versão não otimizada
def versao_nao_otimizada(df):
    print("\n Versão não otimizada...")

    medir_memoria(df, "Inicial não otimizada")

    def is_relevant_row(row):
        return (row['is_premium'] and (row['timestamp'] >= cutoff))
        # retorna as linhas que is_premium e estão dentro de 30 dias
    
    start = time.perf_counter()
    mask = df.apply(is_relevant_row, axis=1) # processo linha a linha. É lento
    filtrado = df[mask]

    def aggregate_group(g):
        return pd.Series({
            'total_amount': g['amount'].sum(),
            'unique_users': g['user_id'].nunique(),
            'avg_amount': g['amount'].mean()
        })
    
    result = filtrado.groupby('country').apply(aggregate_group)
    tempo_execucao = time.perf_counter() - start

    print(f"Tempo de execução não otimizado: {tempo_execucao:.3f} segundos")
    print(result)

    return result, tempo_execucao

# Execução
result_nao_opt, tempo_nao_opt = versao_nao_otimizada(df.copy())


# Comparativo
print("\n Comparativo Final")
print(f"Tempo não otimizado: {tempo_nao_opt:.3f} s")