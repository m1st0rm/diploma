import pandas as pd
import pytest

from backend.pandas_utils import get_students_stats_raw, join_dfs, map_dfs_columns, read_xlsx


@pytest.fixture
def sample_dataframe_1():
    return pd.DataFrame(
        {"ФИО": ["Иванов Иван", "Петров Петр"], "Математика": [5, 4], "Физика": [3, 4]}
    )


@pytest.fixture
def sample_dataframe_2():
    return pd.DataFrame(
        {"ФИО": ["Иванов Иван", "Петров Петр"], "Химия": [5, 5], "Информатика": [4, 3]}
    )


def test_read_xlsx(monkeypatch):
    test_path = "fake_path.xlsx"
    expected_df = pd.DataFrame({"column1": [1, 2], "column2": [3, 4]})

    def mock_read_excel(path):
        assert path == test_path
        return expected_df

    monkeypatch.setattr(pd, "read_excel", mock_read_excel)

    result_df = read_xlsx(test_path)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_map_dfs_columns(sample_dataframe_1, sample_dataframe_2):
    input_dfs = [sample_dataframe_1, sample_dataframe_2]
    result = map_dfs_columns(input_dfs, key_column="ФИО")

    assert result[0].columns.tolist() == ["ФИО", "1.Математика", "1.Физика"]
    assert result[1].columns.tolist() == ["ФИО", "2.Химия", "2.Информатика"]


def test_join_dfs(sample_dataframe_1, sample_dataframe_2):
    input_dfs = [sample_dataframe_1, sample_dataframe_2]
    result = join_dfs(input_dfs, join_column="ФИО")

    expected_columns = ["ФИО", "Математика", "Физика", "Химия", "Информатика"]
    assert result.columns.tolist() == expected_columns

    assert len(result) == 2
    assert result.loc[0, "ФИО"] == "Иванов Иван"
    assert result.loc[1, "ФИО"] == "Петров Петр"


def test_get_students_stats_raw(sample_dataframe_1):
    result = get_students_stats_raw(sample_dataframe_1, set_index="ФИО")

    expected_output = [
        {'Иванов Иван': {'Математика': 5, 'Физика': 3}},
        {'Петров Петр': {'Математика': 4, 'Физика': 4}},
    ]

    assert isinstance(result, list)
    assert result == expected_output
