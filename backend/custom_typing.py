"""
Module defining custom typing aliases for student statistics and discipline configurations.

This module provides type aliases to simplify and clarify the representation of data structures used
to handle raw student statistics, discipline configurations, and their groupings.

Types:
- STUDENTS_STATS_RAW_TYPE: Represents raw student statistics before processing.
- STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE: Maps student names to their list of discipline configurations.
- STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE:
    Maps student names to categorized lists of discipline configurations.
- STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE:
    Represents summarized discipline configurations grouped by categories.

Dependencies:
- DisciplineConfig: A class representing the structure of a discipline configuration.
"""

from backend.classes.discipline_config import DisciplineConfig

STUDENTS_STATS_RAW_TYPE = list[dict[str, dict[str, str | int]]]
"""
STUDENTS_STATS_RAW_TYPE: A list of dictionaries representing raw student statistics.

- Outer list: Represents multiple student records.
- Outer dictionary key: Student's full name (str).
- Inner dictionary key: Encoded discipline information (str).
- Inner dictionary value: Discipline mark or hours (str | int).
"""


STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE = dict[str, list[DisciplineConfig]]
"""
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE: Maps student names to their list of DisciplineConfig objects.

- Key: Student's full name (str).
- Value: A list of DisciplineConfig objects representing the student's disciplines.
"""

STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE = dict[
    str, dict[str, list[DisciplineConfig]]
]
"""
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE: 
Maps student names to their discipline configurations grouped by categories.

- Outer key: Student's full name (str).
- Outer value: Dictionary mapping discipline categories to a list of DisciplineConfig objects.
    - Inner key: Discipline category (e.g., 'regular', 'practice', etc.).
    - Inner value: List of DisciplineConfig objects within the given category.
"""

STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE = dict[
    str, dict[str, list[DisciplineConfig]]
]
"""
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE: 
Represents summarized discipline configurations grouped by categories.

- Outer key: Student's full name (str).
- Outer value: Dictionary mapping discipline categories to a summarized list of DisciplineConfig objects.
    - Inner key: Discipline category (e.g., 'regular', 'practice', etc.).
    - Inner value: List of summarized DisciplineConfig objects.
"""


STUDENTS_WITH_AVG_MARK_TYPE = tuple[tuple[str, float], ...]
"""
STUDENTS_WITH_AVG_MARK_TYPE: A tuple containing multiple tuples of student names and their average marks.

- Outer tuple: Represents multiple student records.
- Inner tuple:
    - First element: Student's full name (str).
    - Second element: Average mark (float).
"""
