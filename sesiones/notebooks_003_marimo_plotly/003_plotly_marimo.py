import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import plotly.express as px
    return mo, pd, px


@app.cell
def _(pd):
    f = "data/ClimaLab_2023-10-27_2025-04-30.parquet"
    tmx = pd.read_parquet(f).reset_index()
    return (tmx,)


@app.cell
def _(mo, tmx):
    columnas = [columna for columna in tmx.columns if columna!="date"]


    # Tu lista de opciones (puede venir de cualquier lado)

    selector = mo.ui.dropdown(
        options=columnas,       # la lista
        value="tdb",      # valor inicial (opcional)
        label="Elige una variable",
        searchable=True         # añade caja de búsqueda para listas largas
    )

    selector  # muéstralo en la celda

    return (selector,)


@app.cell
def _(px, selector, tmx):
    fig = px.scatter(tmx,tmx.date,selector.value )  
    fig.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
