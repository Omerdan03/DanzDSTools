import pandas as pd

def multiply_plots():

    num_features = len(null_features_modi)
    fig, ax = plt.subplots(nrows=num_features, ncols=2, figsize=[6, 5*num_features])
    for i, feature in enumerate(null_features_modi):
        sns.histplot(df_modi[feature], ax=ax[i][0])
        sns.histplot(df[~df[feature].isnull()][feature], ax=ax[i][1])
    plt.tight_layout()



def add_exist_column(X): # create exist yes\no column
    X.loc[:, 'Is Remodeld'] = X.apply(lambda x: 'yes' if (x['YearRemodAdd'] != x['YearBuilt']) else 'No', axis=1)


def remove_outliers(df, feature, p):
    limits = df[feature].quantile(p), df[feature].quantile(1-p)
    df[df[feature].between(*limits)][feature]


def get_top_n(df, feature, n):
    top_n = df[feature].value_counts().index[:n]
    df.loc[~df[feature].isin(top_n), feature] = "Other"


def if_in_list(df, feature, list1):
    df['feature'].isin(list1)





def init_df(columns=None):
    return pd.DataFrame(columns=columns)


print(init_df(['hey', 'Column']))