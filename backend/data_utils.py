"""
Module for processing and transforming student statistics with discipline configurations.

This module provides functions to:
1. Parse and transform raw student statistics into structured discipline configurations.
2. Group and summarize discipline configurations by categories such as regular, course work, course project, and practice.
3. Map disciplines to formatted outputs suitable for student reports.
4. Generate final student configurations, including diploma themes and structured discipline data.
5. Calculate and sort students by their average marks.

Functions:
- get_students_stats_with_discipline_configs: Transforms raw statistics into discipline configurations.
- get_students_stats_with_discipline_configs_grouped_by_category: Groups disciplines by category.
- get_students_stats_with_discipline_configs_grouped_by_category_summarized: Summarizes disciplines by name.
- get_disciplines_for_student_config: Formats disciplines for output.
- get_students_configs: Generates a list of structured student configurations.
- get_students_with_avg_mark: Computes and sorts students by average mark.

Dependencies:
- pandas: For data manipulation.
- backend.custom_typing: Custom typing definitions.
- backend.classes.discipline_config: Discipline configuration class.
- backend.classes.student_config: Student configuration class.
"""

from collections import defaultdict
from copy import deepcopy

from pandas import DataFrame

from backend.classes.discipline_config import DisciplineConfig
from backend.classes.student_config import StudentConfig
from backend.custom_typing import (
    STUDENTS_STATS_RAW_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE,
    STUDENTS_WITH_AVG_MARK_TYPE,
)

PRACTICE_ABBREVIATION = 'ПР'
COURSE_PROJECT_ABBREVIATION = 'КП'
COURSE_WORK_ABBREVIATION = 'КР'

SUMMARIZED_CONTROL_FORM_ABBREVIATION = "СФ"

CREDITS_NUMBER_TEMPLATE = " ({} з.е.)"

CREDIT_MARK = 'зч'

PRACTICE_CATEGORY = 'practice'
COURSE_PROJECT_CATEGORY = 'course_project'
COURSE_WORK_CATEGORY = 'course_work'
REGULAR_CATEGORY = 'regular'

DIPLOMA_THEMES_DATAFRAME_FULL_NAME_COLUMN = 'ФИО'
DIPLOMA_THEMES_DATAFRAME_THEME_COLUMN = 'Тема дипломного проекта'

MARKS_MAPPING = {
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    'зч': 'зачтено',
}


