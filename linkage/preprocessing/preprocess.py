import pandas as pd


def preprocess () -> pd.DataFrame | pd.DataFrame:
    input_fdr = 'input/'

    sinasc = pd.read_parquet(input_fdr + 'DN2023.parquet.gzip')
    sim = pd.read_parquet(input_fdr + 'DO2023.parquet.gzip')

    sinasc.drop_duplicates(inplace=True)
    sim.drop_duplicates(inplace=True)

    sinasc['index'] = range(len(sinasc))
    sinasc.set_index('index', inplace=True)

    sim['index'] = range(len(sim))
    sim.set_index('index', inplace=True)

    return sinasc, sim
