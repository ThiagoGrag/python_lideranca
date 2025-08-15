import pandas as pd
import numpy as np
import time

# ===============
# Gerar base de 300.000 dados
# ==============

def gerar_base(n=300_000): 
# Função com um parâmetro chamado n com um valor padrão de 300.000. A função irá gerar 300.000 dados.
    np.random.seed(42)

    user_id = np.random.randint(1, 100_000, size=n)
    # Cria uma série de n números inteiros aleatórios para serem os IDs dos usuários. Os números variam de 1 e 99.999.
    event_type = np.random.choice(
        ['purchase', 'click', 'view', 'signup'],
        size=n,
        p=[0.12, 0.44, 0.40, 0.04]
    )
    # Cria uma série de n tipos de eventos.
    # np.random.choice escolhe aleatoriamente um valor da lista
    # O parâmetro p define a probabilidade de cada escolha

    country = np.random.choice(
        ['BR', 'US', 'PT', 'ES'],
        size=n,
        p=[0.6, 0.2, 0.1, 0.1]
    )
    # Cria a série escolhendo aleatóriamente seguindo as probabilidades

    is_premium = np.random.choice([True, False], size=n, p=[0.18, 0.82])
    # Cria a série escolhendo aleatóriamente seguindo as probabilidades

    base_data = pd.Timestamp("2025-06-01")
    # Cria um objeto de data e hora de ponto de partida.
    days = np.random.randint(0, 60, size=n)
    # Gera n números inteiros aleatórios entre 0 e 59
    timestamp = base_data + pd.to_timedelta(days, unit='D')
    # Soma a base_data com os números aleatórios

    amount = np.random.exponential(scale=80, size=n).round(2)
    # Gera n valores de uma distribuição exponencial, que é util para simular valores de compra (muitos valores baixos e poucos valores muito altos)
    # arredonda para duas casas decimais
    amount = np.where(event_type == 'purchase', amount, 0.0)
    # Onde o event_type == 'purchase', mantenha o valor original amount e se não, zero.

    df = pd.DataFrame({
        'user_id': user_id,
        'event_type': event_type,
        'country': country,
        'is_premium': is_premium,
        'timestamp': timestamp,
        'amount': amount
    })
    # Cria o dataframe final recebendo cada chave e se torna uma coluna.

    return df
    # Retorna o dataframe

# Criar base
df = gerar_base()
print(f"📦 Base gerada com {df.shape[0]} linhas e {df.shape[1]} colunas")
print(df.head())

df.to_csv("base_estudos.csv", index=False)

