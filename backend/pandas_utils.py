import pandas
from typing import List, Dict
from backend.custom_typing import STUDENTS_STATS_NON_AGGREGATED_TYPE as students_stats_non_aggregated_type


def read_xlsx(
        file_path: str
) -> pandas.DataFrame:
    return pandas.read_excel(file_path)


def map_dfs_columns(
        dfs: List[pandas.DataFrame],
        key_column: str = "ФИО"
) -> List[pandas.DataFrame]:
    mapped_dfs = []
    for i, df in enumerate(dfs):
        updated_df = df.copy()
        updated_df.columns = [
            f"{i + 1}.{col}" if col != key_column else col
            for col in df.columns
        ]
        mapped_dfs.append(updated_df)

    return mapped_dfs


def join_dfs(
        dfs: List[pandas.DataFrame],
        join_column: str = "ФИО"
) -> pandas.DataFrame:
    result_df = dfs[0]
    for df in dfs[1:]:
        result_df = pandas.merge(result_df, df, on=join_column, how='inner')

    return result_df


def get_students_stats_non_aggregated(
        df: pandas.DataFrame,
        set_index: str = "ФИО"
) -> students_stats_non_aggregated_type:
    dfs_divided_by_full_name = [row.to_frame().T.reset_index(drop=True) for _, row in df.iterrows()]
    return [df.set_index(set_index).to_dict(orient='index') for df in dfs_divided_by_full_name]


