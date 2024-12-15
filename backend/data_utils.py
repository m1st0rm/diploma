from backend.custom_typing import (
    STUDENTS_STATS_RAW_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE
)
from backend.classes.discipline_config import DisciplineConfig


PRACTICE_ABBREVIATION = 'ПР'
COURSE_PROJECT_ABBREVIATION = 'КП'
COURSE_WORK_ABBREVIATION = 'КР'

PRACTICE_CATEGORY = 'practice'
COURSE_PROJECT_CATEGORY = 'course_project'
COURSE_WORK_CATEGORY = 'course_work'
REGULAR_CATEGORY = 'regular'


def get_students_stats_with_discipline_configs(
        students_stats: STUDENTS_STATS_RAW_TYPE
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE:
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
                    discipline_category
                )
                discipline_configs.append(discipline_config)
            students_stats_with_discipline_configs[student_full_name] = discipline_configs

    return students_stats_with_discipline_configs


def get_students_stats_with_discipline_configs_grouped_by_category(
        students_stats_with_discipline_configs: STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE:
    students_stats_with_discipline_configs_grouped_by_category = {}
    categories = (REGULAR_CATEGORY, COURSE_WORK_CATEGORY, COURSE_PROJECT_CATEGORY, PRACTICE_CATEGORY)
    for student_full_name, stats_discipline_configs in students_stats_with_discipline_configs.items():
        discipline_configs_grouped_by_category = {
            REGULAR_CATEGORY: [],
            COURSE_WORK_CATEGORY: [],
            COURSE_PROJECT_CATEGORY: [],
            PRACTICE_CATEGORY: []
        }

        for stats_discipline_config in stats_discipline_configs:
            if stats_discipline_config.categoty == PRACTICE_CATEGORY:
                discipline_configs_grouped_by_category[PRACTICE_CATEGORY].append(stats_discipline_config)
            elif stats_discipline_config.categoty == COURSE_WORK_CATEGORY:
                discipline_configs_grouped_by_category[COURSE_WORK_CATEGORY].append(stats_discipline_config)
            elif stats_discipline_config.categoty == COURSE_PROJECT_CATEGORY:
                discipline_configs_grouped_by_category[COURSE_PROJECT_CATEGORY].append(stats_discipline_config)
            else:
                discipline_configs_grouped_by_category[REGULAR_CATEGORY].append(stats_discipline_config)

        for category in categories:
            discipline_configs_grouped_by_category[category].sort(
                key=lambda discipline_config: discipline_config.semester)

        students_stats_with_discipline_configs_grouped_by_category[
            student_full_name] = discipline_configs_grouped_by_category

    return students_stats_with_discipline_configs_grouped_by_category
