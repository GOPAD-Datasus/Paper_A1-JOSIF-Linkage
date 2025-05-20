import pandas as pd
import recordlinkage as rl


def link (sinasc: pd.DataFrame, sim: pd.DataFrame):
    ind = rl.Index()
    ind.block(['DTNASC', 'CODMUNRES'])
    candidates = ind.index(sinasc, sim)

    compare = rl.Compare()
    compare.exact('PESO', 'PESO', label='A')
    compare.exact('PARTO', 'PARTO', label='B')
    compare.exact('GRAVIDEZ', 'GRAVIDEZ', label='C')
    compare.exact('SEMAGESTAC', 'SEMAGESTAC', label='D')
    compare.exact('ESCMAE', 'ESCMAE', label='E')
    results = compare.compute(candidates, sinasc, sim)

    df_mort = results[(results['A'] == 1) &
                      (results['B'] == 1) &
                      (results['C'] == 1) &
                      (results['D'] == 1) &
                      (results['E'] == 1)]
    df_mort.reset_index(inplace=True)
    df_mort = df_mort[['index_1', 'index_2']]

    df_mort = df_mort.merge(sinasc, left_on='index_1',
                            right_on='index', how='left')
    df_mort = df_mort.merge(sim, left_on='index_2',
                            right_on='index', how='left')

    df_mort.to_parquet('output/SIMORTN.parquet.gzip',
                  compression='gzip')

    print(f'SIM size: {len(sim)}\n'
          f'SINASC size: {len(sinasc)}\n'
          f'SIMORTN size: {len(df_mort)}\n'
          f'\tRatio SIMORTN / SIM: {len(df_mort)/len(sim)}')