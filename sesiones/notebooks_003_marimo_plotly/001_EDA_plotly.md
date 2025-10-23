---
title: 001 Eda Plotly
marimo-version: 0.17.0
width: medium
---

```python {.marimo}
import marimo as mo
import pandas as pd
import plotly.express as px
```

```python {.marimo}
f = 'data/ClimaLab_2023-10-27_2025-04-30.parquet'
tmx = pd.read_parquet(f)
tmx_date = tmx.reset_index().copy()
tmx
```

```python {.marimo}
px.line(
    data_frame=tmx_date,
    x='date',
    y='dhi'
)
```

```python {.marimo}
tmx2024 = tmx[tmx.index.year == 2024].copy()
tmx2024_horario = tmx2024.tdb.resample("h").max().copy()
tdb_heatmap = tmx2024_horario.groupby(
            by=[
                tmx2024_horario.index.month,
                tmx2024_horario.index.hour]
            ).mean().unstack().T
tdb_heatmap
```

```python {.marimo}
fig = px.imshow(tdb_heatmap, color_continuous_scale='RdBu_r', origin='lower')
fig.show()
```

```python {.marimo}
figs = px.line(data_frame=tmx_date, x='date', y='tdb', title='Time Series with Rangeslider')

figs.update_xaxes(rangeslider_visible=True)
figs.show()
```

```python {.marimo}
tmx_date
```

```python {.marimo}

```