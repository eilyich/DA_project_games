import pandas as pd

def info(data):
    l_dtypes = lambda x: type(x).__name__
    dtype = data.dtypes.tolist()
    nans = data.isna().sum().tolist()

    str_count = []
    int_count = []
    float_count = []

    for col in data.columns:
        column_dtp = data.query(f'{col}.notna()')[col].apply(l_dtypes)
        str_count.append((column_dtp == 'str').sum())
        int_count.append((column_dtp == 'int').sum())
        float_count.append((column_dtp == 'float').sum())

    output = pd.concat(
        [pd.DataFrame(
            columns=['index'],
            data=['missed', 'dtypes', 'str_values', 'int_values',
                  'float_values']),
            pd.DataFrame(
                columns=data.columns.tolist(),
                data=[nans, dtype, str_count, int_count, float_count])], axis=1
    ).set_index('index')

    return output