"""
Module for processing data from Excel files and performing operations on pandas DataFrames.

This module provides the following functions:
1. read_xlsx: Reads an Excel file and converts its content into a pandas DataFrame.
2. map_dfs_columns: Updates column names in a list of DataFrames by adding prefixes.
3. join_dfs: Merges multiple DataFrames based on a common column.
4. get_students_stats_raw: Converts DataFrame rows into a list of dictionaries indexed by a specified column.

Functions:
- read_xlsx: Reads an Excel file and returns a DataFrame.
- map_dfs_columns: Adds prefixes to column names in DataFrames.
- join_dfs: Performs inner joins on a list of DataFrames.
- get_students_stats_raw: Splits rows into dictionaries with the specified index.

Dependencies:
- pandas: For data manipulation and analysis.
- backend.custom_typing: Custom typing definition for STUDENTS_STATS_RAW_TYPE.
"""

import pandas
from pandas import DataFrame
from backend.custom_typing import STUDENTS_STATS_RAW_TYPE


def read_xlsx(
        file_path: str
) -> DataFrame:
    """
    Reads an Excel file and returns its content as a DataFrame.

    :param file_path: The path to the Excel file.
    :type file_path: str
    :return: A DataFrame containing the data from the Excel file.
    :rtype: DataFrame
    """
    return pandas.read_excel(file_path)


def map_dfs_columns(
        dfs: list[DataFrame],
        key_column: str = "ФИО"
) -> list[DataFrame]:
    """
    Updates column names for a list of DataFrames, prefixing column names with an index.

    :param dfs: A list of DataFrames to be updated.
    :type dfs: list[DataFrame]
    :param key_column: The column name to exclude from renaming (default is "ФИО").
    :type key_column: str
    :return: A list of DataFrames with updated column names.
    :rtype: list[DataFrame]
    """
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
        dfs: list[DataFrame],
        join_column: str = "ФИО"
) -> DataFrame:
    """
    Performs an inner join on a list of DataFrames based on a common column.

    :param dfs: A list of DataFrames to be joined.
    :type dfs: list[DataFrame]
    :param join_column: The name of the column to join on (default is "ФИО").
    :type join_column: str
    :return: A single DataFrame resulting from the inner join of the input DataFrames.
    :rtype: DataFrame
    """
    result_df = dfs[0]
    for df in dfs[1:]:
        result_df = pandas.merge(result_df, df, on=join_column, how='inner')

    return result_df


def get_students_stats_raw(
        df: DataFrame,
        set_index: str = "ФИО"
) -> STUDENTS_STATS_RAW_TYPE:
    """
    Splits a DataFrame row-by-row into individual DataFrames and converts each row into a dictionary.

    :param df: The input DataFrame containing student statistics.
    :type df: DataFrame
    :param set_index: The column to use as the index for the resulting dictionaries (default is "ФИО").
    :type set_index: str
    :return: A list of dictionaries representing each row in the DataFrame.
    :rtype: STUDENTS_STATS_RAW_TYPE
    """
    dfs_divided_by_full_name = [row.to_frame().T.reset_index(drop=True) for _, row in df.iterrows()]
    return [df.set_index(set_index).to_dict(orient='index') for df in dfs_divided_by_full_name]
