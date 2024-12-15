from backend.classes.discipline_config import DisciplineConfig

STUDENTS_STATS_RAW_TYPE = list[dict[str, dict[str, str | int]]]
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_TYPE = dict[str, list[DisciplineConfig]]
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_TYPE = dict[str, dict[str, list[DisciplineConfig]]]
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS_GROUPED_BY_CATEGORY_SUMMARIZED_TYPE = dict[str, dict[str, list[DisciplineConfig]]]
