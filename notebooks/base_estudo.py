import pandas as pd
import numpy as np
import time

# ===============
# Gerar base de 300.000 dados
# ==============

def gerar_base(n=300_000):
    np.random.seed(42)

    user_id = np.random.randint(1, 100_000, size=n)
    event_type = np.random.choice(
        ['purchase', 'click', 'view', 'signup'],
        size=n,
        p=[0.12, 0.44, 0.40, 0.04]
    )

    country = np.random.choice(
        ['BR', 'US', 'PT', 'ES'],
        size=n,
        p=[0.6, 0.2, 0.1, 0.1]
    )
    is_premium = np.random.choice([True, False], size=n, p=[0.18, 0.82])

    base_data = pd.Timestamp("2025-06-01")
    days = np.random.randint(0, 60, size=n)
    timestamp = base_data + pd.to_timedelta(days, unit='D')

    amount = np.random.exponential(scale=80, size=n).round(2)
    amount = np.where(event_type == 'purchase', amount, 0.0)

    df = pd.DataFrame({
        'user_id': user_id,
        'event_type': event_type,
        'country': country,
        'is_premium': is_premium,
        'timestamp': timestamp,
        'amount': amount
    })

    return df

# Criar base
df = gerar_base()
print(f"📦 Base gerada com {df.shape[0]} linhas e {df.shape[1]} colunas")
print(df.head())

df.to_csv("base_estudos.csv", index=False)

