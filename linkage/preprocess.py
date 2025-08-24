from pathlib import Path
import os

import pandas as pd


def make_data_folder() -> None:
    """
    Creates the temporary folder structure to hold raw and
    processed files. The structure is defined below:

    + data: root folder
      - input: DO and DN
      - output: processed data
    """
    data_folder = Path().cwd() / 'data'

    raw_folder = data_folder / 'input'
    os.makedirs(raw_folder, exist_ok=True)

    processed_folder = data_folder / 'output'
    os.makedirs(processed_folder, exist_ok=True)


def preprocess() -> tuple[pd.DataFrame, pd.DataFrame]:
    make_data_folder()

    input_fdr = 'data/input/'

    try:
        sinasc = pd.read_parquet(input_fdr +
                                 'DN.parquet.gzip')
    except FileNotFoundError:
        error = ('Error| Missing "DN.parquet.gzip"'
                 ' inside input folder')
        raise RuntimeError(error)

    try:
        sim = pd.read_parquet(input_fdr +
                              'DO.parquet.gzip')
    except FileNotFoundError:
        error = ('Error| Missing "DO.parquet.gzip"'
                 ' inside input folder')
        raise RuntimeError(error)

    sinasc.drop_duplicates(inplace=True)
    sim.drop_duplicates(inplace=True)

    sinasc['index'] = range(len(sinasc))
    sinasc.set_index('index', inplace=True)

    sim['index'] = range(len(sim))
    sim.set_index('index', inplace=True)

    return sinasc, sim
