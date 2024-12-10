import pandas
from typing import List


def read_xlsx(file_path: str) -> pandas.DataFrame:
    return pandas.read_excel(file_path)


def map_dfs_columns(dfs: List[pandas.DataFrame], key_column: str = "ФИО") -> List[pandas.DataFrame]:
    mapped_dfs = []
    for i, df in enumerate(dfs):
        updated_df = df.copy()
        updated_df.columns = [
            f"{i + 1}.{col}" if col != key_column else col
            for col in df.columns
        ]
        mapped_dfs.append(updated_df)

    return mapped_dfs


def join_dfs(dfs: List[pandas.DataFrame], join_column: str = "ФИО") -> pandas.DataFrame:
    result_df = dfs[0]
    for df in dfs[1:]:
        result_df = pandas.merge(result_df, df, on=join_column, how='inner')

    return result_df
