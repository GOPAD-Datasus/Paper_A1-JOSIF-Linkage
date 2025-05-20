import pandas as pd
import os


def make_data_folder () -> None:
    """
    Creates the temporary file structure to hold raw and
    processed files. The structure is defined below:

    + data: root folder
      - input: DO and DN
      - output: processed data
    """
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    raw_folder = data_folder + '/input'
    if not os.path.exists(raw_folder):
        os.mkdir(raw_folder)

    processed_folder = data_folder + '/output'
    if not os.path.exists(processed_folder):
        os.mkdir(processed_folder)


def preprocess () -> pd.DataFrame | pd.DataFrame:
    make_data_folder()

    input_fdr = 'data/input/'

    sinasc = pd.read_parquet(input_fdr + 'DN2023.parquet.gzip')
    sim = pd.read_parquet(input_fdr + 'DO2023.parquet.gzip')

    sinasc.drop_duplicates(inplace=True)
    sim.drop_duplicates(inplace=True)

    sinasc['index'] = range(len(sinasc))
    sinasc.set_index('index', inplace=True)

    sim['index'] = range(len(sim))
    sim.set_index('index', inplace=True)

    return sinasc, sim
