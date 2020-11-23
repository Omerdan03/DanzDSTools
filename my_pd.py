import pandas as pd


def init_df(columns=None):
    return pd.DataFrame(columns=columns)


print(init_df(['hey', 'Column']))
