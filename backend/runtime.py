import datetime
from typing import Any

from backend import data_utils, docx_utils, pandas_utils
from backend.classes.common_config import CommonConfig


def _make_date_string_representation(date: datetime.date) -> tuple[str, str, str]:
    month_names_dict = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }

    day = date.day
    month = date.month
    year = date.year

    if day < 10:
        day_repr = "0" + str(day)
    else:
        day_repr = str(day)

    month_repr = month_names_dict[month]

    year_repr = str(year)

    return day_repr, month_repr, year_repr


def runtime(
    state_holder: dict[str, Any],
) -> int:
    dfs = []
    for path in state_holder['semester_files_paths']:
        dfs.append(pandas_utils.read_xlsx(path))
    try:
        mapped_dfs = pandas_utils.map_dfs_columns(dfs)

        joined_df = pandas_utils.join_dfs(mapped_dfs)

        non_aggregated_data = pandas_utils.get_students_stats_raw(joined_df)

        data_with_configs = data_utils.get_students_stats_with_discipline_configs(
            non_aggregated_data
        )

        data_with_avg_marks = data_utils.get_students_with_avg_mark(data_with_configs)

        data_with_grouped_configs = (
            data_utils.get_students_stats_with_discipline_configs_grouped_by_category(
                data_with_configs
            )
        )

        data_summarized = (
            data_utils.get_students_stats_with_discipline_configs_grouped_by_category_summarized(
                data_with_grouped_configs
            )
        )
    except Exception:
        return 1

    try:
        data_ready = data_utils.get_students_configs(
            data_summarized, pandas_utils.read_xlsx(state_holder['diploma_file_path'])
        )
    except Exception:
        return 2

    start_date_repr = _make_date_string_representation(state_holder['start_date'])
    end_date_repr = _make_date_string_representation(state_holder['end_date'])
    statement_date_repr = _make_date_string_representation(state_holder['statement_date'])

    common_config = CommonConfig(
        start_date_day=start_date_repr[0],
        start_date_month=start_date_repr[1],
        start_date_year=start_date_repr[2][2:],
        end_date_day=end_date_repr[0],
        end_date_month=end_date_repr[1],
        end_date_year=end_date_repr[2][2:],
        speciality_code=state_holder['speciality_code'],
        speciality_name=state_holder['speciality_name'],
        speciality_area_code=state_holder['speciality_area_code'],
        speciality_area_name=state_holder['speciality_area_name'],
        statement_date_day=statement_date_repr[0],
        statement_date_month=statement_date_repr[1],
        statement_date_year=statement_date_repr[2],
    )

    try:
        docx_utils.build_statements(
            state_holder['template_file_path'],
            state_holder['save_directory_path'],
            data_ready,
            common_config,
        )
        pandas_utils.make_students_with_avg_mark_xlsx_file(
            data_with_avg_marks, state_holder['save_directory_path']
        )
    except Exception:
        return 3

    return 4