def get_students_stats_with_discipline_configs(
    students_stats: STUDENTS_STATS_RAW_TYPE,
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE:
    """
    Transforms raw student statistics into structured discipline configurations.

    :param students_stats: A list of dictionaries containing raw student statistics.
    :type students_stats: STUDENTS_STATS_RAW_TYPE
    :return: A dictionary mapping student names to their discipline configurations.
    :rtype: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE
    """
    students_stats_with_discipline_configs = {}
    for student_stats in students_stats:
        for student_full_name, disciplines_dict in student_stats.items():
            discipline_configs = []
            for discipline_info, discipline_mark in disciplines_dict.items():
                discipline_control_form = discipline_info.split(':')[2]
                discipline_name = discipline_info.split('.')[1].split('/')[0]
                discipline_semester = int(discipline_info.split('.')[0])
                discipline_study_hours = int(discipline_info.split('/')[1].split(':')[0])
                discipline_credits_number = float(discipline_info.split(':')[1])

                if discipline_control_form == PRACTICE_ABBREVIATION:
                    discipline_category = PRACTICE_CATEGORY
                elif discipline_control_form == COURSE_PROJECT_ABBREVIATION:
                    discipline_category = COURSE_PROJECT_CATEGORY
                elif discipline_control_form == COURSE_WORK_ABBREVIATION:
                    discipline_category = COURSE_WORK_CATEGORY
                else:
                    discipline_category = REGULAR_CATEGORY

                discipline_config = DisciplineConfig(
                    discipline_control_form,
                    discipline_name,
                    discipline_semester,
                    discipline_mark,
                    discipline_study_hours,
                    discipline_credits_number,
                    discipline_category,
                )
                discipline_configs.append(discipline_config)
            students_stats_with_discipline_configs[student_full_name] = discipline_configs

    return students_stats_with_discipline_configs


def get_students_stats_with_discipline_configs_grouped_by_category(
    students_stats_with_discipline_configs: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE,
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE:
    """
    Groups student discipline configurations into predefined categories.

    :param students_stats_with_discipline_configs: A dictionary of student discipline configurations.
    :type students_stats_with_discipline_configs: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE
    :return: A dictionary mapping student names to their grouped discipline configurations.
    :rtype: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE
    """
    students_stats_with_discipline_configs_grouped_by_category = {}
    categories = (
        REGULAR_CATEGORY,
        COURSE_WORK_CATEGORY,
        COURSE_PROJECT_CATEGORY,
        PRACTICE_CATEGORY,
    )
    for (
        student_full_name,
        stats_discipline_configs,
    ) in students_stats_with_discipline_configs.items():
        discipline_configs_grouped_by_category = {
            REGULAR_CATEGORY: [],
            COURSE_WORK_CATEGORY: [],
            COURSE_PROJECT_CATEGORY: [],
            PRACTICE_CATEGORY: [],
        }

        for stats_discipline_config in stats_discipline_configs:
            if stats_discipline_config.categoty == PRACTICE_CATEGORY:
                discipline_configs_grouped_by_category[PRACTICE_CATEGORY].append(
                    stats_discipline_config
                )
            elif stats_discipline_config.categoty == COURSE_WORK_CATEGORY:
                discipline_configs_grouped_by_category[COURSE_WORK_CATEGORY].append(
                    stats_discipline_config
                )
            elif stats_discipline_config.categoty == COURSE_PROJECT_CATEGORY:
                discipline_configs_grouped_by_category[COURSE_PROJECT_CATEGORY].append(
                    stats_discipline_config
                )
            else:
                discipline_configs_grouped_by_category[REGULAR_CATEGORY].append(
                    stats_discipline_config
                )

        for category in categories:
            discipline_configs_grouped_by_category[category].sort(
                key=lambda discipline_config: discipline_config.semester
            )

        students_stats_with_discipline_configs_grouped_by_category[student_full_name] = (
            discipline_configs_grouped_by_category
        )

    return students_stats_with_discipline_configs_grouped_by_category


def get_students_stats_with_discipline_configs_grouped_by_category_summarized(
    students_stats_with_discipline_configs_grouped_by_category: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE,
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE:
    """
    Summarizes regular disciplines grouped by name, combining marks, hours, and credits.

    :param students_stats_with_discipline_configs_grouped_by_category: Grouped discipline configurations.
    :type students_stats_with_discipline_configs_grouped_by_category: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE
    :return: A dictionary with summarized discipline configurations.
    :rtype: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE
    """
    students_stats_with_discipline_configs_grouped_by_category_summarized = deepcopy(
        students_stats_with_discipline_configs_grouped_by_category
    )

    for (
        student_full_name,
        stats_discipline_configs,
    ) in students_stats_with_discipline_configs_grouped_by_category_summarized.items():
        regular_disciplines_configs = stats_discipline_configs[REGULAR_CATEGORY]

        discipline_configs_grouped_by_name = defaultdict(list)
        for discipline_config in regular_disciplines_configs:
            discipline_configs_grouped_by_name[discipline_config.name].append(discipline_config)

        discipline_configs_groups_by_name = list(discipline_configs_grouped_by_name.values())

        summarized_regular_stats_discipline_configs = []

        for discipline_configs_group_by_name in discipline_configs_groups_by_name:
            summarized_control_form = SUMMARIZED_CONTROL_FORM_ABBREVIATION
            summarized_name = discipline_configs_group_by_name[0].name
            summarized_semesters = []
            summarized_mark = []
            summarized_study_hours = 0
            summarized_credits_number = 0.0
            summarized_category = REGULAR_CATEGORY

            for discipline_config in discipline_configs_group_by_name:
                summarized_semesters.append(discipline_config.semester)
                summarized_mark.append(discipline_config.mark)
                summarized_study_hours += discipline_config.study_hours
                summarized_credits_number += discipline_config.credits_number

            summarized_regular_stats_discipline_configs.append(
                DisciplineConfig(
                    summarized_control_form,
                    summarized_name,
                    min(summarized_semesters),
                    summarized_mark,
                    summarized_study_hours,
                    summarized_credits_number,
                    summarized_category,
                )
            )

        summarized_regular_stats_discipline_configs.sort(
            key=lambda summarized_discipline_config: summarized_discipline_config.semester
        )

        stats_discipline_configs[REGULAR_CATEGORY] = summarized_regular_stats_discipline_configs

    return students_stats_with_discipline_configs_grouped_by_category_summarized


def get_disciplines_for_student_config(
    stats_discipline_configs: list[DisciplineConfig],
) -> list[tuple[str, str, str]]:
    """
    Formats a list of discipline configurations for output, including name, hours, credits, and marks.

    :param stats_discipline_configs: A list of discipline configurations for a student.
    :type stats_discipline_configs: list[DisciplineConfig]
    :return: A list of tuples containing formatted discipline data: (name, hours_and_credits, mark).
    :rtype: list[tuple[str, str, str]]
    """
    disciplines = []
    for discipline_config in stats_discipline_configs:
        discipline_name = discipline_config.name
        discipline_hours = str(discipline_config.study_hours)

        if discipline_config.credits_number.is_integer():
            discipline_credits_number = (
                str(int(discipline_config.credits_number))
                if int(discipline_config.credits_number) != 0
                else ''
            )
        else:
            discipline_credits_number = str(discipline_config.credits_number).replace('.', ',')

        if discipline_credits_number == '':
            discipline_hours_and_credits_number = discipline_hours
        else:
            discipline_hours_and_credits_number = discipline_hours + CREDITS_NUMBER_TEMPLATE.format(
                discipline_credits_number
            )

        if isinstance(discipline_config.mark, list):
            if all(mark == CREDIT_MARK for mark in discipline_config.mark):
                discipline_mark = MARKS_MAPPING[CREDIT_MARK]
            else:
                discipline_mark = ', '.join(MARKS_MAPPING[mark] for mark in discipline_config.mark)
        else:
            discipline_mark = MARKS_MAPPING[discipline_config.mark]

        disciplines.append((discipline_name, discipline_hours_and_credits_number, discipline_mark))

    return disciplines


def get_students_configs(
    students_stats_with_discipline_configs_grouped_by_category_summarized: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE,
    diploma_themes_df: DataFrame,
) -> list[StudentConfig]:
    """
    Generates a list of student configurations, including formatted disciplines and diploma themes.

    :param students_stats_with_discipline_configs_grouped_by_category_summarized:
        Summarized discipline configurations grouped by category for all students.
    :type students_stats_with_discipline_configs_grouped_by_category_summarized:
        STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE
    :param diploma_themes_df: A DataFrame containing student names and their corresponding diploma themes.
    :type diploma_themes_df: DataFrame
    :return: A list of StudentConfig objects containing structured student data.
    :rtype: list[StudentConfig]
    """
    students_configs = []

    diploma_themes_dict = diploma_themes_df.set_index(DIPLOMA_THEMES_DATAFRAME_FULL_NAME_COLUMN)[
        DIPLOMA_THEMES_DATAFRAME_THEME_COLUMN
    ].to_dict()
    for (
        full_name,
        stats_disciplines_configs,
    ) in students_stats_with_discipline_configs_grouped_by_category_summarized.items():
        student_full_name = full_name

        student_regular_disciplines = get_disciplines_for_student_config(
            stats_disciplines_configs[REGULAR_CATEGORY]
        )

        student_course_work_disciplines = get_disciplines_for_student_config(
            stats_disciplines_configs[COURSE_WORK_CATEGORY]
        )

        student_course_project_disciplines = get_disciplines_for_student_config(
            stats_disciplines_configs[COURSE_PROJECT_CATEGORY]
        )

        student_practice_disciplines = get_disciplines_for_student_config(
            stats_disciplines_configs[PRACTICE_CATEGORY]
        )

        student_diploma_theme = diploma_themes_dict[full_name]

        students_configs.append(
            StudentConfig(
                student_full_name,
                student_regular_disciplines,
                student_course_work_disciplines,
                student_course_project_disciplines,
                student_practice_disciplines,
                student_diploma_theme,
            )
        )

    return students_configs


def get_students_with_avg_mark(
    students_stats_with_discipline_configs: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE,
) -> STUDENTS_WITH_AVG_MARK_TYPE:
    """
    Calculates the average mark for each student and sorts them in descending order.

    :param students_stats_with_discipline_configs: A dictionary mapping student names to their discipline configurations.
    :type students_stats_with_discipline_configs: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE
    :return: A sorted tuple of student names with their average marks, from highest to lowest.
    :rtype: STUDENTS_WITH_AVG_MARK_TYPE
    """
    students_with_avg_mark = []
    for (
        student_full_name,
        stats_discipline_configs,
    ) in students_stats_with_discipline_configs.items():
        student_marks = [
            stats_discipline_config.mark
            for stats_discipline_config in stats_discipline_configs
            if isinstance(stats_discipline_config.mark, int)
        ]
        avg_mark = sum(student_marks) / len(student_marks) if student_marks else 0
        students_with_avg_mark.append((student_full_name, avg_mark))

    return tuple(sorted(students_with_avg_mark, key=lambda x: x[1], reverse=True))
