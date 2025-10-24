---
title: 003 Plotly Marimo
marimo-version: 0.17.0
width: medium
---

```python {.marimo}
import marimo as mo
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
```

```python {.marimo}
f = "data/ClimaLab_2023-10-27_2025-04-30.parquet"
tmx = pd.read_parquet(f).reset_index()
```

```python {.marimo}
columnas = [columna for columna in tmx.columns if columna!="date"]


# Tu lista de opciones (puede venir de cualquier lado)

selector = mo.ui.dropdown(
    options=columnas,       # la lista
    value="tdb",      # valor inicial (opcional)
    label="Elige una variable",
    searchable=True         # añade caja de búsqueda para listas largas
)

selector  # muéstralo en la celda
```

```python {.marimo}
fig = px.scatter(tmx,tmx.date,selector.value )  
fig.show()
```

```python {.marimo}

```