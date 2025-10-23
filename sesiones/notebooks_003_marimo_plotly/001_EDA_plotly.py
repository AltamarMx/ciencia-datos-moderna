import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    return pd, px


@app.cell
def _(pd):
    f = 'data/ClimaLab_2023-10-27_2025-04-30.parquet'
    tmx = pd.read_parquet(f)
    tmx_date = tmx.reset_index().copy()
    tmx
    return tmx, tmx_date


@app.cell
def _(px, tmx_date):
    px.line(
        data_frame=tmx_date,
        x='date',
        y='dhi'
    )
    return


@app.cell
def _(tmx):
    tmx2024 = tmx[tmx.index.year == 2024].copy()
    tmx2024_horario = tmx2024.tdb.resample("h").max().copy()
    tdb_heatmap = tmx2024_horario.groupby(
                by=[
                    tmx2024_horario.index.month,
                    tmx2024_horario.index.hour]
                ).mean().unstack().T
    tdb_heatmap
    return (tdb_heatmap,)


@app.cell
def _(px, tdb_heatmap):
    fig = px.imshow(tdb_heatmap, color_continuous_scale='RdBu_r', origin='lower')
    fig.show()

    return


@app.cell
def _(px, tmx_date):
    figs = px.line(data_frame=tmx_date, x='date', y='tdb', title='Time Series with Rangeslider')

    figs.update_xaxes(rangeslider_visible=True)
    figs.show()

    return


@app.cell
def _(tmx_date):
    tmx_date
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
