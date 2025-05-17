import pytest
from pandas import DataFrame

from backend.classes.discipline_config import DisciplineConfig
from backend.classes.student_config import StudentConfig
from backend.data_utils import (
    get_disciplines_for_student_config,
    get_students_configs,
    get_students_stats_with_discipline_configs,
    get_students_stats_with_discipline_configs_grouped_by_category,
    get_students_stats_with_discipline_configs_grouped_by_category_summarized,
    get_students_with_avg_mark
)

PRACTICE_CATEGORY = 'practice'
COURSE_PROJECT_CATEGORY = 'course_project'
COURSE_WORK_CATEGORY = 'course_work'
REGULAR_CATEGORY = 'regular'


@pytest.fixture
def sample_students_stats_raw():
    return [
        {
            "Иванов Иван": {
                "1.1.Математика/120:5:ЭК": 5,
                "1.2.Физика/80:4:ЭК": 4,
                "2.1.Химия/60:3:ЭК": 4,
            },
            "Петров Петр": {
                "1.1.Математика/120:5:ЭК": 5,
                "2.1.Химия/60:4:ЭК": 4,
                "2.2.Информатика/90:5:ЭК": 5,
            },
        }
    ]


@pytest.fixture
def sample_diploma_themes_df():
    return DataFrame(
        {"ФИО": ["Иванов Иван", "Петров Петр"], "Тема дипломного проекта": ["Тема 1", "Тема 2"]}
    )


def test_get_students_stats_with_discipline_configs(sample_students_stats_raw):
    result = get_students_stats_with_discipline_configs(sample_students_stats_raw)

    assert len(result) == 2
    assert isinstance(result["Иванов Иван"], list)
    assert isinstance(result["Иванов Иван"][0], DisciplineConfig)


def test_get_students_stats_with_discipline_configs_grouped_by_category(sample_students_stats_raw):
    students_stats = get_students_stats_with_discipline_configs(sample_students_stats_raw)
    result = get_students_stats_with_discipline_configs_grouped_by_category(students_stats)

    assert "Иванов Иван" in result
    assert REGULAR_CATEGORY in result["Иванов Иван"]


def test_get_students_stats_with_discipline_configs_grouped_by_category_summarized(
    sample_students_stats_raw,
):
    students_stats = get_students_stats_with_discipline_configs(sample_students_stats_raw)
    grouped_by_category = get_students_stats_with_discipline_configs_grouped_by_category(
        students_stats
    )
    result = get_students_stats_with_discipline_configs_grouped_by_category_summarized(
        grouped_by_category
    )

    assert len(result) > 0
    for student_name, categories in result.items():
        assert REGULAR_CATEGORY in categories
        assert len(categories[REGULAR_CATEGORY]) > 0


def test_get_disciplines_for_student_config(sample_students_stats_raw):
    students_stats = get_students_stats_with_discipline_configs(sample_students_stats_raw)
    student_discipline_configs = students_stats["Иванов Иван"]
    result = get_disciplines_for_student_config(student_discipline_configs)

    assert len(result) > 0
    assert isinstance(result[0], tuple)
    assert len(result[0]) == 3


def test_get_students_configs(sample_students_stats_raw, sample_diploma_themes_df):
    students_stats = get_students_stats_with_discipline_configs(sample_students_stats_raw)
    grouped_by_category = get_students_stats_with_discipline_configs_grouped_by_category(
        students_stats
    )
    summarized_by_category = (
        get_students_stats_with_discipline_configs_grouped_by_category_summarized(
            grouped_by_category
        )
    )

    result = get_students_configs(summarized_by_category, sample_diploma_themes_df)

    assert len(result) == 2
    assert isinstance(result[0], StudentConfig)
    assert result[0].full_name == "Иванов Иван"


def test_get_students_with_avg_mark():
    students_stats = {
        "Иванов Иван": [
            DisciplineConfig(contol_form="exam", name="Математика", semester=1,
                             mark=5, study_hours=60, credits_number=3, categoty="regular"),
            DisciplineConfig(contol_form="test", name="Физика", semester=1,
                             mark=4, study_hours=45, credits_number=3, categoty="regular"),
        ],
        "Петров Петр": [
            DisciplineConfig(contol_form="exam", name="Математика", semester=1,
                             mark=3, study_hours=60, credits_number=3, categoty="regular"),
            DisciplineConfig(contol_form="test", name="Физика", semester=1,
                             mark=2, study_hours=45, credits_number=3, categoty="regular"),
        ],
    }

    result = get_students_with_avg_mark(students_stats)

    expected = (
        ("Иванов Иван", pytest.approx(4.5)),
        ("Петров Петр", pytest.approx(2.5)),
    )

    assert isinstance(result, tuple)
    assert result == expected


if __name__ == "__main__":
    pytest.main()
