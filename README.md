
<h1> API CoinGecko </h1>

![image](https://github.com/user-attachments/assets/923bd627-75fb-4e3a-a85d-68a0536bf323)

<h2> Bibliotecas utilizadas</h2>

```python
import pandas as pd
import streamlit as st
import plotly.express as px
import requests
```

<strong> API </strong>

```python
url = "https://api.coingecko.com/api/v3/coins/markets"
parametros = {
    "vs_currency": "brl",
    "order": "market_cap_desc",
    "per_page": 1000,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(url, params=parametros)
data = response.json()
```

<strong> Dataframe </strong>

```python
df = pd.DataFrame(data)
print(df.head())
```
