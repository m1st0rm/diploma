from backend.custom_typing import (
    STUDENTS_STATS_RAW_TYPE,
    STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS
)
from backend.classes.discipline_config import DisciplineConfig


PRACTICE_ABBREVIATION = 'ПР'
COURSE_PROJECT_ABBREVIATION = 'КП'
COURSE_WORK_ABBREVIATION = 'КР'

REGULAR_DISCIPLINES_KEY = 'regular_disciplines'
PRACTICE_DISCIPLINES_KEY = 'practice_disciplines'
COURSE_PROJECT_DISCIPLINES_KEY = 'course_project_disciplines'
COURSE_WORK_DISCIPLINES_KEY = 'course_work_disciplines'


def get_students_stats_with_discipline_configs(
        students_stats: STUDENTS_STATS_RAW_TYPE
) -> STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS:
    students_stats_with_discipline_configs = {}
    for student_stats in students_stats:
        for student_full_name, disciplines_dict in student_stats.items():
            discipline_configs = []
            for discipline_info, discipline_mark in disciplines_dict.items():
                discipline_control_form = discipline_info.split(':')[2]
                discipline_name = discipline_info.split('.')[1].split('/')[0]
                discipline_semester = int(discipline_info.split('.')[0])
                discipline_study_hours = int(discipline_info.split('/')[1].split(':')[0])
                discipline_credits_number = float(discipline_info.split('/')[1].split(':')[1])

                if discipline_control_form == PRACTICE_ABBREVIATION:
                    discipline_category = 'practice'
                elif discipline_control_form == COURSE_PROJECT_ABBREVIATION:
                    discipline_category = 'course project'
                elif discipline_control_form == COURSE_WORK_ABBREVIATION:
                    discipline_category = 'course work'
                else:
                    discipline_category = 'regular'

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
