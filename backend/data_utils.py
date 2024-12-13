from backend.custom_typing import (
    STUDENTS_STATS_NON_AGGREGATED_TYPE as students_stats_non_aggregated_type,
    STUDENTS_STATS_AGGREGATED_BY_CONTROL_FORM_TYPE as students_stats_aggregated_by_control_form_type,
)


PRACTICE_ABBREVIATION = 'ПР'
COURSE_PROJECT_ABBREVIATION = 'КП'
COURSE_WORK_ABBREVIATION = 'КР'

REGULAR_DISCIPLINES_KEY = 'regular_disciplines'
PRACTICE_DISCIPLINES_KEY = 'practice_disciplines'
COURSE_PROJECT_DISCIPLINES_KEY = 'course_project_disciplines'
COURSE_WORK_DISCIPLINES_KEY = 'course_work_disciplines'


def get_students_stats_aggregated_by_control_form(
        students_stats: students_stats_non_aggregated_type
) -> students_stats_aggregated_by_control_form_type:
    students_stats_aggregated_by_control_form = []

    for student_stats in students_stats:
        regular_disciplines = []
        practice_disciplines = []
        course_project_disciplines = []
        course_work_disciplines = []
        for full_name, disciplines_dict in student_stats.items():
            for discipline_name, discipline_mark in disciplines_dict.items():
                discipline_category = discipline_name.split(':')[-1]
                if discipline_category == PRACTICE_ABBREVIATION:
                    practice_disciplines.append({discipline_name: discipline_mark})
                elif discipline_category == COURSE_PROJECT_ABBREVIATION:
                    course_project_disciplines.append({discipline_name: discipline_mark})
                elif discipline_category == COURSE_WORK_ABBREVIATION:
                    course_work_disciplines.append({discipline_name: discipline_mark})
                else:
                    regular_disciplines.append({discipline_name: discipline_mark})

            regular_disciplines_dict = {k: v for d in regular_disciplines for k, v in d.items()}
            practice_disciplines_dict = {k: v for d in practice_disciplines for k, v in d.items()}
            course_work_disciplines_dict = {k: v for d in course_work_disciplines for k, v in d.items()}
            course_project_disciplines_dict = {k: v for d in course_project_disciplines for k, v in d.items()}

            students_stats_aggregated_by_control_form.append({full_name: {
                REGULAR_DISCIPLINES_KEY: regular_disciplines_dict,
                PRACTICE_DISCIPLINES_KEY: practice_disciplines_dict,
                COURSE_PROJECT_DISCIPLINES_KEY: course_project_disciplines_dict,
                COURSE_WORK_DISCIPLINES_KEY: course_work_disciplines_dict,
            }})

    return students_stats_aggregated_by_control_form
